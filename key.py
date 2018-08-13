try:
	with open('../../.password/google-maps/api', 'r') as fp:
		key = fp.readlines()

	key = ''.join(key)

except:
	# Insert your API key here
	key = 'AIzaSyCFiggwEU6yOmDBF8-5ImsUzLPD7fmAkR8'