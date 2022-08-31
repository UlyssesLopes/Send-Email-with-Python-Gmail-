import smtplib
import email.message

# configure email message

# first define your body text to send
body = """<h1> Hello, Ulysses </h1>
<p>  Test send email with python </p>
"""

subject = 'Test Send Email with Python Function'
my_from = ' your email '
my_to = ' email to '
my_password = '###############'


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

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

        print('Email Enviado')

    except:
        print('Email não enviado')
