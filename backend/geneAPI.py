import re
import os
import ast
import boto3
import logging
import pymongo as pm
import psycopg2 as pypg
from botocore.config import Config
from bottle import Bottle, request, response, post, get, put, delete, run
cqs = '''select count(*) from public.registered_users where '''
snt = '''select user_name,user_type '''
app = Bottle(__name__)
emailpattern = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
passwordpattern = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
mc = pm.MongoClient("mongodb://localhost:27017")
con = pypg.connect(user='postgres', password='password', database='postgres')
cur = con.cursor()
mys = boto3.session.Session()
myr = mys.region_name
client = boto3.client('s3')
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# and
# and
# %s,%s
# execute
# execute
# execute
# execute
# %s
#
#
#
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# @adata
# @adata
# @a
# @a
# @a
# @a
# @a
# @a


@app.post('/login')
def login():
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if data is None:
            raise ValueError
        try:
            if ('user_name' in data.keys() and 'password' in data.keys()):
                try:
                    ud = (data['user_name'], data['password'])
                    cur.execute(cqs + "user_name=%s and password=%s", ud)
                    a = cur.fetchone()[0]
                    if a == 1:
                        response.body = str(
                            {"success": True, "status": True, "message": "Logged In Successfully"})
                    else:
                        response.body = str(
                            {"success": False, "status": False, "message": "User Does Not Exist"})
                except Exception as e:
                    print(e)
                    error = e.args[0].split('\n')[0]
                    response.body = str(
                        {"success": False, "status": False, "message": error})
            else:
                raise ValueError
        except (TypeError, KeyError):
            raise ValueError

    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/register')
def register():
    try:
        try:
            data = request.json
        except:
            raise ValueError
        if data is None or data == {}:
            raise ValueError
        try:
            if 'user_name' in data.keys() and 'password' in data.keys() and 'user_type' in data.keys() and 'user_email' in data.keys() and emailpattern.match(data['user_email']) != None and passwordpattern.match(data['password']) != None:
                ud = (data['user_name'], data['user_type'],
                      data['user_email'], data['password'])
                cur.execute(
                    cqs+'''user_name=%s and user_type=%s and user_email=%s and password=%s''', ud)
                if cur.fetchone()[0] == 0:
                    try:
                        user_data = (data['user_name'],
                                     data['date_of_birth'], data['gender'], data['mobile_number'], data['user_email'], data['pincode'], data['user_type'], data['password'])
                        cur.execute(
                            '''insert into public.registered_users(user_name, date_of_birth, gender, mobile_number, user_email, pincode, user_type, password) values (%s , %s , %s , %s , %s , %s , %s , %s)''', user_data)
                        con.commit()
                        response.body = str(
                            {"success": True, "status": True, "message": "User Registered Successfully"})
                    except Exception as e:
                        error = e.args[0].split('\n')[0]
                        response.body = str(
                            {"success": False, "status": False, "message": error})
                else:
                    response.body = str(
                        {"success": True, "status": True, "message": "User is Already Registered, Please Login"})
        except (TypeError, KeyError):
            raise ValueError
    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/userDetails')
def getUserDetails():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'user_id' in data.keys():
            user_id = data['user_id']
            try:
                cur.execute(
                    '''select user_name,date_of_birth,gender,mobile_number,user_email,pincode,user_type from public.registered_users where user_id=%s''', (user_id))
                dft = [dict(zip([col[0] for col in cur.description], row))
                       for row in cur]
                if dft is not None and dft != []:
                    fd = dft[0]
                    fd['date_of_birth'] = fd['date_of_birth'].strftime(
                        "%Y-%m-%d %H:%M:%S")
                    response.body = str(
                        {"success": True, "status": True, "message": "User Details", "result": str(fd)})
                else:
                    response.body = str(
                        {"success": True, "status": True, "message": "User Details"})
            except Exception as e:
                print(e)
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Content-Type'] = 'application/json'
    rb = ast.literal_eval(response.body)
    result = ast.literal_eval(rb['result']) if 'result' in rb.keys() else None
    if result is not None:
        rb['result'] = result
    return rb


@app.put('/updateUserDetails')
def updateUserData():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'user_id' in data.keys():
            ud1 = (data['user_name'], data['password'],
                   data['date_of_birth'], data['gender'], data['pincode'], data['user_email'], data['mobile_number'], data['user_id'])
            try:
                cur.execute(
                    '''update public.registered_users set user_name=%s, password=%s, date_of_birth=%s, gender=%s, pincode=%s, user_email=%s, mobile_number=%s where user_id=%s''', ud1)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "User Details Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError

    except ValueError:
        response.status = 400
        return
    except KeyError as e:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteUser')
