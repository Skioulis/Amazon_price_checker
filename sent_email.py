import smtplib
from dotenv import load_dotenv
import os


def sent_email(message: str):
    subject = "Amazon Price Alert!"
    email_to = "skioulis@gmail.com"
    load_dotenv(dotenv_path="ENV files/.env")
    smtp = os.getenv("GMAIL_smtp")
    port = os.getenv("PORT")
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD")
    connection = smtplib.SMTP(smtp, port=port)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email_to, msg=f"Subject:{subject}\n\n{message}".encode("utf-8"))
    connection.close()

    print ("ok") # TODO: delete

