import glob
import requests
import json

files = glob.glob('*.jpg')

for file in files:
	base_file = file.split("/")[-1]
	output = open(base_file.replace(".jpg", ".json"))
	url = f"http://localhost:3000/api/json/{base_file}"
	json.dump(requests.get(url).json(), output)