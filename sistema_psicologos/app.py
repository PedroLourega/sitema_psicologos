from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import (init_db, verificar_login_psicologo, verificar_login_paciente, 
                     listar_consultas, listar_psicologos, criar_paciente, 
                     agendar_consulta, listar_pacientes, consultas_paciente)

app = Flask(__name__)
app.secret_key = 'connect_psicologos_secret_key_2025'  # Para sessions e flash messages

# Inicializa o banco de dados
init_db()

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
        
        # Verifica login no banco de dados
        psicologo = verificar_login_psicologo(username, password)
        if psicologo:
            session['psicologo_id'] = psicologo['id']
            session['psicologo_nome'] = psicologo['nome']
            session['user_type'] = 'psicologo'
            return redirect(url_for('dashboard_psicologo'))
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
        
        # Verifica login no banco de dados
        paciente = verificar_login_paciente(username, password)
        if paciente:
            session['paciente_id'] = paciente['id']
            session['paciente_nome'] = paciente['nome']
            session['user_type'] = 'paciente'
            return redirect(url_for('dashboard_paciente'))
        else:
            error = 'Usuário ou senha incorretos.'
            
    return render_template('paciente_login.html', error=error)

# Dashboard do psicólogo
@app.route('/dashboard/psicologo')
def dashboard_psicologo():
    if 'psicologo_id' not in session:
        return redirect(url_for('psicologo_login'))
    
    consultas = listar_consultas()
    psicologos = listar_psicologos()
    pacientes = listar_pacientes()
    
    return render_template('dashboard_psicologo.html', 
                         consultas=consultas, 
                         psicologos=psicologos,
                         pacientes=pacientes,
                         psicologo_nome=session.get('psicologo_nome'))

# Dashboard do paciente
@app.route('/dashboard/paciente')
def dashboard_paciente():
    if 'paciente_id' not in session:
        return redirect(url_for('paciente_login'))
    
    consultas = consultas_paciente(session['paciente_id'])
    
    return render_template('dashboard_paciente.html', 
                         consultas=consultas,
                         paciente_nome=session.get('paciente_nome'))

# Criar novo paciente (apenas psicólogos podem fazer)
@app.route('/criar-paciente', methods=['POST'])
def criar_novo_paciente():
    if 'psicologo_id' not in session:
        return redirect(url_for('psicologo_login'))
    
    nome = request.form['nome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data_nascimento']
    username = request.form['username']
    password = request.form['password']
    
    if criar_paciente(nome, cpf, data_nascimento, username, password):
        flash('Paciente criado com sucesso!', 'success')
    else:
        flash('Erro: Username já existe!', 'error')
    
    return redirect(url_for('dashboard_psicologo'))

# Agendar nova consulta (apenas psicólogos podem fazer)
@app.route('/agendar-consulta', methods=['POST'])
def nova_consulta():
    if 'psicologo_id' not in session:
        return redirect(url_for('psicologo_login'))
    
    paciente_id = request.form['paciente_id']
    psicologo_id = request.form['psicologo_id']
    data_consulta = request.form['data_consulta']
    horario = request.form['horario']
    
    agendar_consulta(paciente_id, psicologo_id, data_consulta, horario)
    flash('Consulta agendada com sucesso!', 'success')
    
    return redirect(url_for('dashboard_psicologo'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# garante que o app só será executado se este arquivo for rodado diretamente
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo debug