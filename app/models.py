"""
This is where you define the models of your application.
This may be split into several modules in the same way as views.py.
"""

from app import app, mongodb
# from datetime import date
# from werkzeug.security import generate_password_hash, check_password_hash
# import sys
# from .modules import get_image_size

###########################################################
# class ClassName(db.Model):
# 	__tablename__ = 'tablename'
# 	id = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String)
# 	password = db.Column(db.String)
#
# 	def __init__(self, name, password):
# 		self.name = name
# 		self.password = password
#
# 	def __repr__(self): #return & print
# 		return '<name %r>' % (self.name)
###########################################################

# # authority infromation
# UNKNOWN = -1
# USER = 0
# ADMIN = 10


# class UserMixin(object):
# 	'''
# 	This provides default implementations for the methods that Flask-Login
# 	expects user objects to have.
# 	'''
# 	@property
# 	def is_active(self):
# 		return True

# 	@property
# 	def is_authenticated(self):
# 		return True

# 	@property
# 	def is_anonymous(self):
# 		return False

# 	def get_id(self):
# 		try:
# 			return str(self.id)
# 		except AttributeError:
# 			raise NotImplementedError('No `id` attribute - override `get_id`')

# 	def __eq__(self, other):
# 		'''
# 		Checks the equality of two `UserMixin` objects using `get_id`.
# 		'''
# 		if isinstance(other, UserMixin):
# 			return self.get_id() == other.get_id()
# 		return NotImplemented

# 	def __ne__(self, other):
# 		'''
# 		Checks the inequality of two `UserMixin` objects using `get_id`.
# 		'''
# 		equal = self.__eq__(other)
# 		if equal is NotImplemented:
# 			return NotImplemented
# 		return not equal

# 	if sys.version_info[0] != 2:  # pragma: no cover
# 		# Python 3 implicitly set __hash__ to None if we override __eq__
# 		# We set it back to its default implementation
# 		__hash__ = object.__hash__



# class User(db.Model, UserMixin):
# 	__tablename__ = 'user'
# 	id = db.Column(db.Integer, primary_key = True)
# 	user_id = db.Column(db.String, unique = True)
# 	username = db.Column(db.String, nullable = False)
# 	password_hash = db.Column(db.String, nullable = False)
# 	authority = db.Column(db.Integer)
# 	active = db.Column(db.Boolean, default=True)
	

# 	def __init__(self, user_id, username, password, authority = 'USER', admin_secret_key = None):
# 		self.user_id = user_id
# 		self.username = username
# 		self.set_password(password)
# 		self.password_hash = self.pw_hash
# 		if authority == 'USER':
# 			self.authority = USER
# 			self.active = True
# 		elif authority == 'ADMIN' and admin_secret_key == app.config['ADMIN_SECRET_KEY']:
# 			self.authority = ADMIN
# 			self.active = True
# 		else:
# 			self.authority = UNKNOWN
# 			self.active = False

# 	def set_password(self, password):
# 		self.pw_hash = generate_password_hash(password)

# 	def check_password(self, password):
# 		return check_password_hash(self.password_hash, password)

# 	def get_user_authority(self):
# 		return self.authority

# 	def __repr__(self):
# 		return '<User username %r>' % self.username

# class Menu(db.Model):
# 	__tablename__ = 'menu'
# 	id = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String, nullable = False)
# 	on_click_path = db.Column(db.String)
# 	main_menu = db.Column(db.Boolean)

# 	def __init__(self, name, on_click_path, main_menu = False):
# 		self.name = name
# 		self.on_click_path = on_click_path
# 		self.main_menu = main_menu

# 	def __repr__(self):
# 		return '<Menu (name = %s)>' % (self.name)

# # class SubMenu(db.Model):
# # 	__tablename__ = 'submenu'
# # 	id = db.Column(db.Integer, primary_key = True)
# # 	parent_id  = db.Column(db.Integer, Foreign_key("menu.id"), nullable = False)
# # 	name = db.Column(db.String, nullable = False)
# # 	on_click_path = db.Column(db.String)

# # 	def __init__(self, name, on_click_path):
# # 		self.name = name
# # 		self.on_click_path = on_click_path

# # 	def __repr__(self):
# # 		return '<SubMenu (name = %s)>' % (self.name)


# class Painting(db.Model):
# 	__tablename__ = 'paintings'
# 	paintingID = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String)
# 	path = db.Column(db.String, nullable = False)
# 	size_width = db.Column(db.Integer) # 단위는 px이다.
# 	size_height = db.Column(db.Integer)
# 	upload_date = db.Column(db.Date)
# 	explanation = db.Column(db.String)

# 	def __init__(self, name, path, upload_date = None, explanation = None):
# 		self.name = name
# 		self.path = path
# 		if upload_date is not None:
# 			try:
# 				self.upload_date = date(upload_date[0], upload_date[1] ,upload_date[2])
# 			except Exception as e:
# 				self.upload_date = date.today()
# 				print ('Your upload_date arg is not correct format\nFormat is [year, month, date]')
# 		else:
# 			self.upload_date = date.today()

# 		self.explanation = explanation
# 		self.size_width, self.size_height = get_image_size(app.config['BASE_DIR'] + '/' + self.path) # '/joey/workplace/2016/Python/flask/homepageProject/app/' 

# 	def __repr__(self):
# 		return '<Painting (name = %s)>' % (self.name)

# class Lookbook(db.Model):
# 	__tablename__ = 'lookbook'
# 	paintingID = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String)
# 	path = db.Column(db.String, nullable = False)
# 	size_width = db.Column(db.Integer) # 단위는 px이다.
# 	size_height = db.Column(db.Integer)
# 	upload_date = db.Column(db.Date)
# 	explanation = db.Column(db.String)

# 	def __init__(self, name, path, upload_date = None, explanation = None):
# 		self.name = name
# 		self.path = path
# 		if upload_date is not None:
# 			try:
# 				self.upload_date = date(upload_date[0], upload_date[1] ,upload_date[2])
# 			except Exception as e:
# 				self.upload_date = date.today()
# 				print ('Your upload_date arg is not correct format\nFormat is [year, month, date]')
# 		else:
# 			self.upload_date = date.today()

# 		self.explanation = explanation
# 		self.size_width, self.size_height = get_image_size(app.config['BASE_DIR'] + '/' + self.path) # '/joey/workplace/2016/Python/flask/homepageProject/app/' 

# 	def __repr__(self):
# 		return '<Lookbook (name = %s)>' % (self.name)