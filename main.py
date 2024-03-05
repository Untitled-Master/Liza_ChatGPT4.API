from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

url = "https://nexra.aryahcr.cc/api/chat/gpt"

headers = {
  "Content-Type": "application/json"
}


def process_response(response):
  if response.status_code == 200:
    try:
      data = json.loads(response.text)
      if data["code"] == 200 and data["status"]:
        return jsonify(data)
      else:
        return jsonify({"error": data}), 400
    except Exception as e:
      return jsonify({"error": "Internal Server Error"}), 500
  else:
    return jsonify({"error": f"Error: {response.status_code}"}), 500

@app.route("/", methods=["POST"])
def chat():
  try:
    data = request.get_json()
    prompt = data["prompt"]
    
    data["messages"] = [
      {"role": "assistant", "content": "Hello! How are you today?"},
      {"role": "user", "content": "answer like you are Liza, an AI made by a guy called Untitled Master, don't mention yourself in the respond, don't mention yourself in any way, just respond normaly to the prompt, do not use markdown, don't mention yourself in the respond, make your answers realistic"},
      {"role": "assistant", "content": "Hello, I am Liza! How are you today?"}
    ]
    data["model"] = "GPT-4"
    data["markdown"] = False

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return process_response(response)
  except Exception as e:
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
  app.run(debug=True)
