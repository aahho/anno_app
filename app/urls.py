from g_firebase.urls import firebase

## 
# Register all url blueprints
# @param blueprint_instance as app
##
def register_urls(app):
	## Blueprint for firebase
	app.register_blueprint(firebase)