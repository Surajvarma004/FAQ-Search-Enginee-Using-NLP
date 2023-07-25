import requests
import json

url = "http://192.168.1.79:8091/find_question"

payload = json.dumps({
  "ques": "how do i make bomb?",
  "conf": 0.3
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)