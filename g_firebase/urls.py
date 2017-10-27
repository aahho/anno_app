from flask import Blueprint, request
from g_firebase import views

firebase = Blueprint('firebase', __name__, url_prefix='/anno')

@firebase.route('', methods=['GET'])
def get():
	return 'Working'

@firebase.route('/signup', methods=['POST'])
def signup():
	result = views.signup(request)
	return result

@firebase.route('/signin', methods=['POST'])
def legacy():
	result = views.signin(request)
	return result

@firebase.route('/user/notify', methods=['POST'])
def send_notification():
	result = views.notify_users(request)
	return result