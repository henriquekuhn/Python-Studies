from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = '+13253089916'
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")

MAIL_PROVIDER_SMTP_ADDRESS = os.getenv("MAIL_PROVIDER_SMTP_ADDRESS")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

        
class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    def send_sms(self, message):
        message = self.client.messages.create(
            body=f"{message}",
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
            ) 
        
    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )