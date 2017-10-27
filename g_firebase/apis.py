from g_firebase.helpers import generate_firebase_config
from app.helpers import generate_uuid, getenv
import pyrebase, json

class FirebaseApi():

	def __init__(self):
		self.config = generate_firebase_config()
		self.firebase = pyrebase.initialize_app(self.config)
		self.auth = self.firebase.auth()
		self.db = self.firebase.database()

	def create_custom_token(self):
		return self.auth.create_custom_token(str(generate_uuid()))

	def signin_with_custom_token(self):
		return self.auth.sign_in_with_custom_token(self.create_custom_token())

	def user_signup(self, data):
		return self.db.child("/chat/users").push(data, self.signin_with_custom_token()['idToken'])

	def get_user(self, data):
		return self.db.child("/chat/users").get(self.signin_with_custom_token()['idToken'])

	def notify_users(self, data):
		from pyfcm import FCMNotification
		push_service = FCMNotification(api_key=getenv('server_key'))
		result = push_service.notify_multiple_devices(registration_ids = data['device_ids'], message_title = data['title'], message_body = data['body'], data_message = data['data'])
		return result
