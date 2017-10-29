from g_firebase.apis import FirebaseApi
from g_firebase.helpers import user_signup_format, user_notify_format
from app import helpers

class RequestHandler():

	def __init__(self):
		self.firebase = FirebaseApi()

	def handle_user_signup(self, request):
		data = user_signup_format(request.json)
		new = self.firebase.user_signup(data)
		return 'User Created Successfully'

	def handle_user_sigin(self, request):
		users = self.firebase.get_user(request.json)
		for user in users.each():
			if user.val()['username'] == str(request.json['username']) and helpers.validate_hash_password(request.json['password'], user.val()['password']):
				data = user.val()
				data['idToken'] = self.firebase.signin_with_custom_token()['idToken']
				data['refreshToken'] = self.firebase.signin_with_custom_token()['refreshToken']
				return data
		return False

	def handle_notifying_users(self, request):
		data = user_notify_format(request.json)
		result = self.firebase.notify_users(data)
		return result
