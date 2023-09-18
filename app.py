from flask import Flask, request, jsonify
import json
import requests
from message_helper import WhatsAppWraper


app = Flask(__name__)

with open('config.json') as f:
    config = json.load(f)

client = WhatsAppWraper()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/send_template_msg")
def send_template_message():
    data = client.send_template_msg_function()
    return data.text, data.status_code

# @app.route("/send_text_msg")
# def send_text_message():
#     text_response = client.send_text_msg_function("Hi again") 
#     return text_response.text, text_response.status_code

@app.route('/webhook', methods=['POST', 'GET'])
def webhook_function():
   if request.method == "GET":
        if request.args.get('hub.verify_token') == config['VERIFY_TOKEN']:
            return request.args.get('hub.challenge')
        return "Authentication failed. Invalid Token."
   res = client.webhook_handler()
   text_response = client.send_text_msg_function(res) 
   return text_response.text, text_response.status_code
#    return jsonify({"status": "success"}, 200)


# @app.route("/webhook/", methods=["POST", "GET"])
# def webhook_whatsapp():
#     """__summary__: Get message from the webhook"""
    
#     if request.method == "GET":
#         print(request.args.get('hub.verify_token'))
#         if request.args.get('hub.verify_token') == config['VERIFY_TOKEN']:
#             return request.args.get('hub.challenge')
#         return "Authentication failed. Invalid Token."

#     response = process_webhook_notification(request.get_json())
#     print(response)
#     return jsonify({"status": "success"}, 200)

if (__name__) == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
