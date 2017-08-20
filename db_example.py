from app import app, mongodb, user_list_collection
from app.models import *
import datetime

# user_list_data = [
# 	{
# 		"user_name": "Mike",
# 		"user_login_id" : "mike",
# 		"user_login_pw" : "1111",
# 		# "profile_img": "",
# 		"registration_date": datetime.datetime.today()
# 	},
# 	{
# 		"user_name": "Jenny",
# 		"user_login_id" : "jenny",
# 		"user_login_pw" : "1111",
# 		# "profile_img": "",
# 		"registration_date": datetime.datetime.today()
# 	},
# 	{
# 		"user_name": "Peter",
# 		"user_login_id" : "peter",
# 		"user_login_pw" : "1111",
# 		# "profile_img": "",
# 		"registration_date": datetime.datetime.today()
# 	},
# 	{
# 		"user_name": "Joey Min",
# 		"user_login_id" : "enjoey",
# 		"user_login_pw" : "1111",
# 		"profile_img": "../static/default/images/img.jpg",
# 		"registration_date": datetime.datetime.today()
# 	}
# ]
# user_list_result = user_list_collection.insert_many(user_list_data)

# joey_user_id = user_list_result.inserted_ids[-1]
collection = mongodb["1"]
a = 17
joey_exercise_data = [
	{
		"exercise_event" : "benchpress",
		"count" : 30,
		"weight" : 20,
		"time" : 20,
		"date": datetime.datetime(2016,11,a-7)
	},
		{
		"exercise_event" : "benchpress",
		"count" : 18,
		"weight" : 20,
		"time" : 18,
		"date": datetime.datetime(2016,11,a-6)
	},
		{
		"exercise_event" : "benchpress",
		"count" : 25,
		"weight" : 50,
		"time" : 10,
		"date": datetime.datetime(2016,11,a-5)
	},
		{
		"exercise_event" : "benchpress",
		"count" : 10,
		"weight" : 20,
		"time" : 20,
		"date": datetime.datetime(2016,11,a-4)
	},
		{
		"exercise_event" : "benchpress",
		"count" : 27,
		"weight" : 30,
		"time" : 8,
		"date": datetime.datetime(2016,11,a-3)
	},
		{
		"exercise_event" : "benchpress",
		"count" : 17,
		"weight" : 20,
		"time" : 13,
		"date": datetime.datetime(2016,11,a-2)
	},
		{
		"exercise_event" : "benchpress",
		"count" : 7,
		"weight" : 10,
		"time" : 8,
		"date": datetime.datetime(2016,11,a-1)
	},
	{
		"exercise_event" : "benchpress",
		"count" : 1,
		"weight" : 10,
		"time" : 1,
		"date": datetime.datetime(2016,11,a)
	}
]
exercise_result = collection.insert_many(joey_exercise_data)
