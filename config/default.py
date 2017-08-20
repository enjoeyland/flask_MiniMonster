"""
This file contains most of the configuration variables that your app needs.

Default values, to be used for all environments or overridden by individual environments.
An example might be setting DEBUG = False in config/default.py and DEBUG = True in config/development.py.
"""

# Statement for enabling the development environment
DEBUG = True


# Define the application directory
import os
BASE_DIR_WIN = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\app\\'))
if BASE_DIR_WIN.find('\\') != -1:
	BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../app/'))
else:
	BASE_DIR = BASE_DIR_WIN
APP_STATIC = BASE_DIR + "/static"

# MongoDB config
MONGO_DB_IP = "localhost"
MONGO_DB_PORT = 27017 
MONGO_DATABASE = "Embedded_Software_Contest_2016"
MONGO_COLLECTION_USER_LIST = "user_list"


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
# // THREADS_PER_PAGE = 2


# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True
# WTF_CSRF_ENABLED = True


# Use a secure, unique and absolutely secret key for
# signing the data.
# // CSRF_SESSION_KEY = "secret"


# Secret key for signing cookies
SECRET_KEY = "VjB[W<b/2I&?yS,ld|i0R[l@J{NV:.YlU$1:c1V&qQnN}NMWRGY*Uc"
ADMIN_SECRET_KEY = "ZS8ySWEmaWVfWT9UZHlTLHJzbWxkfGluMFJbbGVAS2M"




########################################################################################
# import os
#
# class Config(object):
# 	DEBUG = False
# 	TESTING = False
# 	CSRF_ENABLED = True
# 	SECRET_KEY = 'this-really-needs-to-be-changed'
# 	# // SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#
# class ProductionConfig(Config):
# 	DEBUG = False
#
# class StagingConfig(Config):
# 	DEVELOPMENT = True
# 	DEBUG = True
#
# class DevelopmentConfig(Config):
# 	DEVELOPMENT = True
# 	DEBUG = True
#
# class TestingConfig(Config):
# 	TESTING = True