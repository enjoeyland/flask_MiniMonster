# from flask.ext.wtf import Form 
# from wtforms import TextField, PasswordField, validators
# from wtforms.validators import Required
# from .models import User

# class LoginForm(Form):
# 	user_id = TextField('User Id', validators = [Required()], render_kw = {"placeholder" : "User Id", "class" : "ej-loginInput"})
# 	password = PasswordField('Password', validators = [Required()], render_kw = {"placeholder" : "Password", "class" : "ej-loginInput"})

# 	def __init__(self, *args, **kwargs):
# 		Form.__init__(self, *args, **kwargs)
# 		self.user = None

# 	def validate(self):
# 		rv = Form.validate(self)
# 		if not rv:
# 			return False

# 		user = User.query.filter_by(user_id = self.user_id.data).first()
# 		if user is None:
# 			self.id.errors.append('Unknown id')
# 			return False

# 		if not user.check_password(self.password.data):
# 			self.password.errors.append('Invalid password')
# 			return False

# 		self.user = user
# 		return True

# 	def get_username(self):
# 		if self.validate():
# 			return self.user.username
