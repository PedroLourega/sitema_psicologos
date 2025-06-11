from flask import Flask, render_template, request, redirect, url_for  # Importa o que falta

app = Flask(__name__)  # cria uma instância do Flask

# Cria uma URL para a página principal do site
@app.route('/')
def home():
    return render_template('index.html')

# Página de acesso
@app.route('/acesso')
def escolha_acesso():
    return render_template('escolha_acesso.html')

# Página de login do psicólogo
@app.route('/psicologo-login', methods=['GET', 'POST'])
def psicologo_login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Aqui pode colocar sua validação de psicólogo (exemplo fixo)
        if username == 'admin' and password == '1234':
            return redirect(url_for('dashboard_psicologo'))  # Redireciona para o dashboard
        else:
            error = 'Usuário ou senha incorretos.'
            
    return render_template('psicologo_login.html', error=error)
# Página de login do paciente
@app.route('/paciente-login', methods=['GET', 'POST'])
def paciente_login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Exemplo de validação simples
        if username == 'paciente1' and password == 'abcd':
            render_template('dashboard_paciente.html')
        else:
            error = 'Usuário ou senha incorretos.'
            
    return render_template('paciente_login.html', error=error)


# Dashboard do psicólogo
@app.route('/dashboard/psicologo')
def dashboard_psicologo():
    return render_template('dashboard_psicologo.html')  

# Dashboard do paciente
@app.route('/dashboard/paciente')
def dashboard_paciente():
    return render_template('dashboard_paciente.html')  

# garante que o app só será executado se este arquivo for rodado diretamente
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo debug