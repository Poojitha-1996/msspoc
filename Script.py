# Databricks notebook source
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(subject, body, receiver_email):
    sender_email = "saipoojitha90@gmail.com"
    # Use Databricks Secrets to securely store email password (replace with actual secret)
    password = "ojsh zeag ydsd dhve"

    # Create the message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Use Gmail's SMTP server to send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)  # Login with your email and password from Databricks Secrets
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
    except Exception as email_error:
        print(f"Error sending email: {email_error}")

# Try to execute SQL and handle errors
try:
    # Execute your SQL code
    result = spark.sql("SELECT * FROM dwh.edws.fdhdjf")    
except Exception as e:
    # Handle the error and log it
    error_message = str(e).split("\n")[0]
    print(f"Error occurred: {error_message}")

    # Define email parameters
    subject = "Databricks SQL Script Failure Notification"
    body = f"Dear user,\n\nYour SQL script in Databricks failed with the following error:\n\n{error_message}"
    receiver_email = "saipoojitha90@gmail.com"  # This could be the script owner's email

    # Call the send_email function to send the notification
    send_email(subject, body, receiver_email)


# COMMAND ----------

current_user_email = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
print(current_user_email)
