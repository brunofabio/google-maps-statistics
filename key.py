try:
	with open('../../.password/google-maps/api', 'r') as fp:
		key = fp.readlines()

	key = ''.join(key)

except:
	# Insert your API key here
	key = 'YOUR_API_KEY_HERE'