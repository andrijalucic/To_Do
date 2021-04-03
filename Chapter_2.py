# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:08:43 2021

@author: Andrija
"""


# to do 1
import pymongo
client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection2 = mydb["CRUD_exercise"]

import json

with open('data.json', 'r') as fp:
    test= json.load(fp)

new_post2 = test

collection2.insert_one(new_post2)


#to do 2

import tqdm


client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection2 = mydb["CRUD_exercise"]

for i in tqdm.tqdm(range(3)):
    post = {"x":1}
    collection2.insert_one(post)
    
collection2.delete_one({'x': 1}) # the first one 

# to do 3

client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection = mydb["example"]
with open('data_nxml.json', 'r') as fp:
    result= json.load(fp)
new_post3 = result
collection.insert_one(new_post3)

# to do 4

doc=collection.find({'authors': { '$exists': True}})

for d in doc:
    print(d)


# to do 5

post4 = {"x" : 4}
collection.insert_one(post4)
collection.update_many({'x': 4}, {'$set': {'x': 1}})

# to do 6

collection.find_one_and_update({'author': "Mike"}, {'$set': {'author': "real_Mike"}})    

# to do 7

collection.delete_one({'author': "real_Mike"})


# to do 8

import tqdm
import pymongo
import numpy as np

client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection3 = mydb["benchmark_2"]

# Note that if you use insert_one, this operation will take more than an hour
list_of_insertion = []
for i in tqdm.tqdm(range(1,1000000,2)):
    post = {"user_id":i,
           "random_value":np.random.randint(1, 500000)}
    list_of_insertion.append(post)
    if i % 15000 == 0:
        collection3.insert_many(list_of_insertion)
        list_of_insertion = []
collection3.insert_many(list_of_insertion)


# to do 9

client = pymongo.MongoClient('localhost', 27017)
mydb = client["to_do"]
collection4 = mydb["to_do"]
random = {"football" : "result"}
collection4.insert_one(random)

# to do 10 
# the main differnce between inner and outer joint is in the fact that for an inner join we will take only the rows present in both tables, 
# on the other side for outer join we will use all rows from table we want, if we use right join, for exemple, we will take all rows from right table 

client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection = mydb["benchmark"]

pipeline = [{'$lookup': 
                {'from' : 'benchmark_2',
                 'localField' : 'user_id',
                 'foreignField' : 'user_id',
                 'as' : 'cellmodels'}},
            {'$unwind': '$cellmodels'},
            {'$project': 
                {'user_id':1, 'cellmodels.user_id':1, 'cellmodels.random_value':1}} 
             ]
    
documents = collection.aggregate(pipeline)
for i in range(20):
    print(next(documents))

pipeline2 = [{'$lookup': 
                {'from' : 'benchmark_2',
                 'localField' : ('user_id'),
                 'foreignField' : ('user_id'),
                 'as' : 'cellmodels'}},
            {'$unwind': '$cellmodels'},
            {'$project': 
                {'user_id':1,'user_name':1, 'cellmodels.user_id':1, 'cellmodels.random_value':1}} 
             ]

documents2 = collection.aggregate(pipeline2)
for i in range(20):
    print(next(documents2))
    
    
pipeline3 = [{'$lookup': 
                {'from' : 'benchmark_2',
                 'localField' : ('user_id'),
                 'foreignField' : ('user_id'),
                 'as' : 'cellmodels'}},
            {'$unwind': '$cellmodels'},
            {'$project': 
                {'user_id':1,'user_name':1, 'cellmodels.user_id':1}} 
             ]

documents3 = collection.aggregate(pipeline3)
for i in range(20):
    print(next(documents3))
    
    
pipeline4 = [{'$lookup': 
                {'from' : 'benchmark_2',
                 'localField' : ('user_id'),
                 'foreignField' : ('user_id'),
                 'as' : 'cellmodels'}},
            {'$unwind': '$cellmodels'},
            {'$project': 
                {'user_id':1,'user_name':1, 'cellmodels.random_value':1}} 
             ]

documents4 = collection.aggregate(pipeline4)
for i in range(20):
    print(next(documents4))
    
    

# to do 11

from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
import tqdm


# Important for TODO
URL = 'http://export.arxiv.org/oai2?verb=ListIdentifiers&set=cs,math,econ&from=2018-11-01&until=2020-12-01'
registry = MetadataRegistry()
registry.registerReader('oai_dc', oai_dc_reader)
client = Client(URL, registry)

arxiv_txt = open('D:/arxiv.txt', 'a+')

for record in tqdm.tqdm(client.listRecords(metadataPrefix='oai_dc')):
    try:
        id_ = record[1].getMap()["identifier"][0].split("/")[-1]
        arxiv_txt.write(id_ + "\n")
    except:
        pass
arxiv_txt.close()
import requests
import feedparser
import tqdm
import time
import pymongo


client = pymongo.MongoClient('localhost',27017)
mydb = client["arxiv"] 
collection = mydb["api"]


with open("D:/arxiv.txt","r") as lines:
    ids = lines.read().split("\n")[0:-2]

results = {}
ids_query = []
iteration = 1
ids[1:200]
for id_ in tqdm.tqdm(ids[0:201]):
    if iteration % 100 != 0:
        iteration += 1
        ids_query.append(id_)
    else:
        ids_query = ",".join(ids_query)
        response = requests.get('http://export.arxiv.org/api/query?id_list={}&max_results=200'.format(ids_query))
        feed = feedparser.parse(response.content)
        list_of_insertion = []
        for entry in feed.entries:
            list_of_insertion.append(dict(entry))
        collection.insert_many(list_of_insertion)
        ids_query = []
        iteration = 1
        time.sleep(1/3)
        
mydoc = collection.find().sort("author")
for x in mydoc:
    print(x)

collection2 = mydb["api_sort"]
collection2.insert_one(x)

myquery = { "author": { "$regex": "^S" } }
a=collection.find(myquery)
for y in a :
    print(y)

myquery2 = { "updated_parsed": { "$gt": 2010 } }
b=collection.find(myquery2)
for v in b :
    print(v)
    
# to do 12

import pymongo
import tqdm
import numpy as np
client = pymongo.MongoClient("mongodb+srv://andrija:<password>@exemple.d1mrb.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
mydb = client["sample_airbnb"]
collection = mydb["listingsAndReviews"]


list_of_insertion = []
for i in tqdm.tqdm(range(1,1000000,2)):
    post = {"user_id":i,
           "random_value":np.random.randint(1, 500000)}
    list_of_insertion.append(post)
    if i % 15000 == 0:
        collection.insert_many(list_of_insertion)
        list_of_insertion = []
collection.insert_many(list_of_insertion)

docs = collection.find()
next(docs)

# to do 13
import urllib
import PIL
from matplotlib import pyplot
import pymongo
url = "https://raw.githubusercontent.com/master-ds2e/NoSQL/master/data/FSEG.jpg"
urllib.request.urlretrieve(url, "FSEG.jpg")

img = PIL.Image.open("FSEG.jpg")
img.show()
pyplot.imshow(img)
pyplot.show()

import numpy as np
from bson.binary import Binary
import pickle


data = np.asarray(img)
print(data.shape)
post = {}
post['image'] = Binary( pickle.dumps( data, protocol=2) ) 

client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial_special_data"]
collection = mydb["image"]
collection.insert_one(post)


docs = collection.find()
doc =  pickle.loads(next(docs)["image"])
print(doc.shape,type(doc))
image = PIL.Image.fromarray(doc)
pyplot.imshow(image)
pyplot.show()

# to do 14

import pandas as pd
import numpy as np
import pymongo
import json
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection = mydb["data_frame"]

dfData = json.dumps(df2.to_dict('records'))
savaData = {'_id': 'a8e42ed79f9dae1cefe8781760231ec0', 'df': dfData}
res = collection.insert_one(savaData)

# load data frame data back from mongodb
data = collection.find_one({'_id': 'a8e42ed79f9dae1cefe8781760231ec0'}).get('df')
dfData = json.loads(data)
df = pd.DataFrame.from_dict(dfData)

#to do 15

import json
import pymongo
import pandas as pd
import csv
client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection2 = mydb["movie"]


tsv_data = []
with open("D:\movies_review.tsv", 'r') as tsv_in:
    tsv_reader = csv.reader(tsv_in, delimiter='\t')

    tsv_labels = tsv_reader.__next__()
   
    for record in tsv_reader:
        tsv_data.append(record)



df = pd.DataFrame(tsv_data)
result = df.to_json(orient="split")
parsed = json.loads(result)

collection2.insert_one(parsed) 
# not finished

# to do 16

import requests
from io import BytesIO
from scipy.io.wavfile import read
import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client["audio_db"]
collection = mydb["audio_file"]

url ="http://soundbible.com/grab.php?id=2219&type=wav"
response = requests.get(url)
rate, data = read(BytesIO(response.content))

collection.insert_one({"rate" : rate,
                       "data" : data.tolist(),
                       })