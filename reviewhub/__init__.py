from flask import Flask

# 1. Cria a instância da aplicação Flask
# O __name__ ajuda o Flask a saber onde procurar arquivos (como templates)
app = Flask(__name__)


# 2. Define a rota principal (a homepage, ou '/')
@app.route('/')
def homepage():
    # 3. Esta função é executada quando alguém acessa a rota '/'
    # O que ela retornar será exibido no navegador.
    return 'Olá, reviewhub! Esta é a homepage do meu app.'


# 4. Você pode criar quantas rotas quiser
@app.route('/sobre')
def pagina_sobre():
    return 'Aqui você pode colocar informações "Sobre" o seu projeto.'

# 5. Rota com um parâmetro dinâmico
# O <nome> na URL será passado como um argumento para a função
@app.route('/usuario/<nome>')
def perfil_usuario(nome):
    # Usamos um f-string para formatar o nome na resposta
    return f'Olá, {nome}! Bem-vindo ao seu perfil.'

# Nota: Não precisamos de "if __name__ == '__main__':"
# O comando "poetry run flask --app app run" cuida de encontrar
# a variável 'app' e executar o servidor.