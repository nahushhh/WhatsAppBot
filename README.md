# WhatsAppBot

Steps to run locally - 
1 - Open command prompt in your project folder.

2 - Start the flask app by entering the command `flask.run`.

3 - Start the ngrok server using command `ngrok http port_number` (I had installed ngrok in my project's local directory. If you are using ngrok for the first time, make sure to execute the authentication command first. The authentication command can be found on the ngrok website.)

  3.1 - Copy the link from ngrok and paste it in the Callback URL section in the WhatsApp Business API Configuration page. Add /webhook as the endpoint 
  (https://33ee-110-226-179-194.ngrok-free.app/webhook). Make sure you are subsribed to the messages webhook on the WhatsApp Business API
  
  3.2 - Set a Verify token.
  
4 - Copy the local host URL obtained from step 2 in the browser.

5 - Navigate to send_template_msg endpoint to send a template message. Template message is the first message that goes from the business side.

6 - After receiving the template message, the user can start having a conversation with bot.

Note: Make sure to populate config.json with the right values which can be obtained from the WhatsApp Business API home page
