import psycopg2 as pgdb
con = pgdb.connect(user='postgres', password='root', database='postgres')
cur = con.cursor()
aid = "select count(*) from public.registered_users where "
ai = "select user_name,user_type"
# "Select * from gene1"
# "Select * from reg where username='"+uname+"' "
# "Select * from category"
# "Select * from gene1 where list='"+id+"'"
# "Select * from gene1"
# "Select * from gened"
# "Select * from gene1"
# "Select * from gene1"
# "Select * from gene1"
# "insert into ghis(uid,gid,gtype,file) values('"+uname+"','"+gid+"','"+ge+"','"+key+".txt"+"')"
# "Select * from gene1 where diseaseid='"+id+"'"
# "Select * from inex where ie='"+ge+"'"
# "select * from ghis where uid='"+uname+"'"
# "Select * from gene1"
# "Select * from bf "
# "Select * from cc "
# "Select * from mf"
# "Select * from id"
# CREATE TABLE `ghis`(`sid`,`uid`,`gid`,`gtype`,`file`)
# CREATE TABLE IF NOT EXISTS `gened`(`id` varchar(222) DEFAULT NULL,`name` varchar(2222) DEFAULT NULL,`geneid` varchar(2222) DEFAULT NULL,`ie` varchar(2222) DEFAULT NULL,`sympt` varchar(22222) DEFAULT NULL,`prec` varchar(2222) DEFAULT NULL,`ppi` varchar(1000) DEFAULT NULL)
def ins(p):
    if p != [] and '' not in p:
        Qy = aid+"user_name='%s' and user_type='%s' and user_mail='%s' and gender='%s' and city='%s' and password='%s'" % (
            p[0], p[1], p[2], p[4], p[5], p[7])
        cur.execute(Qy)
        pct = cur.fetchone()
        pc = 0
        for i in pct:
            pc = i
        qs = "insert into public.registered_users(user_name, user_type, user_mail, date_of_birth, gender, city, phone_no, password) values ('" + \
            p[0]+"','" + p[1] + "','" + p[2]+"','" + \
            p[3]+"','"+p[4]+"','" + p[5] + "'," + p[6]+",'" + p[7]+"')"
        if pc == 0:
            cur.execute(qs)
            con.commit()
            p = []
            return True
        else:
            return False
    elif p==[]:
        return True
    else:
        return False


def get(x):
    if x != [] and '' not in x:
        cur.execute(aid+"user_mail='%s' and password='%s'" % (x[0], x[1]))
        return cur.fetchone()[0]


def get1(x):
    if x != [] and '' not in x:
        cur.execute(
            ai+",gender,city from public.registered_users where user_mail='%s' and password='%s'" % (x[0], x[1]))
        return cur.fetchone()
