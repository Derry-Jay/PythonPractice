import psycopg2 as pypg
cqs = "select count(*) from public.registered_users where "
snt = "select user_name,user_type"
con = pypg.connect(user='postgres', password='root', database='postgres')
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


def get(p):
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
            cur.execute(snt+" from registered_users where user_mail='%s' and password='%s'" % (q[0], q[1]))
            return cur.fetchone()
