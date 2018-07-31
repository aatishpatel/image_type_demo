import requests
import sys
import json

API_KEY = 'AEajS8_Eomr4xyGMxKDpvubZ3XOf6BAGR_S3lEyAd6H'

def get_top_label(json_response):
	response = json.loads(json_response)
	prediction = response["result"][0]["prediction"]
	max_label_dict = max(prediction, key=lambda x:x['probability'])
	return max_label_dict["label"], max_label_dict["probability"]

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

data = {'file': open(sys.argv[2], 'rb'), 'modelId': ('', sys.argv[1])}

response = requests.post(url, auth= requests.auth.HTTPBasicAuth(API_KEY, ''), files=data)

label, probability = get_top_label(response.text)
print "Prediction is:\n", label
print "\nWith Confidence:\n", probability