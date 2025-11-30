import undetected_chromedriver as uc
import schedule
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from schedule import repeat, every
from datetime import datetime, timedelta

"""
    ATENÇÃO:

    Aperte Ctrl + C para finalizar o loop

    Tenha paciência, foi adicionado um tempo de delay proposital para funcionar a autenticação do Gmail

    Para que esse código funcione é necessário:

        - Ter instalado as devidas bibliotecas (schedule, selenium e undetected-chromedriver)
        - Google Chrome
        - Baixar a versão do seu navegador Chrome em: https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br
        - Personalizar os campos de xpath conforme esse vídeo: https://www.youtube.com/watch?v=HbAbJgzYUw8&t=8s
            -> OBS: Os que estão como "'//input[@type=" pode-se deixar como está, pois não necessita de xpath
        - Por as informações corretas nos dados iniciais
"""

# Dados essenciais
email = "seu email@gmail.com"
senha = "senha do seu email"
destinarario = "email do destinatario@gmail.com"

# Função que atribui funcionalidade a função enviar_emails (com schedule usando repeat)
@repeat(every().saturday.at('09:00')) # Sábado às 09:00
def enviar_emails_culto_noite():
    # Coleta de dados iniciais
    assunto = "Igreja - Culto de Noite"
    mensagem = """Olá, vim avisar que amanhã é o culto da noite:

 - Data: Todos os domingos
 - Horário: 19:45
 - Local: Igreja, rua, bairro, cidade, estado"""

    # Abertura do Chrome e abertura do Google Gmail
    driver = uc.Chrome()
    driver.get("https://accounts.google.com")

    # Fazendo login
    campo_email = driver.find_element(By.XPATH, '//input[@type="email"]') # Localiza o local de email
    campo_email.send_keys(email) # Preenche campo do email
    campo_email.send_keys(Keys.RETURN)
    time.sleep(10) # Espera 10 segundos no máximo
    campo_senha = driver.find_element(By.XPATH, '//input[@type="password"]') # Localiza o local de email
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    time.sleep(10) # Espera 10 segundos no máximo

    # Acesso forçado do gmail
    driver.get("https://mail.google.com")

    # Clica no botão 'escrever'
    escrever = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div')
    escrever.click()
    time.sleep(10)

    # Vai na parte de 'destinatario'
    campo_destinatario = driver.find_element(By.XPATH, '//*[@id=":pp"]')
    campo_destinatario.send_keys(destinarario)

    # Vai na parte de 'assunto'
    assunto = driver.find_element(By.XPATH, '//*[@id=":lw"]')
    assunto.send_keys(destinarario)

    # Vai na parte de 'mensagem'
    campo_mensagem = driver.find_element(By.XPATH, '//*[@id=":nc"]')
    campo_mensagem.send_keys(mensagem)

    # Clica no botão de 'enviar'
    enviar = driver.find_element(By.XPATH, '//*[@id=":ll"]')
    enviar.click()
    time.sleep(10)

# Função que atribui funcionalidade a função enviar_emails (com schedule usando repeat)
@repeat(every().saturday.at('09:00')) # Sábado às 09:00
def enviar_emails_culto_manha():

    assunto = "Igreja - Culto de Manhã"
    mensagem = """Olá, vim avisar que amanhã é o culto da manhã:

 - Data: Todos os domingos
 - Horário: 08:45
 - Local: Igreja, rua, bairro, cidade, estado"""

    driver = uc.Chrome()
    driver.get("https://accounts.google.com")

    campo_email = driver.find_element(By.XPATH, '//input[@type="email"]')
    campo_email.send_keys(email)
    campo_email.send_keys(Keys.RETURN)
    time.sleep(10)
    campo_senha = driver.find_element(By.XPATH, '//input[@type="password"]')
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    time.sleep(10)

    driver.get("https://mail.google.com")

    escrever = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div')
    escrever.click()
    time.sleep(5)

    campo_destinatario = driver.find_element(By.XPATH, '//*[@id=":pp"]')
    campo_destinatario.send_keys(destinarario)

    assunto = driver.find_element(By.XPATH, '//*[@id=":lw"]')
    assunto.send_keys(destinarario)

    campo_mensagem = driver.find_element(By.XPATH, '//*[@id=":nc"]')
    campo_mensagem.send_keys(mensagem)

    enviar = driver.find_element(By.XPATH, '//*[@id=":ll"]')
    enviar.click()
    time.sleep(5)

@repeat(every().friday.at('09:00'))
def enviar_emails_rede_jovens():

    assunto = "Igreja - Rede de Jovens"
    mensagem = """Olá, vim avisar que amanhã terá a rede de jovens:

 - Data: Todos os sábados
 - Horário: 20:00
 - Local: Igreja, rua, bairro, cidade, estado"""

    driver = uc.Chrome()
    driver.get("https://accounts.google.com")

    campo_email = driver.find_element(By.XPATH, '//input[@type="email"]')
    campo_email.send_keys(email)
    campo_email.send_keys(Keys.RETURN)
    time.sleep(10)
    campo_senha = driver.find_element(By.XPATH, '//input[@type="password"]')
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    time.sleep(10)

    driver.get("https://mail.google.com")

    escrever = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div')
    escrever.click()
    time.sleep(5)

    campo_destinatario = driver.find_element(By.XPATH, '//*[@id=":pp"]')
    campo_destinatario.send_keys(destinarario)

    assunto = driver.find_element(By.XPATH, '//*[@id=":lw"]')
    assunto.send_keys(destinarario)

    campo_mensagem = driver.find_element(By.XPATH, '//*[@id=":nc"]')
    campo_mensagem.send_keys(mensagem)

    enviar = driver.find_element(By.XPATH, '//*[@id=":ll"]')
    enviar.click()
    time.sleep(5)

# Define a data para lançar o aviso do dia de ação de graças: Ano, Mês, Dia, Hora, Minuto, Segundo
dia_aviso_acao_gracas = datetime(2025, 12, 5, 9, 0, 0)
@repeat(every().day.until(dia_aviso_acao_gracas + timedelta(seconds=1))) # Garante que dará certo com o timedelta
def enviar_emails_acao_gracas():

    assunto = "Igreja - Dia de Ação de Graças (Rede de Jovens)"
    mensagem = """Olá, vim avisar que amanhã é o dia de ação de graças da rede de jovens:

 - Data: Nesse sábado
 - Horário: 20:00
 - Local: Igreja, rua, bairro, cidade, estado"""

    driver = uc.Chrome()
    driver.get("https://accounts.google.com")

    campo_email = driver.find_element(By.XPATH, '//input[@type="email"]')
    campo_email.send_keys(email)
    campo_email.send_keys(Keys.RETURN)
    time.sleep(10)
    campo_senha = driver.find_element(By.XPATH, '//input[@type="password"]')
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    time.sleep(10)

    driver.get("https://mail.google.com")

    escrever = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div')
    escrever.click()
    time.sleep(5)

    campo_destinatario = driver.find_element(By.XPATH, '//*[@id=":pp"]')
    campo_destinatario.send_keys(destinarario)

    assunto = driver.find_element(By.XPATH, '//*[@id=":lw"]')
    assunto.send_keys(destinarario)

    campo_mensagem = driver.find_element(By.XPATH, '//*[@id=":nc"]')
    campo_mensagem.send_keys(mensagem)

    enviar = driver.find_element(By.XPATH, '//*[@id=":ll"]')
    enviar.click()
    time.sleep(5)

# Loop infinito para ele funcionar
while True:
    schedule.run_pending()
    time.sleep(5) # Limite de velocidade de 5 segundo a cada loop para não encher a memória