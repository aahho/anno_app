from app import helpers
import datetime

def generate_firebase_config():
	return {
		"apiKey" : helpers.getenv('api_key'),
		"authDomain" : helpers.getenv('auth_domain'),
		"databaseURL" : helpers.getenv('database_url'),
		"projectId" : helpers.getenv('project_id'),
		"storageBucket" : helpers.getenv('storage_bucket'),
		"serviceAccount" : helpers.getenv('service_account')
	}

def user_signup_format(data):
	return {
		"id": str(helpers.generate_uuid()),
		"username" : str(data['username']),
		"display_name" : str(data['display_name']),
		"password" : helpers.hash_password(str(data['password'])),
		"intrests" : data['intrests'],
		"gravatar" : None,
		"is_active" : True, 
		"date_of_birth" :None,
		"created_at" : str(datetime.datetime.now()),
		"updated_at" : str(datetime.datetime.now())
	}

def user_signin_format(data):
	return {
		'username' : str(data['username']),
		'password' : str(data['password'])
	}

def user_notify_format(data):
	return {
		'device_ids' : data['deviceIds'],
		'title' : data['messageTitle'],
		'body' : data['messageBody'],
		'data' : data['data']
	}
