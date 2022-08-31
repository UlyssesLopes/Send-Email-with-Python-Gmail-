import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# configure email message

# first define your body text to send
body = """<h1> Olá, Ulysses </h1>
<p>  Teste de Envio de Email com python</p>
"""

subject = 'Test Send Email with Python Function'
my_from = ' here your email from '
my_to = ' here your email to '
my_password = '##########'
host = 'smtp.gmail.com'
port = '587'


# function for send emails with attachments
def send_email_with_files():
    try:
        server = smtplib.SMTP(host,port)
        server.ehlo()
        server.starttls()
        server.login(my_from, my_password)

        email_msg = MIMEMultipart()
        email_msg['From'] = my_from
        email_msg['To'] = my_to
        email_msg['Subject'] = subject
        email_msg.attach(MIMEText(body, 'html'))

        cam_arquivo = './files/sendtest.pdf'
        attachment = open(cam_arquivo, 'rb')

        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attachment.read())
        encoders.encode_base64(att)

        att.add_header('Content-Disposition', f'attachment; filename=sendtest.pdf')
        attachment.close()

        email_msg.attach(att)

        server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
        server.quit()

        msg = 'Email and File send!'
        print(msg)

    except:
        msg = 'Email and File not send!'
        print(msg)


# function for send a normal email without files
def send_email():
    body_email = body

    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = my_from
    msg['To'] = my_to
    password = my_password

    try:
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(body_email)

        s = smtplib.SMTP(host,port)
        s.starttls()

        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

        msg = 'Email Send!'
        print(msg)

    except:
        msg = 'Email not Send!'
        print(msg)









