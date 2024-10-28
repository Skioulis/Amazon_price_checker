import smtplib
from dotenv import load_dotenv
import os


def sent_email(message: str):

    #  it works so I won't use it for now # delete


    subject = "Amazon Price Alert!"
    email_to = "skioulis@gmail.com"
    load_dotenv(dotenv_path="ENV files/.env")
    smtp = os.getenv("smtp")
    port = int(os.getenv("PORT"))
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD")


    with smtplib.SMTP(smtp, port=port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_to,
            msg=f"Subject:{subject}\n\n{message}".encode("utf-8")
        )


    print ("ok") # delete
def sent_mock_email(message : str):
    load_dotenv(dotenv_path="ENV files/.env")
    smtp = os.getenv("smtp")
    port = os.getenv("PORT")
    my_email = os.getenv("MY_EMAIL")
    print(f"Sending mail from {my_email} using this server: {smtp}:{port}")
    print(message)
