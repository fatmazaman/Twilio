from twilio.rest import TwilioRestClient

account_sid = " AC5ba19564ecfd47881407d0a67f58a5a0" # Your Account SID from www.twilio.com/console
auth_token  = "4313df59270935fbcc6e84f60a3dcac0"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
	body="My name is Fatma Zaman",
    to="+18133751280",    # Replace with your phone number
    from_="+18139023117") # Replace with your Twilio number

print(message.sid)
