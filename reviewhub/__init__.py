from flask import Flask, render_template  # <-- Importe o render_template

# 1. Cria a instância da aplicação Flask
app = Flask(__name__)


# 2. Define a rota principal (a homepage, ou '/')
@app.route('/')
def homepage():
    # 3. Agora, em vez de um texto, renderize o seu arquivo HTML
    # O Flask vai procurar por 'index.html' na pasta 'templates'
    return render_template('index.html')


# 4. Você pode criar quantas rotas quiser
@app.route('/sobre')
def pagina_sobre():
    return 'Aqui você pode colocar informações "Sobre" o seu projeto.'

# 5. Rota com um parâmetro dinâmico
@app.route('/usuario/<nome>')
def perfil_usuario(nome):
    return f'Olá, {nome}! Bem-vindo ao seu perfil.'

# Nota: Não precisamos de "if __name__ == '__main__':"
# O comando "poetry run flask --app reviewhub run" cuida de encontrar
# a variável 'app' e executar o servidor.from flask import Flask, render_template  # <-- Importe o render_template

# 1. Cria a instância da aplicação Flask
app = Flask(__name__)


# 2. Define a rota principal (a homepage, ou '/')
@app.route('/')
def homepage():
    # 3. Agora, em vez de um texto, renderize o seu arquivo HTML
    # O Flask vai procurar por 'index.html' na pasta 'templates'
    return render_template('index.html')


# 4. Você pode criar quantas rotas quiser
@app.route('/sobre')
def pagina_sobre():
    return 'Aqui você pode colocar informações "Sobre" o seu projeto.'

# 5. Rota com um parâmetro dinâmico
@app.route('/usuario/<nome>')
def perfil_usuario(nome):
    return f'Olá, {nome}! Bem-vindo ao seu perfil.'

# Nota: Não precisamos de "if __name__ == '__main__':"
# O comando "poetry run flask --app reviewhub run" cuida de encontrar
# a variável 'app' e executar o servidor.