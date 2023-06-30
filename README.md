# Message_GPT
This is a simple chatbot application that integrates Twilio for SMS messaging and OpenAI API for generating AI-powered responses. The chatbot assumes the persona of a loving son, providing uplifting and positive responses to the user.

Prerequisites
Python 3.7 or higher
Twilio account credentials (Account SID, Auth Token, Twilio phone number)
OpenAI API key

Setup
Clone the repository: git clone https://github.com/your-username/twilio-chatbot.git
Install the required dependencies: pip install flask twilio openai

Update the following variables in app.py:
account_sid - Your Twilio account SID
auth_token - Your Twilio account auth token
twilio_number - Your Twilio phone number
destination_number - Phone number to receive the chatbot responses
openai.api_key - Your OpenAI API key

Usage
Start the Flask development server: python app.py
Expose the local server to the internet using ngrok: ngrok http 5010

Update the Messaging Webhook URL in your Twilio account:
Go to the Twilio Console
Navigate to "Phone Numbers"
Click on your Twilio phone number
In the "Messaging" section, update the "A MESSAGE COMES IN" webhook URL with the ngrok forwarding URL (e.g., http://<ngrok-url>/sms)
Send a text message to your Twilio phone number and start chatting with the chatbot!

Notes
The chatbot assumes the persona of a loving son, providing positive and uplifting responses.
Make sure to fill in the blanks with your own api key and tokens!
