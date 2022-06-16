from twilio.rest import Client
import keys

def message():
    client = Client(keys.account_sid, keys.auth_token)
    number = input()
    content = input()
    message = client.messages.create(
        body = content,
        from_='+18575977076',
        to=number

        )
    print(message.body)