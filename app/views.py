"""
This is where the routes are defined.
It may be split into a package of its own (app/views/)
with related views grouped together into modules.
"""

from flask import render_template, redirect, url_for, abort, request, g, json
from app import app,  login_manager, mongodb
# from flask.ext.login import login_user, logout_user, current_user, login_required
from .models import *
from .modules import *
from .form import *
# from sqlalchemy import text


# @app.before_request
# def before_request():
# 	g.user = current_user

@app.route('/table', methods = ['GET', 'POST'])
def table():
	return render_template("tableV01.html")

@app.route('/', methods = ['GET', 'POST'])
def index():
	# rule = request.url_rule
	# user = Validated_User("582c37137bfc3108b0bf0229")
	user = Validated_User("1")

	one_week_data = user.get_recent_one_week_exercise_data()
	user_profile_data = {"name" : user.get_user_name(), "profile_img" : user.get_profile_img()}
	request_user_name = request.args.get("username")
	if request_user_name != None:
		user_profile_data["name"] = request_user_name

	today_benchpress_top_data = getBiggestCalorie(user.get_benchPress_oneday_data())
	yesterday_benchpress_top_data = getBiggestCalorie(user.get_benchPress_oneday_data(past = 1))

	test_topPage_increasement_list = [
		{
			"topic_title": "Bench Press",
			"topic_count" : str(today_benchpress_top_data["count"]) + "개/" + str(today_benchpress_top_data["weight"]) + "kg",
			"increase_percent" : getPercentOfIncreasement(today_benchpress_top_data["calorie"],yesterday_benchpress_top_data["calorie"])
		},
		{
			"topic_title": "Squart",
			"topic_count" : "52",
			"increase_percent" : -19
		},
		{
			"topic_title": "Dead Lift",
			"topic_count" : "12/40kg",
			"increase_percent" : 2
		},
		{
			"topic_title": "Running",
			"topic_count" : "32km",
			"increase_percent" : -12
		},
		{
			"topic_title": "Total Caiories",
			"topic_count" : "4201kal",
			"increase_percent" : 34
		},
		{
			"topic_title": "Ranking",
			"topic_count" : "12,230",
			"increase_percent" : 28
		},
	]

	test_line_graph = {
		"title" : "Exercies Count Graph",
		"sub_title" : "",
		"topic" : {
			"calorie_data_one_week" : one_week_data,
			"exercise_time_one_week" : one_week_data
		}
	}

	test_progressbar = {
		"title" : "Calroise From Exercise",
		"total" : 4201,
		"unit" : "kal",
		"main" : [
			{
				"topic_title" : "Bench Press",
				"topic_num" : getBenchPressCalorie(user.get_benchPress_oneday_data()),
			},
			{
				"topic_title" : "Dead Lift",
				"topic_num" : 1159,
			},
			{
				"topic_title" : "Running",
				"topic_num" : 839,
			},
			{
				"topic_title" : "Squart",
				"topic_num" : 232,
			},
			{
				"topic_title" : "Walking",
				"topic_num" : 102,
			}
		]
	}

	test_doughnut_chart = {
		"title" : "Exercise Part",
		"th" : {
			"topic" : "Body Part",
			"value" : "Progress"
		},
		"main" : [
			{
				"topic_title" :"가슴",
				"topic_percent" : 28,
				"color" : "green"
			},
			{
				"topic_title" :"이두",
				"topic_percent" : 16,
				"color" : "blue"
			},
			{
				"topic_title" :"어꺠",
				"topic_percent" : 20,
				"color" : "red"
			},
			{
				"topic_title" :"허벅지",
				"topic_percent" : 18,
				"color" : "purple"
			},
			{
				"topic_title" :"복부",
				"topic_percent" : 8,
				"color" : "aero"
			}
		]
	}


	
	return render_template(
		"userV05.html",
		title = "Android User Page",
		company_name = "Mini Monster",
		user_profile_data = user_profile_data,
		topPage_increasement_list = test_topPage_increasement_list,
		line_graph = test_line_graph,
		progressbar = test_progressbar,
		doughnut_chart = test_doughnut_chart,
		test = "hi"
	)

