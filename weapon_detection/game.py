import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'gamechangersofusa2@gmail.com'
smtp_password = 'lnrwoduvxjbryakl'

# Create the email message
message = MIMEMultipart()
message['Subject'] = 'GAME changers in the house'
message['From'] = smtp_username
message['To'] = 'shahzadmustafa755@gmail.com'
body = 'GAME CHANGERS'
message.attach(MIMEText(body, 'plain'))

# Attach the image to the email
with open('6.jpeg', 'rb') as f:
    image_data = f.read()
image = MIMEImage(image_data, name=os.path.basename('6.jpeg'))
message.attach(image)

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, 'shahzadmustafa755@gmail.com', message.as_string())
