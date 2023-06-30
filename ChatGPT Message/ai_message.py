import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# OpenAI API key
openai.api_key = ""

# Twilio configuration
account_sid = ''
auth_token = ''
twilio_number = ''
destination_number = ''

app = Flask(__name__)
client = Client(account_sid, auth_token)
messages = []

def send_message_via_twilio(message):
    """Send a message via Twilio."""
    client.messages.create(
        from_=twilio_number,
        body=message,
        to=destination_number
    )

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming text messages."""
    incoming_message = request.values.get('Body')
    
    # Add user message to the messages list
    messages.append({"role": "user", "content": incoming_message})

    # Construct the persona message of a loving son
    persona_message = "Hi Mom, it's your loving son. How can I uplift your day today? Remember, you are strong, loved, and capable of anything!"
    
    # Add the persona message to the messages list
    messages.append({"role": "system", "content": persona_message})

    # Send user and persona messages to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Get the assistant's reply from the API response
    reply = response.choices[0].message.content
    
    # Split the reply into smaller chunks if it exceeds the SMS character limit
    reply_chunks = [reply[i:i+160] for i in range(0, len(reply), 160)]
    
    # Send each chunk of the reply via Twilio
    for chunk in reply_chunks:
        send_message_via_twilio(chunk)
    
    # Add assistant's reply to the messages list
    messages.append({"role": "assistant", "content": reply})
    
    return str(MessagingResponse())

if __name__ == "__main__":
    app.run(debug=True, port=5010)
