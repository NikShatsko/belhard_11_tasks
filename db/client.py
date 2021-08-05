from pymongo import MongoClient
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

client1 = MongoClient(config["connection"]["host"], int(config["connection"]["port"]))
new_users = client1.new_users
users = new_users.users
db_list = client1.list_database_names()

if "users" in db_list:
    print("Nice")
