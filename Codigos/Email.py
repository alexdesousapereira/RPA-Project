import schedule
import time
from RoboPowerBI import BotRobo # importa função do arquivo Robo
import smtplib # enviar e-mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
try:
    print("Iniciou..")

    schedule.every().day.at("06:50").do(BotRobo)
    schedule.every().day.at("23:00").do(BotRobo)

    while True:
        schedule.run_pending()
        time.sleep(1)
except IndexError as e:

    # texto do email
    texto_email =   f'''
                    O bot notepade falhor, por gentileza, verificar.
                    Erro: {e}
                    '''

    # email remetente, senha, destinatário
    de = 'alexdesousapereiraa@gmail.com'
    senha = 'alex31032000alex'
    para = 'alexdesousapereira@ymail.com'
    # para02 = ''

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = de
    message['To'] = para
    # message['To'] = para02
    message['Subject'] = 'BotNotepad Falhou!!'  # Título do e-mail

    # Corpo do E-mail com anexos
    message.attach(MIMEText(texto_email, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
    session.starttls()  # Habilita a segurança
    session.login(de, senha)  # Login e senha de quem envia o e-mail
    texto = message.as_string()
    session.sendmail(de, para, texto)
    session.quit()