import re
import ast
import bottle
import pymongo as pm
import psycopg2 as pypg
from google.cloud import storage
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

# cur.execute("show tables")
# cur.execute("insert into public.registered_users(user_name, user_type, user_mail, date_of_birth, gender, city, phone_no, password) values " % )
# cur.execute(snt+"mail='%s' and password='%s'")
# cur.execute("""update marklist set total=300276""")
# and
# cqs + "user_mail='%s' and password='%s'" total
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''
# ''''''


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
                        # "select * from ghis " "insert into gened values('"+did+"','"+dn+"','"+as+"','"+dt+"','"+sym+"','"+pre+"','"+ppi+"')" "Select * from gene1" "Select * from bf "
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
                        print(e)
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


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000')
