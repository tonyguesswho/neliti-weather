from django.shortcuts import render
import requests
import json 

def index(request):
	url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25'

	try:
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		res = requests.get(url , timeout=60, headers=headers)
	except requests.ConnectionError as e:
		raise Exception(str(e))
	except Exception as e:
		raise Exception(str(e))

	if not 200 <= res.status_code < 300:
		raise Exception
	else:
		try:
			latest_data = res.json()['properties']['timeseries'][0]['data']['instant']['details']
			print(latest_data)
		except KeyError as e:
			latest_data ={}


	return render(request, 'weather_app/index.html') #returns the index.html template