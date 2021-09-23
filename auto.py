import requests

try:
	wa = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=c568eb34e9aa05c9fd449df4cc568eae&user_id=193987156%40N02&format=json&nojsoncallback=1"
	res = requests.get(wa)
	print(res)

	data = res.json()
	print(data)

	
except Exception as e:
	print("issue", e)