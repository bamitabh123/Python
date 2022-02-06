#!/usr/bin/python3.4

from twilio.rest import Client

import schedule
import time
from datetime import datetime

account_sid = 'AC1fa943a39d4fb52fa1a26e1e5cc66767'
auth_token = '8135a3424f4b10385067323f301ee167'
client = Client(account_sid, auth_token)



# message = client.messages.create(
#     body='Test Message 1234',
#     from_='whatsapp:+14155238886',
#     #to='whatsapp:+919004927347'
#     to='whatsapp:+918962129334'
# )
#
#
#
# message = client.messages.create(
#     body='Test Message 321',
#     from_='whatsapp:+14155238886',
#     to='whatsapp:+919004927347'
#     #to='whatsapp:+918962129334'
# )
# print(message.sid)
def sendWhatsapp(message1):
    message = client.messages.create(
        body='Alert : '+message1,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919004927347'
    )
    message = client.messages.create(
        body='Alert : '+message1,
        from_='whatsapp:+14155238886',
        to='whatsapp:+918962129334'
    )

sendWhatsapp('Hi')