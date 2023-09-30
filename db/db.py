from pymongo import MongoClient

client = MongoClient("mongodb://admin:juegoroblox123@mongodb:27017/CervezaSergio?authSource=admin")
client = client["CervezaSergio"]
