from twilio.rest import Client
import Keys
client = Client(Keys.account_sid, Keys.auth_token)
message = client.messages.create(
    body="The Smart Bin is Full, Please come and collect the Garbage \n\n\nLocation:\nhttps://www.google.com/maps/place/Sri+Sairam+Institute+of+Technology/@12.9606471,80.0532325,15z/data=!4m5!3m4!1s0x0:0xf3aef7ec7c8979ba!8m2!3d12.9606471!4d80.0532325",
    from_=Keys.twilio_number,
    to=Keys.my_phone_number
)
print(message.body)
