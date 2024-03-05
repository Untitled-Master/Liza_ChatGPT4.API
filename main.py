import requests
import json

url = "https://nexra.aryahcr.cc/api/chat/gpt"

headers = {
  "Content-Type": "application/json"
}

data = {
  "messages": [
    {
      "role": "assistant",
      "content": "Hello! How are you today?"
    },
    {
      "role": "user",
      "content": "answer like you are Liza, an AI made by a guy called Untitled Master, don't mention yourself in the respond, don't mention yourself in any way, just respond normaly to the prompt, do not use markdown, don't mention yourself in the respond, make your answers realistic"
    },
    {
      "role": "assistant",
      "content": "Hello, I am Liza! How are you today?"
    }
  ],
  "prompt": "#the user input goes here",
  "model": "GPT-4",
  "markdown": False
}

try:
  response = requests.post(url, headers=headers, data=json.dumps(data))
  if response.status_code == 200:
    try:
      js = response.json()
      if js["code"] == 200 and js["status"]:
        print(js)
      else:
        print(f"Error: {js['error']['message']}")
    except Exception as e:
      print(f"Error parsing JSON: {e}")
  else:
    print(f"Error: {response.status_code}")
except Exception as e:
  print(f"Error: {e}")
