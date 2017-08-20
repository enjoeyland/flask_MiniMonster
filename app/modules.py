from flask import render_template, request, url_for
from app import mongodb,user_list_collection
from bson.objectid import ObjectId
from datetime import datetime, timedelta
# from PIL import Image
# from flask.ext.login import current_user, login_required, current_app
# from functools import wraps



def convert_string_to_ObjectId(post_id):
    return ObjectId(post_id)

class Validated_User():
	def __init__(self, post_id):
		# if type(post_id) is str and type(post_id) is not ObjectId:
		# 	self.post_id = convert_string_to_ObjectId(post_id)
		# elif type(post_id) is ObjectId:
		# 	self.post_id = post_id
		self.post_id = post_id
		self.user_collection = mongodb[self.post_id]
		user_data = user_list_collection.find_one({"user_id": self.post_id})
		try:
			self.user_name = user_data["user_name"]
		except Exception as e:
			print (e)
			self.user_name = "guest"
		try:
			self.profile_img = user_data["profile_img"]
		except Exception as e:
			print (e)
			self.profile_img = "../static/default/images/user.png"
	def get_user_name(self):
		return self.user_name
	def get_profile_img(self):
		return self.profile_img
	def get_recent_one_week_exercise_data(self):
		WEEK = 7
		NO_DATA = 0

		recent_one_week_exercise_data = []
		for item in range(WEEK):
			start = (datetime.now() - timedelta(days = WEEK-item)).replace(hour=0, minute=0, second=0)
			end = (datetime.now() - timedelta(days = WEEK-1-item)).replace(hour=0, minute=0, second=0)

			# result = self.user_collection.find_one({'date': {'$gte': start, '$lt': end}})

			result_list = list(self.user_collection.find({'date': {'$gte': start, '$lt': end}}))
			if len(result_list) == NO_DATA:
				result_list = [{"date" : start, "count" : 0, "time" : 0, "weight" : 0 }]	
				# print (result_list)
			recent_one_week_exercise_data.append(result_list)
		return recent_one_week_exercise_data

	def get_benchPress_oneday_data(self, past = 0):
		start = (datetime.now() - timedelta(days = 1 + past)).replace(hour=0, minute=0, second=0)
		end = (datetime.now() - timedelta(days =  past)).replace(hour=0, minute=0, second=0)
		result_list = list(self.user_collection.find({'date': {'$gte': start, '$lt': end},"exercise_event":"benchpress"}))
		return result_list


def cal_for_benchpress(weight, count, time):
	calorie_per_once_at10kg = 1
	calorie = int(weight / 10 * calorie_per_once_at10kg *count)
	return calorie

def getBenchPressCalorie(day_data):
	calorie = 0

	for item in day_data:
		weight = item["weight"]
		count = item["count"]
		time = item["time"]
		calorie += cal_for_benchpress(weight,count,time)
	return calorie

def getBiggestCalorie(day_data, type = "benchpress"):
	biggest = {"calorie":0, "count":0, "weight":0, "time" : 0}
	if type == "benchpress":
		for item in day_data:
			weight = item["weight"]
			count = item["count"]
			time = item["time"]
			calorie = cal_for_benchpress(weight,count,time)
			if biggest["calorie"] < cal_for_benchpress(weight,count,time):
				biggest = item
				biggest["calorie"] = calorie
		print (biggest)
		return biggest
	return 0

def getPercentOfIncreasement(first, last):
	try:
		result_percent = int(100 * first / last - 100)
	except Exception as e:
		result_percent = 0
	return result_percent
# def default_render_template(template, path, login_hidden = False,*arg, **kwargs):
# 	menu_items = get_menu()
# 	menu_main = []
# 	menu_hidden = []
# 	menubar_thispage = None
# 	for name, on_click_path, main_menu_TF in menu_items:
# 		if main_menu_TF == True :
# 			menu_main.append([name, on_click_path])
# 		else:
# 			menu_hidden.append([name, on_click_path])

# 		if on_click_path == path:
# 			menubar_thispage = name

# 	if current_user.is_authenticated:
# 		logged_in = True
# 	else:
# 		logged_in = False

# 	if path == '/login':
# 		return render_template(template, main_menu = menu_main, hidden_menu = menu_hidden, logged_in = logged_in, login_hidden = True, menubar_thispage = menubar_thispage, *arg, **kwargs)

# 	return render_template(template, main_menu = menu_main, hidden_menu = menu_hidden, logged_in = logged_in, login_hidden = login_hidden, menubar_thispage = menubar_thispage, *arg, **kwargs)	

# def redirect_url(default='index'):
# 	return request.args.get('next') or request.referrer or url_for(default)


# def authority_required(func):
# 	"""
# 		@app.route('/')
# 		@authority_required
# 		def index():
# 			return base_authority, "hi"
# 	base_authority is int type
# 	"""
# 	@login_required
# 	@wraps(func)
# 	def decorated_view(*args, **kwargs):
# 		if current_user.get_user_authority() >= func(*args, **kwargs)[0]:
# 			return func(*args, **kwargs)[1]
# 		return current_app.login_manager.unauthorized()

# 	return decorated_view

# # def get_image_size(filepath):
# # 	im = Image.open(filepath)
# # 	width, height = im.size
# # 	return width, height

# # def get_image_to_display_painting(number_of_display):
# # 	result = db.session.execute(
# # 		"""SELECT name, path 
# # 		FROM paintings 
# # 		ORDER BY upload_date DESC
# # 		limit """ + str(number_of_display))
# # 	images = []
# # 	for row in result:
# # 		images.append(row)

# # 	return images

# # def get_image_to_display_lookbook(number_of_display):
# # 	result = db.session.execute(
# # 		"""SELECT name, path 
# # 		FROM lookbook 
# # 		ORDER BY upload_date DESC
# # 		limit """ + str(number_of_display))
# # 	images = []
# # 	for row in result:
# # 		images.append(row)

# # 	return images

# def get_menu():
# 	result = db.session.execute(
# 		"""SELECT name, on_click_path, main_menu
# 		FROM menu""")
# 	menu_items = []
# 	for row in result:
# 		menu_items.append(row)

# 	return menu_items