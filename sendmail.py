import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = ''
password = ''

def send_mail(msg_body = "No text", subject = "Hello world", from_mail = "{Name} <___@gmail.com>", to_mails = []):
	assert isinstance(to_mails,list)

	from_mail = from_mail.format(Name = sys.argv[1])

	msg = MIMEMultipart('alternative')
	msg['From'] = from_mail
	msg['To'] = ", ".join(to_mails)
	msg['Subject'] = subject

	body = MIMEText(msg_body,'plain')
	msg.attach(body)

	msg_str = msg.as_string()

	server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(from_mail,to_mails,msg_str)

	server.quit()

if __name__ == "__main__":

	to = sys.argv[2]

	body = input("Enter the mail: ")
	sub = input("Enter the subject: ")

	send_mail(msg_body = body,subject = sub,to_mails = [to])