import os
from twilio.rest import Client


def sendsms():
    account_sid = 'AC6049ea1cda2adee0b79942603c6ba08d'
    auth_token = 'ff0c3308ab303d30a2909455e7bdbb48'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Xabaringiz muvafaqiyatli yuborildi!",
                        from_='+14438927078',
                        to='+998971401717'
                    )

    print('Xabaringiz muvafaqiyatli yuborildi!')