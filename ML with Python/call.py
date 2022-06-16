from twilio.rest import Client

import keys

def call():
    client = Client(keys.account_sid, keys.auth_token)
    number = input()
    call = client.calls.create(
        from_='+18575977076',
        to=number,
        url="http://demo.twilio.com/docs/voice.xml"

    )
    print(call.sid)