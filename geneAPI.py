import re
import json
import bottle
import ast
import psycopg2 as pypg
from bottle import Bottle, request, response, post, get, put, delete, run
cqs = "select count(*) from public.registered_users where "
snt = "select user_name,user_type"
app = Bottle(__name__)
emailpattern = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
passwordpattern = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
con = pypg.connect(user='postgres', password='password', database='postgres')
cur = con.cursor()


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
                    cur.execute(
                        cqs + "user_email='{"+data['user_name']+"}' and password='{"+data['password']+"}'")
                    if cur.fetchone()[0] == 1:
                        cur.execute(
                            snt+" from registered_users where user_mail='{"+data['user_name']+"}' and password='{"+data['password'] + "}'")
                        print(dict(cur.fetchall()))
                        response.body = str(
                            {"success": True, "status": True, "message": "Logged In Successfully"})
                    else:
                        response.body = str(
                            {"success": False, "status": False, "message": "User Does Not Exist"})
                except Exception as e:
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
                cur.execute(
                    cqs+"user_name='{"+data['user_name']+"}' and user_type={"+data['user_type']+"} and user_email='{"+data['user_email']+"}' and password='{"+data['password']+"}'")
                if cur.fetchone()[0] == 0:
                    try:
                        cur.execute("insert into public.registered_users(user_name, user_email, user_type, city, gender, password, date_of_birth, mobile_number) values ('{" +
                                    data['user_name']+"}','{" + data['user_email'] + "}',{" + data['user_type']+"},'{"+data['city'] +
                                    "}','{" + data['gender'] + "}','{" + data['password'] + "}',{" + data['date_of_birth'] + "},'" + data['mobile_number'] + "')")
                        con.commit()
                        response.body = str(
                            {"success": True, "status": True, "message": "User Registered Successfully"})
                    except Exception as e:
                        error = e.args[0].split('\n')[0]
                        response.body = str(
                            {"success": False, "status": False, "message": error})
                else:
                    response.body = str(
                        {"success": False, "status": False, "message": "User is Already Registered"})
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


@put('/names/<oldname>')
def update_handler(name):
    '''Handles name updates'''

    try:
        # parse input data
        try:
            data = json.load(request.body)
        except:
            raise ValueError

        # extract and validate new name
        try:
            # if namepattern.match(data['name']) is None:
            #     raise ValueError
            newname = data['name']
        except (TypeError, KeyError):
            raise ValueError

        # check if updated name exists
        # if oldname not in _names:
        #     raise KeyError(404)

        # check if new name exists
        # if name in _names:
        #     raise KeyError(409)

    except ValueError:
        response.status = 400
        return
    except KeyError as e:
        response.status = e.args[0]
        return

    # add new name and remove old name
    # _names.remove(oldname)
    # _names.add(newname)

    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'name': newname})


# @delete('/names/<name>')
# def delete_handler(name):
#     '''Handles name updates'''

#     try:
#         # Check if name exists
#         # if name not in _names:
#         #     raise KeyError
#     except KeyError:
#         response.status = 404
#         return

#     # Remove name
#     # _names.remove(name)
#     return


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000')
