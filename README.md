# Projeto-Final-de-Algoritmos-e-Programação

Esse trabalho teve como objetivo criar uma solução para o esquecimento ou
até o mal entendimento de horários de eventos divulgados por uma determinada
igreja; para criar essa solução, ou ao menos melhorar o caso, foi desenvolvido um
site contendo a agenda de uma igreja, tanto em formato público (com eventos
divulgados mais recentemente e atualizados), como privado (com eventos, escalas e
mais que foram divulgados ou previstos) além de um programa em python que
enviará email através do Gmail automaticamente em um determinado período.

Para a criação e funcionamento do site e do sistema automático de
lembretes, foi utilizado e instalado o framework Flask e as bibliotecas schedule,
selenium, undetected-chromedriver e outras já presentes no python 3.13.9; o arquivo
contendo essas informações está em static, instalar_bibliotecas.txt.

AGENDA DA IGREJA

Para a criação do site foi utilizado em python o framework chamado Flask, ele
possibilita a criação de aplicações web simples; Ele foi importado no arquivo
chamado main.py.

O arquivo views.py importa do arquivo main.py o app e do Flask o render_templates. A
finalidade desse arquivo é definir as rotas do site, definindo qual será o URL da parte
pública e privada do site e em qual arquivo html ele deve buscar. A home do site, ou
seja, logo quando se abre o site, aparecerá na parte pública. Para acessar a parte
privada, basta adicionar no URL “/organizacao” e ele entrará na parte privada.
Os arquivos HTML estão presentes na pasta chamada templates, contendo a
homepage.html e a organizacao.html, que são, respectivamente, a estrutura da
parte pública e privada do site, e os arquivos CSS estão presentes em outra pasta
chamada static, que contém os arquivos style-homepage.css e
style-organizacao.css, que são a estilização das duas partes na mesma ordem.

SISTEMA AUTOMÁTICO DE LEMBRETE VIA EMAIL

Os códigos presentes nesse sistema estão no arquivo agendador.py. Para
seu funcionamento, ele necessita que o usuário utilize o navegador Chrome e instale
no link https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br de
acordo com a sua versão. Delete a pasta chrome-win64 e posicione no lugar a que
foi instalada e descompacte-a.

Informações importantes

Nas sete primeiras linhas há a importação das bibliotecas

        undetected_chromedriver, schedule, time, selenium e datetime e funcionalidades
        presentes nelas:
        import undetected_chromedriver as uc
        import schedule
        import time
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        from schedule import repeat, every
        from datetime import datetime, timedelta

Após há um enunciado com informações importante antes da utilização do
programa:

        """
        ATENÇÃO:
        Aperte Ctrl + C para finalizar o loop
        Tenha paciência, foi adicionado um tempo de delay proposital para
        funcionar a autenticação do Gmail
        Para que esse código funcione é necessário:
        - Ter instalado as devidas bibliotecas (schedule, selenium e
        undetected-chromedriver)
        - Google Chrome
        - Baixar a versão do seu navegador Chrome em:
        https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br
        - Personalizar os campos de xpath conforme esse vídeo:
        https://www.youtube.com/watch?v=HbAbJgzYUw8&t=8s
        -> OBS: Os que estão como "'//input[@type=" pode-se deixar
        como está, pois não necessita de xpath
        - Por as informações corretas nos dados iniciais
        """
  
Depois há a coleta de dados importantes para o funcionamento:
        
        # Dados essenciais
        email = "seu email@gmail.com"
        senha = "senha do seu email"
        destinarario = "email do destinatario@gmail.com"

Funcionamento

Na primeira linha das há a atribuição de uma funcionalidade à função
presente abaixo desta, utilizando o @repeat, que é uma parte da biblioteca
schedule, que permite definir o tempo em que a função será chamada. Por exemplo
na dos cultos da manhã e noite foi definido para chama-lá todos os sábados às
09:00:

        @repeat(every().saturday.at('09:00'))
        
