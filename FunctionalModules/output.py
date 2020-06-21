import os
import json
import pymongo as pm
import datetime as dt
import appServer as ap
# import calculate as calc
# key=new Random().nextInt(99999999-10000000)+10000000
T = {}
mc = pm.MongoClient("mongodb://localhost:27017/")
db = mc['db1']
col = db['gene_test_results']
if T != {}:
    w = col.insert_one(T)
    json.dump(T, open(os.path.join(ap.app.root_path, "output", "Result_"+dt.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+"_"+T['Result ID']+".json"), 'w'))
