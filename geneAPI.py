import re
import json
import bottle
import ast
import psycopg2 as pypg
from bottle import Bottle, request, response, post, get, put, delete, run
cqs = "select count(*) from public.registered_users where "
snt = "select user_name,user_type"
# app = application = bottle.default_app()
app = Bottle(__name__)
namepattern = re.compile(r'^[a-zA-Z\d]{1,64}$')
con = pypg.connect(user='postgres', password='password', database='postgres')
cur = con.cursor()


def ins(p):
    if p != [] and '' not in p:
        cur.execute(cqs+"user_name='%s' and user_type='%s' and user_mail='%s' and password='%s'" %
                    (p[0], p[1], p[2], p[4]))
        pct = cur.fetchone()
        pc = 0
        for i in pct:
            pc = i
        qs = "insert into public.registered_users(user_name, user_type, user_mail, date_of_birth, gender, city, phone_no, password) values ('" + \
            p[0]+"','" + p[1] + "','" + p[2]+"',"+p[3] + \
            ",'"+p[4]+"','"+p[5]+"',"+p[6]+",'"+p[7]+"')"
        if pc == 0:
            cur.execute(qs)
            con.commit()
            p = []


def get2(p):
    if p != [] and '' not in p:
        cur.execute(cqs+"user_mail='%s' and password='%s'" % (p[0], p[1]))
        prc = cur.fetchone()
        return prc[0]
    else:
        return -1


def get1(q):
    a = 0
    if q != [] and '' not in q:
        cur.execute(cqs + "user_mail='%s' and password='%s'" % (q[0], q[1]))
        a = cur.fetchone()
        if a == 1:
            cur.execute(
                snt+" from registered_users where user_mail='%s' and password='%s'" % (q[0], q[1]))
            return cur.fetchone()


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
                    cur.execute(cqs + "user_email='{"+data['user_name']+"}' and password='{"+data['password']+"}'")
                    if cur.fetchone()[0] == 1:
                        cur.execute(
                            snt+" from registered_users where user_mail='{"+data['user_name']+"}' and password='{"+data['password'] + "}'")
                        print(dict(cur.fetchall()))
                        response.body = str(
                            {"success": True, "status": True, "message": "Logged In Successfully"})
                    else:
                        response.body = str({"success":False,"status":False,"message":"User Does Not Exist"})
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


@app.post('/signup')
def signup():
    try:
        try:
            data = request.json
        except:
            raise ValueError
        if data is None or data == {}:
            raise ValueError
        try:
            if 'user_name' in data.keys() and 'password' in data.keys() and 'user_type' in data.keys() and 'user_email' in data.keys():
                cur.execute(
                    cqs+"user_name='{"+data['user_name']+"}' and user_type={"+data['user_type']+"} and user_email='{"+data['user_email']+"}' and password='{"+data['password']+"}'")
        except (TypeError, KeyError):
            raise ValueError
    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Content-Type'] = 'application/json'
    return 


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
            if namepattern.match(data['name']) is None:
                raise ValueError
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
