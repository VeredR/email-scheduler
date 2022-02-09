from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv
import rentals

load_dotenv(".env")

SENDER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")


def send_email(recipient, subject, text):
    msg = EmailMessage()
    msg.set_content(text)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = recipient
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER, PASSWORD)
    server.send_message(msg)
    server.quit()


current_rentals = rentals.get_current_rentals()
all_current_rentals = ""
for rental in current_rentals:
    for rent in rental:
        if current_rentals.index(rental) < len(current_rentals) - 1:
            all_current_rentals += rent + ", "
        elif current_rentals.index(rental) == len(current_rentals) - 1:
            all_current_rentals += rent+"."

body = "The active rentals for this day are: "+"\b" + all_current_rentals

send_email("vered.Ros@gmail.com", "test", body)

