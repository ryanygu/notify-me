import smtplib
import config
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

'''
'''
def send_email(subject, message):
    try:
        sender = config.SENDER_EMAIL
        password = config.SENDER_PASSWORD
        recipient = config.RECIPIENT_EMAIL

        # set up MIME encoded message
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # connect to gmail and attempt to send
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()

        print('Success: sent email.\n')
    except:
        print('Error: could not send email.\n')

''' 
'''
def changes_detected(self):
    return True

if __name__ == "__main__":
    subject = 'test subject'    
    message = 'test message'

    while True:
        if (changes_detected()):
        send_email(subject, message)
        time.sleep(60)