def deleteUser():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'user_id' in data.keys():
            try:
                cur.execute(
                    '''delete from public.registered_users where user_id=%s''', (data['user_id']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "User Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/storeDocs')
def storeDocs():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'user_id' in data.keys() and 'doc_type' in data.keys() and 'doc_url' in data.keys():
            try:
                cur.execute(
                    '''insert into public.documents(user_id, doc_type, doc_url) values(%s,%s,%s)''', (data['user_id'], data['doc_type'], data['doc_url']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Document Uploaded Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteDoc')
def deleteDocument():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'doc_id' in data.keys():
            try:
                cur.execute(
                    '''delete from public.documents where doc_id=%s''', (data['doc_id']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Document Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/addDiseaseCategory')
def addDiseaseCategory():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'disease_category' in data.keys():
            try:
                cur.execute(
                    '''insert into public.disease_categories(disease_category) values(%s)''', (data['disease_category'],))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Category Added Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.put('/updateDiseaseCategory')
def updateDiseaseCategory():
    try:
        data = request.json
        if data == {} or data is None:
            raise ValueError
        elif 'disease_category' in data.keys() and 'disease_category_id' in data.keys():
            try:
                cur.execute(
                    '''update public.disease_categories set disease_category = %s where disease_category_id = %s''', (data['disease_category'], data['disease_category_id']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Category Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteDiseaseCategory')
def deleteDiseaseCategory():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'disease_category_id' in data.keys():
            try:
                cur.execute(
                    '''delete from public.disease_categories where disease_category_id = %s''', (data['disease_category_id']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Category Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/addDisease')
def addDisease():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'disease_category_id' in data.keys() and 'disease' in data.keys():
            try:
                d1 = (data['disease_category_id'], data['disease'])
                cur.execute(
                    '''insert into public.diseases(disease_category_id,disease) values (%s,%s)''', d1)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Added Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.put('/updateDisease')
def updateDisease():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'disease_id' in data.keys() and 'disease' in data.keys() and 'disease_category_id' in data.keys():
            try:
                d1 = (data['disease'], data['disease_category_id'],
                      data['disease_id'])
                cur.execute(
                    '''update public.diseases set disease=%s , disease_category_id= %s where disease_id=%s''', d1)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteDisease')
def deleteDisease():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'disease_id' in data.keys():
            try:
                a = (data['disease_id'],)
                cur.execute(
                    '''delete from public.diseases where disease_id=%s''', a)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/addGene')
def addGene():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'gene' in data.keys() and 'gene_type' in data.keys():
            try:
                cur.execute(
                    '''insert into public.genes(gene,gene_type) values(%s,%s)''', (data['gene'], data['gene_type']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Gene Added Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.put('/updateGene')
def updateGene():
    try:
        data = request.json
        if data == {} or data is None:
            raise ValueError
        elif 'gene' in data.keys() and 'gene_type' in data.keys() and 'gene_id' in data.keys():
            try:
                cur.execute(
                    "update public.genes set gene=%s, gene_type=%s where gene_id=%s", (data['gene'], data['gene_type'], data['gene_id']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Gene Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteGene')
def deleteGene():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'gene_id' in data.keys():
            try:
                p = (data['gene_id'],)
                cur.execute('''delete from public.genes where gene=%s''', p)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Gene Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/addSymptom')
def addSymptom():
    try:
        data = request.json
        if data == {} or data is None:
            raise ValueError
        elif 'symptom' in data.keys():
            try:
                a = (data['symptom'],)
                cur.execute(
                    '''insert into public.symptoms(symptom) values(%s)''', a)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Symptom Added Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.put('/updateSymptom')
def updateSymptom():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'symptom' in data.keys() and 'symptom_id' in data.keys():
            try:
                cur.execute(
                    '''update public.symptoms set symptom=%s where symptom_id=%s''', (data['symptom'], data['symptom_id']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Symptom Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteSymptom')
def deleteSymptom():
    try:
        data = request.json
        if data is None or data == {}:
            raise ValueError
        elif 'symptom_id' in data.keys():
            try:
                v = (data['symptom_id'],)
                cur.execute(
                    '''delete from public.symptoms where symptom_id=%s''', v)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Symptom Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/postToS3')
def postFileToS3():
    try:
        data = request.files['file']
        folder = ''
        fps = os.path.join("temp", data.filename)
        if fps.endswith(".jpg") or fps.endswith(".png") or fps.endswith(".svg"):
            folder = 'img/'
        elif fps.endswith(".pdf"):
            folder = 'pdf/'
        elif fps.endswith(".doc") or fps.endswith(".docx"):
            folder = 'doc/'
        data.save(fps)
        client.upload_file(fps, 'gene-onto', folder +
                           '{}'.format(data.filename))
        os.remove(fps)
        url = "http://s3-" + myr + ".amazonaws.com/gene-onto/" + folder + data.filename
        response.body = str(
            {"success": True, "status": True, "message": "Document Posted to Bucket Successfully", "location": url})
    except Exception as e:
        error = e.args[0].split('\n')[0]
        response.body = str(
            {"success": False, "status": False, "message": error})
    return ast.literal_eval(response.body)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000')
