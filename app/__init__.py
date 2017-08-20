"""
This file initializes your application
and brings together all of the various components.
"""

import os
import sys

from flask import Flask
from flask.ext.login import LoginManager
from pymongo import MongoClient




app = Flask(__name__) # instance_relative_config = True
app.config.from_object('config.default')
# app.config.from_pyfile('config.py') -> UnicodeDecodeError: 'cp949' codec can't decode byte 0xe2 in position 57: illegal multibyte sequence

# --MongoDB setting--
mongoClient = MongoClient(app.config["MONGO_DB_IP"], app.config["MONGO_DB_PORT"])
mongodb = mongoClient[ app.config["MONGO_DATABASE"] ]
user_list_collection = mongodb[ app.config["MONGO_COLLECTION_USER_LIST"] ]

# # --MongoDB insert--
# import datetime
# post = {
# 	"author": "Mike",
# 	"text": "My first blog post!",
# 	"tags": ["mongodb", "python", "pymongo"],
# 	"date": datetime.datetime.utcnow()
# }
# post_id = posts.insert_one(post).inserted_id

# new_posts = [
# 	{
# 		"author": "Mike",
# 		"text": "Another post!",
# 		"tags": ["bulk", "insert"],
# 		"date": datetime.datetime(2009, 11, 12, 11, 14)
# 	},
# 	{
# 		"author": "Eliot",
# 		"title": "MongoDB is fun",
# 		"text": "and pretty easy too!",
# 		"date": datetime.datetime(2009, 11, 10, 10, 45)
# 	}
# ]
# result = posts.insert_many(new_posts)
# >>> result.inserted_ids
# [ObjectId('...'), ObjectId('...')]

# # --MongoDB select--
# posts.find_one({"author": "Mike"})
# posts.find_one({"_id": post_id})

# # --MongoDB string to ObjectId--
# from bson.objectid import ObjectId

# # The web framework gets post_id from the URL and passes it as a string
# def get(post_id):
#     # Convert from string to ObjectId:
#     document = client.db.collection.find_one({'_id': ObjectId(post_id)})
#     return document



# def install_secret_key(app, filename = 'secret_key'):
# 	"""Configure the SECRET_KEY from a file
# 	in the instance directory.
#
# 	If the file does not exist, print instructions
# 	to create it from a shell with a random key,
# 	then exit.
# 	"""
# 	filename = os.path.join(app.instance_path, filename)
#
# 	try:
# 		app.config['SECRET_KEY'] = open(filename, 'rb').read()
# 	except IOError:
# 		print('Error: No secret key. Create it with:')
# 		full_path = os.path.dirname(filename)
#
# 		if not os.path.isdir(full_path):
# 			print('mkdir -p {filename}'.format(filename = full_path))
#
# 		print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
# 		sys.exit(1)
#
# if not app.config['DEBUG']:
# 	install_secret_key(app)

login_manager = LoginManager()
login_manager.init_app(app)

# from app import views


# from app.users.views import mod as usersModule
# app.register_blueprint(usersModule)

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)