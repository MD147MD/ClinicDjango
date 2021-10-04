from kavenegar import *
from django.conf import settings

def send_sms(phone_number,message):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_KEY)
        params = {
            #'sender': 'درمانگاه فرهنگیان کوهدشت',#optional
            'receptor': phone_number,#multiple mobile number, split by comma
            'message': message,
        } 
        response = api.sms_send(params)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)