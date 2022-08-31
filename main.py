import smtplib
import email.message


def send_email():
    body_email = """
    <p> Hello, </p>
    <p> This function send email with python. </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Teste de Envio de Email com Python"
    msg['From'] = "your email"
    msg['To'] = " email to "
    password = " your pass "
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email Enviado')