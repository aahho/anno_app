def user_transformer(data):
	print data
	return {
		'id' : data['id'],
		'displayName' : data['display_name'],
		'username' : data['username'],
		'is_active' : data['is_active'],
		'idToken' : data['idToken'],
		'refreshToken' : data['refreshToken']
	}