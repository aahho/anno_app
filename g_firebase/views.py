from g_firebase.handler import RequestHandler
from g_firebase import transformers
from app import response

def signup(request):
	handler = RequestHandler()
	result = handler.handle_user_signup(request)
	return response.http_response(201, result)

def signin(request):
	handler = RequestHandler()
	result = handler.handle_user_sigin(request)
	return response.http_response(200, transformers.user_transformer(result))

def notify_users(request):
	handler = RequestHandler()
	result = handler.handle_notifying_users(request)
	return response.http_response(200, result)