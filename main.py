import smtplib
import email.message

# configure email message

# first define your body text to send
body = """<h1> Olá, Ulysses </h1>
<p>  Teste de Envio de Email </p>
"""

subject = 'Test Send Email with Python Function'
my_from = 'ulysses.rlopes@gmail.com'
my_to = 'ulysses.rlopes@gmail.com'
my_password = 'mlqtlyittczuanhb'


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
