import smtplib
import time
import os
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')
subject_base = os.getenv('SUBJECT')
message_text = os.getenv('MESSAGE')
message_reload = int(os.getenv('MESSAGE_RELOAD'))

target = ['ashasdhasdhasd@gmail.com']  # Coloque o email de destino aqui


def generate_random_string(length=3):
    """Gera uma string aleatória de letras e dígitos."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))


try:
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email, password)

    for send_mail in target:
        for _ in range(message_reload):
            # Gera a string aleatória e adiciona ao assunto
            random_string = generate_random_string()
            subject = f"{subject_base} {random_string}"

            # Criao objeto da mensagem
            message = MIMEMultipart()
            message['From'] = email
            message['To'] = send_mail
            message['Subject'] = subject
            message.attach(MIMEText(message_text, 'plain'))

            # Envia o e-mail
            mail.send_message(message)
            print(f"Mensagem enviada para {send_mail} com o assunto: {subject}")
            time.sleep(1)

    mail.quit()
except Exception as e:
    print(f"Ocorreu um erro: {e}")

print("Concluído")
