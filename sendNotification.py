# Databricks notebook source
# send_email_notification notebook

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, receiver_email):
    sender_email = "saipoojitha90@gmail.com"
    password = "ojsh zeag ydsd dhve"
    receiver_email = receiver_email
    body = body
    Subject = subject  # Store securely in Databricks Secrets or environment variables

    # Create the message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Sending the email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # Replace with your SMTP server
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as email_error:
        print(f"Error sending email: {email_error}")