@app.route('/NFC', methods = ['GET', 'POST'])
def NFC():
	# rule = request.url_rule
	# user = Validated_User("582c37137bfc3108b0bf0229")
	user = Validated_User("2")

	one_week_data = user.get_recent_one_week_exercise_data()
	user_profile_data = {"name" : user.get_user_name(), "profile_img" : user.get_profile_img()}
	request_user_name = request.args.get("username")
	if request_user_name != None:
		user_profile_data["name"] = request_user_name

	today_benchpress_top_data = getBiggestCalorie(user.get_benchPress_oneday_data())
	yesterday_benchpress_top_data = getBiggestCalorie(user.get_benchPress_oneday_data(past = 1))

	test_topPage_increasement_list = [
		{
			"topic_title": "Bench Press",
			"topic_count" : str(today_benchpress_top_data["count"]) + "개/" + str(today_benchpress_top_data["weight"]) + "kg",
			"increase_percent" : getPercentOfIncreasement(today_benchpress_top_data["calorie"],yesterday_benchpress_top_data["calorie"])
		},
		{
			"topic_title": "Squart",
			"topic_count" : "52",
			"increase_percent" : -19
		},
		{
			"topic_title": "Dead Lift",
			"topic_count" : "12/40kg",
			"increase_percent" : 2
		},
		{
			"topic_title": "Running",
			"topic_count" : "32km",
			"increase_percent" : -12
		},
		{
			"topic_title": "Total Caiories",
			"topic_count" : "4201kal",
			"increase_percent" : 34
		},
		{
			"topic_title": "Ranking",
			"topic_count" : "12,230",
			"increase_percent" : 28
		},
	]

	test_line_graph = {
		"title" : "Exercies Count Graph",
		"sub_title" : "",
		"topic" : {
			"calorie_data_one_week" : one_week_data,
			"exercise_time_one_week" : one_week_data
		}
	}

	test_progressbar = {
		"title" : "Calroise From Exercise",
		"total" : 4201,
		"unit" : "kal",
		"main" : [
			{
				"topic_title" : "Bench Press",
				"topic_num" : getBenchPressCalorie(user.get_benchPress_oneday_data()),
			},
			{
				"topic_title" : "Dead Lift",
				"topic_num" : 1159,
			},
			{
				"topic_title" : "Running",
				"topic_num" : 839,
			},
			{
				"topic_title" : "Squart",
				"topic_num" : 232,
			},
			{
				"topic_title" : "Walking",
				"topic_num" : 102,
			}
		]
	}

	test_doughnut_chart = {
		"title" : "Exercise Part",
		"th" : {
			"topic" : "Body Part",
			"value" : "Progress"
		},
		"main" : [
			{
				"topic_title" :"가슴",
				"topic_percent" : 28,
				"color" : "green"
			},
			{
				"topic_title" :"이두",
				"topic_percent" : 16,
				"color" : "blue"
			},
			{
				"topic_title" :"어꺠",
				"topic_percent" : 20,
				"color" : "red"
			},
			{
				"topic_title" :"허벅지",
				"topic_percent" : 18,
				"color" : "purple"
			},
			{
				"topic_title" :"복부",
				"topic_percent" : 8,
				"color" : "aero"
			}
		]
	}


	
	return render_template(
		"userV05.html",
		title = "NGC User Page",
		company_name = "Mini Monster",
		user_profile_data = user_profile_data,
		topPage_increasement_list = test_topPage_increasement_list,
		line_graph = test_line_graph,
		progressbar = test_progressbar,
		doughnut_chart = test_doughnut_chart,
		test = "hi"
	)
