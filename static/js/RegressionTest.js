'use strict';
var request = require('request');
var async = require('asyncawait/async');
var await = require('asyncawait/await');
var jsonDiff = require('json-diff')
var util = require('util')
const fs = require('fs');
var dateFormat = require('dateformat');
const AWS = require('aws-sdk');
var csv = require("csvtojson");
require('./config');
var prepHtml = require('./HTMLStatusReport')
var logs = require('./winstonLogger')
const logger = logs.wlog;

var eventDetails = {}
var authToken = ''
var finalResult = []
var outputResultForTable = {}
var s3 = new AWS.S3();
var fileRefKey = ''
var eventId = ''
var validStatus = ''
var fetchtestResult = ''

async function initiateRegressionTest() {
    var loginResult = await (login());
}
//login to idx
async function login() {
    var loginReq = {// login credentials
        "userName": USER_NAME,
        "password": PASSWORD
    }
    return new Promise(function (resolve, reject) {
        request.post({// api call
            headers: { 'content-type': 'application/json', 'domain': 'intellectseec' },
            url: LOGIN_URL,
            body: JSON.stringify(loginReq)// servers operate using only strings, hence we convert the JS object that contains the login credentials to string using stringify() before taking it to the server
        }, function (error, response, body) {
            if (error) {
                logger.log('error', error);
                resolve(error)
            } else {
                try {
                    logger.log('info', 'resp from login service: ' + body)
                    var loginRes = JSON.parse(body);// again we arrive to client, hence we revert it back to a JS object
                    if (loginRes['output'] === "success") {
                        if (!authToken) {// checks whether an authentication token is already present
                            authToken = loginRes['authToken'];
                            if (authToken) {
                                regressionTestPack();// After succesful login, get the file and start the test 
                                resolve(true)
                            } else {
                                logger.log('error', 'Login failed')// Abort as Failed login
                            }
                        } else {
                            logger.log('info', 'token renewed successfully')// A token's validity is 1 Hour
                            authToken = loginRes['authToken'];// hence, it should be renewed at time intervals of 1 Hour
                            if (authToken) {
                                resolve(authToken)
                            }
                        }
                    }
                } catch (error) {
                    logger.log('error', 'Login Catch block - Error in login service.')// Abort as Failed login
                    logger.log('error', error)
                    resolve(false)
                }
            }
        });
    });
}
//regression tester
async function regressionTestPack() {
    // Check if files.csv exists in local or S3
    try {// Checking whether the path given in destinationFilePath exists
        if (fs.existsSync(destinationFilePath)) {// Checking whether the file exists in the local i.e the given local path
            var checkIfFileExists = fs.existsSync(destinationFilePath)
        }
    } catch (err) {
        logger.log('error', err)
    }

    if (checkIfFileExists) {
        var csvFilePath = destinationFilePath
    } else {
        //Fetching file from s3
        if (s3 && BUCKET_NAME && S3_FOLDER_PATH && S3_FILE_PATH) {
            var s3DownloadParams = {
                Bucket: BUCKET_NAME,
                Key: S3_FILE_PATH
            };
            var fileContent = await (fetchFileFromS3(s3, s3DownloadParams));
            if (fileContent) {
                var fileSavedInLocalFromS3 = await (writeFileToLocalFromS3(destinationFilePath, fileContent));//copying the file content from S3 to Local
            }
            if (!fileSavedInLocalFromS3) {
                logger.log('error', "Failure in fetching file from s3");
                return false
            } else {
                var csvFilePath = destinationFilePath
            }
        } else {
            logger.log('error', 'Failed at S3 - csv')
        }
    }
    // Generate a JSON from the contents of the CSV file
    if (csvFilePath) {
        csv().fromFile(csvFilePath)
            .then((jsonObj) => {
                logger.log('info', jsonObj);
            })
        // Async / await usage
        const fileListJson = await csv().fromFile(csvFilePath);
        let currentDateTime = dateFormat(new Date(), "yyyy_mm_dd_HH_MM_ss");// getting today's date & time
        if(!fs.existsSync('final_result/RegressionTest'+currentDateTime)){// if the file doesn't exist,
            fs.mkdirSync('final_result/RegressionTest'+currentDateTime);// create the same
        }
        if (!fs.existsSync('final_result/RegressionTest' + currentDateTime + '/Individual_Results')) {// if the file doesn't exist,
            fs.mkdirSync('final_result/RegressionTest' + currentDateTime + '/Individual_Results');// create the same
        }
        // Loop through each file and fetchTestResult
        for (var i = 0; i < fileListJson.length; i++) {
            let obj = fileListJson[i];
            logger.log('info', 'before pullfrom S3 ' + S3_FOLDER_PATH + fileListJson[i]['folderName'] + fileListJson[i]['fileName'])
            var fetchTestResult = await initializeTest(obj)
            if (fetchTestResult) {
                var s3FetchExpOpJSONDownloadParams = {
                    Bucket: BUCKET_NAME,
                    Key: S3_FOLDER_PATH + obj.folderName + obj.expectedJSON
                }
                var fetchExpOpFromS3 = await (fetchFileFromS3(s3, s3FetchExpOpJSONDownloadParams));
                if (fetchExpOpFromS3) {
                    try {
                        logger.log('info', 'Op of fetchExpOpFromS3 : ' + fetchExpOpFromS3)
                        var expectedOp = JSON.parse(fetchExpOpFromS3)
                        if (fetchTestResult['values'] && expectedOp && expectedOp['values']) {
                            // Checking the JSON keys
                            var keys_expected = Object.keys(expectedOp['values']);
                            keys_expected.sort();
                            var keys_actual = Object.keys(fetchTestResult['values']);
                            keys_actual.sort();
                            var isKeyMatch = compareObjects(keys_expected, keys_actual);
                            logger.log('info', 'JSON Key Match :' + isKeyMatch)
                            // json-diff npm package for both labels and values
                            var diff = jsonDiff.diffString(expectedOp['values'], fetchTestResult['values']);
                            logger.log('info', diff)
                            var isJSONMatch = (diff) ? false : true // if the 2 JSONs match, their differences are nothing. Hence, 'diff' should contain nothing if the JSONs are equal and should have any value that should'nt pertain to false if they are'nt equal
                            var outputResult = {}
                            var outputResult = prepRegressionTestResultJSON(expectedOp['values'], fetchTestResult['values'])
                            eventDetails[obj.fileName]['expectedOutput'] = expectedOp['values']
                            eventDetails[obj.fileName]['jsonKeyMatch'] = isKeyMatch
                            eventDetails[obj.fileName]['isJSONMatch'] = isJSONMatch
                            eventDetails[obj.fileName]['difference'] = diff
                            eventDetails[obj.fileName]['regressionTest'] = "success"
                            eventDetails[obj.fileName]['fetchTestResult'] = fetchTestResult
                            eventDetails[obj.fileName]['outputResult'] = outputResult
                        } else {
                            logger.log('info', "fetchTestResult does not have values key")
                            eventDetails[obj.fileName]['expectedOutput'] = expectedOp['values']
                            eventDetails[obj.fileName]['regressionTest'] = "failure"
                            eventDetails[obj.fileName]['failed_at'] = "Values key is empty on response from fetchTestResult Api"
                            eventDetails[obj.fileName]['fetchTestResult'] = fetchTestResult
                        }
                    } catch (error) {
                        logger.log('error', 'fetchExpOpFromS3 Catch block - Error in fetchExpOpFromS3.')
                        logger.log('error', error)
                        break;
                    }
                } else {
                    eventDetails[obj.fileName]['isJSONMatch'] = 'NA'
                    eventDetails[obj.fileName]['regressionTest'] = "failure"
                    eventDetails[obj.fileName]['failed_at'] = "fetchExpectedJSONFile"
                }
            } else {
                eventDetails[obj.fileName]['id'] = obj.id
                eventDetails[obj.fileName]['isJSONMatch'] = 'NA'
                eventDetails[obj.fileName]['scenario'] = obj.scenario
                eventDetails[obj.fileName]['fileName'] = obj.fileName
                eventDetails[obj.fileName]['fileId'] = 'NA'
                eventDetails[obj.fileName]['processStatus'] = 'F'
            }
        }
        var finalOutput = { eventDetails: eventDetails }
        fs.writeFile('final_result/RegressionTest' + currentDateTime + '/TestResult'+'.json', JSON.stringify(finalOutput, null, 2), (err) => {
            if (err) throw err;
            logger.log('info', 'Data written to file');
        });
        logger.log('info', 'eventDetails : ' + util.inspect(eventDetails))
        for (var key in finalOutput.eventDetails) {
            finalResult.push(finalOutput.eventDetails[key])
        }
        // Writing the final json output to a file
        var htmlContent = `
            <!DOCTYPE html>
            <html>
            <head>
                <link rel="stylesheet" type="text/css" href="../../style.css">
                <link rel="stylesheet" href="../../script.css">
                
            </head>
            <body>
                <h1>Regression Test Pack Results <input id="myInput" type="text" placeholder="Search..">
                </h1> 
                
                <table id="mainTable"> 
                <thead>
                <tr>
                    <th><b>S No</b></th>
                    <th><b>File Id</b></th>
                    <th><b>File Name</b></th> 
                    <th><b>Testing Status</b>
                      <select id='filterText' style='display:inline-block' onchange='filterText()'>
                        <option disabled selected>Select</option>
                        <option value='SUCCESS'>SUCCESS</option>
                        <option value='FAILURE'>FAILURE</option>4
                        <option value='ALL'>ALL</option>
                      </select>
                    </th>
                    <th><b>File Process Status</b></th> 
                    <th><b>Scenario</b></th>
                    <th><b>Test Result(Pass/Fail)</b</th>
                    <th><b>Failure Reason</b></th>
                </tr>      
                </thead>
                <tbody id="resultTable">        
                ${ finalResult.map((data) => prepHtml.eventTemplate(data,currentDateTime)).join("")}
                </tbody>
                </table>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
                <script src="../../script.js"></script>
            </body>
            </html>
        `;
        fs.writeFile('final_result/RegressionTest'+currentDateTime+'/ConsolidatedTestResult.html', htmlContent, (err) => {
            if (err) throw err;
            logger.log('info', 'Html Data written to file');
        });
    }
}
async function fetchFileFromS3(s3, s3DownloadParams) {
    //Fetch or read data from aws s3
    return new Promise(function (resolve, reject) {
        s3.headObject(s3DownloadParams, function (err, data) {
            if (err) {
                logger.log('error', 'Reading metadata from S3 failed.');
                logger.log('error', err, err.stack);
                logger.log('info', s3DownloadParams)
                resolve(false)
            } else {
                s3.getObject(s3DownloadParams, function (err, data) {
                    if (err) {
                        logger.log('error', 'Download from S3 failed.');
                        logger.log('error', err, err.stack);
                        resolve(false)
                    } else {
                        logger.log('info', 'Download from S3 success.');
                        var fileContent = data.Body.toString('utf-8');
                        resolve(fileContent)
                    }
                });
            }
        });
    });
}
// copying the file fetched from s3 to local for processing
async function writeFileToLocalFromS3(destinationFilePath, fileContent) {
    return new Promise(function (resolve, reject) {
        fs.writeFile(destinationFilePath, fileContent, function (err) {
            if (err) {
                logger.log('error', 'Unable to save downloaded file locally.');
                logger.log('error', err, err.stack);
                resolve(err)
            } else {
                logger.log('info', 'Downloaded s3 file saved locally.');
                resolve(true)
            }
        });
    });

}
// preparing a test event
async function initializeTest(obj) {
    fileRefKey = await (pullFromS3(obj));
    if (fileRefKey) {
        eventId = await (initiateTest(obj, fileRefKey));
        if (eventId) {
            await sleep(30000);
            validStatus = await (checkEventStatus(obj, eventId, fileRefKey));
            if (validStatus['output'] === "success" && validStatus['files'] && validStatus['files'][0]['processStatus'] === "S") {
                var fetchtestResult = await (fetchTestResult(obj, eventId, fileRefKey));
            } else {
                logger.log('error', "checkEventStatus failed for :" + obj.fileName);
                eventDetails[obj.fileName] = {}
                eventDetails[obj.fileName]['regressionTest'] = "failure"
                eventDetails[obj.fileName]['failed_at'] = "checkEventStatus"
            }
        } else {
            logger.log('error', 'initiateTest failed for :' + obj.fileName)
            eventDetails[obj.fileName] = {}
            eventDetails[obj.fileName]['regressionTest'] = "failure"
            eventDetails[obj.fileName]['failed_at'] = "initiateTest"
        }
    } else {
        logger.log('error', 'pullFromS3 failed for :' + obj.fileName)
        eventDetails[obj.fileName] = {}
        eventDetails[obj.fileName]['regressionTest'] = "failure"
        eventDetails[obj.fileName]['failed_at'] = "pullFromS3"
    }
    return fetchtestResult
}
async function pullFromS3(obj) {
    var pullFromS3req = {
        "S3FilePath": S3_FOLDER_PATH + obj.folderName + obj.fileName,
        "S3FileName": obj.fileName,
        "groupId": "RegressionTest",
        "bucket": BUCKET_NAME
    }
    return new Promise(function (resolve, reject) {
        request.post({// api call
            headers: { 'content-type': 'application/json', 'domain': 'intellectseec', 'authorization': 'Bearer ' + authToken },
            url: PULL_FROM_S3_URL,
            body: JSON.stringify(pullFromS3req)
        }, async function (error, response, body) {
            if (error) {
                logger.log('error', error)
                resolve(error);
            } else {
                try {
                    logger.log('info', 'Op for pullFromS3 : ' + body)
                    var resultOp = JSON.parse(body);
                    if (resultOp && resultOp['output'] && resultOp['output'] === "failure" && resultOp['message'] === AUTH_TOKEN_INVALID) {
                        var loginResult = await (login());
                        if (loginResult) {
                            resolve(pullFromS3(obj));
                        }
                    } else {
                        resolve(resultOp['fileRefKey']);
                    }
                } catch (error) {
                    logger.log('error', 'pullFromS3 catch block');
                    logger.log('error', error);
                    resolve(false)
                }
            }
        });
    });
}
//starting the test
async function initiateTest(obj, fileRefKey) {
    var initiateTestReq = {
        "fileRefKey": fileRefKey,
        "docType": obj.docType,
        "groupId": "RegressionTest"
    }
    return new Promise(function (resolve, reject) {
        request.post({// api call
            headers: { 'content-type': 'application/json', 'domain': 'intellectseec', 'authorization': 'Bearer ' + authToken },
            url: INITIATE_TEST_URL,
            body: JSON.stringify(initiateTestReq)
        }, async function (error, response, body) {
            if (error) {
                logger.log('error', error)
                resolve(error);
            } else {
                try {
                    logger.log('info', "op for initiateTest :" + body);
                    var resultOp = JSON.parse(body);
                    if (resultOp && resultOp['output'] && resultOp['output'] === "failure" && resultOp['message'] === AUTH_TOKEN_INVALID) {
                        var loginResult = await (login());
                        if (loginResult) {
                            resolve(initiateTest(obj, fileRefKey));
                        }
                    } else {
                        resolve(resultOp['eventId']);
                    }
                } catch (error) {
                    logger.log('error', "initiateTest catch block:");
                    logger.log('error', error);
                    resolve(false)
                }
            }
        });
    });
}
// getting the status of the event
async function checkEventStatus(obj, eventId, fileRefKey) {
    var chkEvtStatusReq = {
        "eventId": eventId
    }
    return new Promise(function (resolve, reject) {
        request.post({// api call
            headers: { 'content-type': 'application/json', 'domain': 'intellectseec', 'authorization': 'Bearer ' + authToken },
            url: CHECK_EVENT_STATUS_URL,
            body: JSON.stringify(chkEvtStatusReq)
        }, async function (error, response, body) {
            if (error) {
                logger.log('error', error)
                resolve(error);
            } else {
                try {
                    var status = {}
                    logger.log('info', "op for checkEventStatus :" + body);
                    var eventStatusResult = JSON.parse(body)
                    if (eventStatusResult && eventStatusResult['output'] && eventStatusResult['output'] === "failure" && eventStatusResult['message'] === AUTH_TOKEN_INVALID) {
                        var loginResult = await (login());
                        if (loginResult) {
                            resolve(checkEventStatus(obj, eventId, fileRefKey));
                        }
                    } else if (eventStatusResult['output'] == "success") {
                        if (eventStatusResult['files'][0]['processStatus'] === "S") {//success event
                            eventDetails[obj.fileName] = { id: obj.id, fileName: obj.fileName, eventId: eventId, fileId: eventStatusResult['files'][0]['fileId'], fileRefKey_PullFromS3: fileRefKey, processStatus: eventStatusResult['files'][0]['processStatus'], scenario: obj.scenario }
                            resolve(eventStatusResult)
                        } else if (eventStatusResult['files'][0]['processStatus'] === "G" || eventStatusResult['files'][0]['processStatus'] === "WIP") {// incomplete and still running event
                            await sleep(30000);
                            resolve(checkEventStatus(obj, eventId, fileRefKey));
                        } else if (eventStatusResult['files'][0]['processStatus'] === "F") {//failed event
                            eventDetails[obj.fileName] = { id: obj.id, fileName: obj.fileName, eventId: eventId, fileId: eventStatusResult['files'][0]['fileId'], fileRefKey_PullFromS3: fileRefKey, processStatus: eventStatusResult['files'][0]['processStatus'], scenario: obj.scenario }
                            logger.log('error', 'Event Failed for fileId: ' + eventStatusResult['files'][0]['fileId'])
                            resolve(eventStatusResult)
                        }
                    }
                } catch (error) {
                    logger.log('error', "checkEventStatus catch block");
                    logger.log('error', error);
                    resolve(false)
                }
            }
        });
    });
}
//getting the test result
async function fetchTestResult(obj, eventId, fileRefKey) {
    var fetchTestResultReq = {
        "eventId": eventId,
        "fileRefKey": fileRefKey,
        "doctype": obj.docType,
        "bucket": "",
        "destinationPath": ""
    }
    return new Promise(function (resolve, reject) {
        request.post({// api call
            headers: { 'content-type': 'application/json', 'domain': 'intellectseec', 'authorization': 'Bearer ' + authToken },
            url: FETCH_TEST_RESULT_URL,
            body: JSON.stringify(fetchTestResultReq)
        }, async function (error, response, body) {
            if (error) {
                logger.log('error', rror)
                resolve(error);
            } else {
                try {
                    logger.log('info', "op for fetchTestResult :" + body);
                    var resultOp = JSON.parse(body);
                    if (resultOp && resultOp['output'] && resultOp['output'] === "failure" && resultOp['message'] === AUTH_TOKEN_INVALID) {
                        var loginResult = await (login());
                        if (loginResult) {
                            resolve(fetchTestResult(obj, eventId, fileRefKey));
                        }
                    } else {
                        resolve(resultOp)
                    }
                } catch (error) {
                    logger.log('error', "fetchTestResult catch block");
                    logger.log('error', error);
                    resolve(false)
                }

            }
        });
    });
}
//comparing two JS objects
function compareObjects(obj1, obj2) {
    var equal = true;
    for (var i in obj1)
        if (!obj2.hasOwnProperty(i))
            equal = false;
    return equal;
}
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
//processing the result
function prepRegressionTestResultJSON(expected, actual) {
    for (var e_key in expected) {
        outputResultForTable[e_key] = {}
        outputResultForTable[e_key]['label'] = e_key
        outputResultForTable[e_key]['expectedValue'] = expected[e_key]
        outputResultForTable[e_key]['actualValue'] = ''
        outputResultForTable[e_key]['valueMatchStatus'] = false
        outputResultForTable[e_key]['labelMatchStatus'] = false
        for (var a_key in actual) {
            if (e_key === a_key) {
                var valueMatchStatus = true
                var valDiff = jsonDiff.diffString(expected[e_key], actual[a_key]);
                if (valDiff) {
                    valueMatchStatus = false
                }
                var labelMatchStatus = true
                var keyDiff = jsonDiff.diffString(e_key, a_key);
                if (keyDiff) {
                    labelMatchStatus = false
                }
                outputResultForTable[e_key]['actualValue'] = actual[a_key]
                outputResultForTable[e_key]['valueMatchStatus'] = valueMatchStatus
                outputResultForTable[e_key]['labelMatchStatus'] = labelMatchStatus
                break;
            }
        }
    }
    // For extra labels/ rules in actual op that has been missed in outputResultForTable
    for (var a_key in actual) {
        if (!(a_key in outputResultForTable)) {
            outputResultForTable[a_key] = {}
            outputResultForTable[a_key]['label'] = a_key
            outputResultForTable[a_key]['expectedValue'] = ''
            outputResultForTable[a_key]['actualValue'] = actual[a_key]
            outputResultForTable[a_key]['valueMatchStatus'] = false
            outputResultForTable[a_key]['labelMatchStatus'] = false
        }
    }
    return outputResultForTable
}
module.exports.initiateRegressionTest = initiateRegressionTest;