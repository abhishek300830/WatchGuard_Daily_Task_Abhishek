"""
if you get an SMTPAuthenticationError even when your password is correct.
it's is possible that you have 2 Fator authentication enabled
you will need to use app password to login instead of normal password.

if you don't have 2FA enabled, you will have to allow access by 
less secure apps in your Gmail security preferences through remember to deactivate
once you finished learning about the python email sending.
"""
import smtplib
from email.message import EmailMessage

email_content ="""Dear Sir
i am sending you a mail using python.

kind regards
Abhi
"""

email = EmailMessage()
email['Subject'] = 'Test Email'
email['From'] = 'you@gmail.com'
email["To"] = 'ak9759250020@gmai.com'
email.set_content(email_content)


smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('you@gmail.com','password')

smtp_connector.send_message(email)