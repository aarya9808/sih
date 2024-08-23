from plyer import notification

def send_notification():
    notification.notify(
        title='Needs help',
        message='This is a test notification from Plyer.',
        app_name='Surveillance System',
        timeout=5  # Duration in seconds
    )

if __name__ == "__main__":
    send_notification()



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_alarm_email(smtp_server, smtp_port, smtp_user, smtp_pass, recipient, subject, message_body):
 
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient
    msg['Subject'] = subject
    
   
    msg.attach(MIMEText(message_body, 'plain'))
    
    try:
       
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(smtp_user, smtp_pass)  
            server.sendmail(smtp_user, recipient, msg.as_string()) 
        print("Alarm email sent successfully.")
    except Exception as e:
        print(f"Failed to send an alarm email: \n\n{e}")


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'ryabadhe11@gmail.com'
smtp_pass = 'bvup qbbu dfws rmdp'
recipient = 'fantasizerya@proton.me'
subject = 'Urgent: Alarm Notification'
message_body = (
    "Attention,\n\n"
    "An alarm has been triggered with the following details:\n\n"
    "Please investigate the issue as soon as possible.\n\n"
   
)

send_alarm_email(smtp_server, smtp_port, smtp_user, smtp_pass, recipient, subject, message_body)