Também pode ser definido para um dia, mês, ano, hora, minuto e segundo
específico, utilizando a biblioteca datetime facilita-se essa implementação, por
exemplo para o dia de ação de graças:
        
        dia_aviso_acao_gracas = datetime(2025, 12, 5, 9, 0, 0)
        @repeat(every().day.until(dia_aviso_acao_gracas +timedelta(seconds=1)))

Foi adicionado um um segundo a mais para corrigir alguns erros em
timedelta(seconds=1).

Para que o schedule funcione, é necessário um loop infinito, utilizamos o
while sempre verdadeiro; para interromper esse loop, basta pressionar Ctrl + C no
terminal. A linha seguinte faz rodar a biblioteca schedule. Logo após essa linha à um
limitador de tempo em que o loop ocorrará, aqui foi colocado de cinco segundos,
apenas para não sobrecarregar a memória:

        while True:
          schedule.run_pending()
          time.sleep(5)

É definido uma função para cada dia em que será lançado o email do evento,
foi definido a função para o culto da manhã e noite, rede de jovens e dia de ação de
graças (da rede de jovens), respectivamente, enviar_emails_culto_noite (sábado),
enviar_emails_culto_manha (sábado), enviar_emails_rede_jovens (sexta) e
enviar_emails_acao_gracas (12/05/2025). Todos estão para às 09:00, porém apenas
os três primeiros seguem o mesmo padrão. Essas funções não contém parâmetros,
mas utiliza variáveis globais.

Inicialmente foi definido o assunto e a mensagem do email na variável
assunto e mensagem, por exemplo no do culto da noite:

        assunto = "Igreja - Culto de Noite"
        mensagem = """Olá, vim avisar que amanhã é o culto da noite:
        - Data: Todos os domingos
        - Horário: 19:45
        - Local: Igreja, rua, bairro, cidade, estado"""

Após, é aberto respectivamente o navegador Chrome e a área de login do
email:

        driver = uc.Chrome()
        driver.get("https://accounts.google.com")

Então é encontrado o local para preencher o email, armazenando na variável
campo_email:

        campo_email = driver.find_element(By.XPATH, '//input[@type="email"]')

É preenchido com o que foi descrito na variável email, com o email do
remetente:
        
        campo_email.send_keys(email)
        campo_email.send_keys(Keys.RETURN)

Então é colocado um tempo de espera máximo para ir ao próximo passo, aqui
foi colocado de dez segundos:

        time.sleep(10)

É repetido o mesmo para a senha:

        campo_senha =driver.find_element(By.XPATH, '//input[@type="password"]')
        campo_senha.send_keys(senha)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(10)
        Após realizado o login, abre-se forçadamente o local de email:
        driver.get("https://mail.google.com")

Encontra-se e clica-se no botão de escrever com um tempo máximo definido:

        escrever=driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div')
        escrever.click()
        time.sleep(10)

Encontra-se e preenche-se os campos de destinatário, assunto e mensagem
assim como no campo de login:

        campo_destinatario = driver.find_element(By.XPATH, '//*[@id=":pp"]')
        campo_destinatario.send_keys(destinarario)
        assunto = driver.find_element(By.XPATH, '//*[@id=":lw"]')
        assunto.send_keys(destinarario)
        campo_mensagem = driver.find_element(By.XPATH, '//*[@id=":nc"]')
        campo_mensagem.send_keys(mensagem)

Encontra-se e clica-se em enviar assim como ocorreu no campo de escrever:

        enviar = driver.find_element(By.XPATH, '//*[@id=":ll"]')
        enviar.click()
        time.sleep(10)

O mesmo modelo se aplica para todas as outras funções.

Observou-se que, de fato, o sistema de lembrete automático via email
consegue abrir o navegador, efetuar o login, abrir o email, escrever e enviar o email.
Porém houve algumas complicações, após efetuar o envio do email, o navegador
permanece aberto e necessita abrir outro para enviar outro email, também às vezes
ele não encontra corretamente os locais à preencher.

É necessário alguns ajustes, como a utilização de arquivos txt por exemplo para a mensagem do email, o
fechamento automático do navegador e melhoria na localização dos campos à ser
preenchido.
