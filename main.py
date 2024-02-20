from datetime import datetime
import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from secrets_tuit import ACCESS_TOKEN, CONSUMER_KEY, ACCESS_TOKEN_SECRET, SECRET_KEY, BEARER_TOKEN
import tweepy


uri = "mongodb+srv://johnsonmacedo:edb0IS6wDZ4CbG1S@cluster0.uqlh08o.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

db = client.test 
collection = db.test_collection
#print(db.test_collection) """

post = {
    "author": "José",
    "text": "First blog of Jose.",
    "tags": ["blog", "First", "pymongo"],
    "date": datetime.utcnow()
}

posts = db.posts
#post_id = posts.insert_one(post).inserted_id
#print(post_id)

#pprint.pprint(db.posts.find_one())
print("\nColeção Posts:\n")
for post in posts.find().sort('date'):
    pprint.pprint(post)
    print('\n')

print(f'Quantidade de documentos: {posts.count_documents({})}\n')

print("\nMinhas coleções do MongoDB:\n")
collections = db.list_collection_names()
for collection in collections:
    print(collection)
#result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique = True)
#print(sorted(list(db.profiles.index_information()))) """ 
BRAZIL_WOE_ID = 23424768

""" auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth) """

client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = 'covid -is:retweet'
resultado = client.search_recent_tweets(query=query, max_results=100)

quant = client.get_all_tweets_count(query=query)
print(quant)