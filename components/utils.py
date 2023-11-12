# connect to MongoDB
from pymongo import MongoClient
import os


def connectMongo():
    # variables come from .env file
    mongoHost = os.getenv('MONGO_HOST', default='localhost')
    mongoPort = os.getenv('MONGO_PORT', default='27017')
    mongoUser = os.getenv('MONGO_USER')
    mongoPass = os.getenv('MONGO_PWD')
    mongoAuthSrc = os.getenv('MONGO_AUTH_SRC', default='admin')
    mongoDb = os.getenv('MONGO_DB', default='oeb-research-software')
    mongoCollection = os.getenv('MONGO_COLLECTION', default='githubMiner')
    mongoLogCollection = os.getenv('MONGO_LOG_COLLECTION', default='githubMinerLog')

    # Connect to MongoDB
    mongoClient = MongoClient(
        host=mongoHost,
        port=int(mongoPort),
        username=mongoUser,
        password=mongoPass,
        authSource=mongoAuthSrc,
    )
    db = mongoClient[mongoDb]
    collection = db[mongoCollection]
    logCollection = db[mongoLogCollection]

    return collection, logCollection 
