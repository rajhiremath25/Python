import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the sender and receiver email addresses
sender_email = 'geetachiremath.25@gmail.com'
receiver_email = 'rajhiremath.25@gmail.com'

# Set up the SMTP server and login credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'geetachiremath.25@gmail.com'
password = 'Geeta555'

# Create the email message
subject = 'Hello from Python!'
body = 'This is the content of the email.'
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Email sent successfully!')
