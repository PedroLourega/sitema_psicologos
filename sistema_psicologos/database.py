import sqlite3
from datetime import datetime

def init_db():
    """Inicializa o banco de dados com as tabelas necessárias"""
    conn = sqlite3.connect('connect_psicologos.db')
    cursor = conn.cursor()
    
    # Tabela de psicólogos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS psicologos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Tabela de pacientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            data_nascimento DATE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Tabela de consultas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER NOT NULL,
            psicologo_id INTEGER NOT NULL,
            data_consulta DATE NOT NULL,
            horario TIME NOT NULL,
            status TEXT DEFAULT 'agendada',
            FOREIGN KEY (paciente_id) REFERENCES pacientes (id),
            FOREIGN KEY (psicologo_id) REFERENCES psicologos (id)
        )
    ''')
    
    # Inserir psicólogos padrão se não existirem
    cursor.execute('SELECT COUNT(*) FROM psicologos')
    if cursor.fetchone()[0] == 0:
        psicologos_padrao = [
            ('Afonso Silva', 'Psicanálise: trabalha questões profundas como traumas, identidade e relações.', 'afonso.silva', 'psico123'),
            ('Cleber Rodrigues', 'Psicologia do Trabalho: foco em estresse, carreira e ambiente profissional.', 'cleber.rodrigues', 'psico123'),
            ('Fernanda Ribas', 'Psicologia Clínica: atua com ansiedade, autoestima e acolhimento emocional.', 'fernanda.ribas', 'psico123'),
            ('Marcelo Alcantra', 'Terapia Cognitivo-Comportamental: foco em depressão, ansiedade e autoconhecimento.', 'marcelo.alcantra', 'psico123'),
            ('Vera Maia', 'Psicologia Infantil: especialista em desenvolvimento, vínculos familiares e escola.', 'vera.maia', 'psico123')
        ]
        
        cursor.executemany('''
            INSERT INTO psicologos (nome, especialidade, username, password)
            VALUES (?, ?, ?, ?)
        ''', psicologos_padrao)
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Retorna uma conexão com o banco de dados"""
    conn = sqlite3.connect('connect_psicologos.db')
    conn.row_factory = sqlite3.Row
    return conn

def verificar_login_psicologo(username, password):
    """Verifica se o login do psicólogo é válido"""
    conn = get_db_connection()
    psicologo = conn.execute(
        'SELECT * FROM psicologos WHERE username = ? AND password = ?',
        (username, password)
    ).fetchone()
    conn.close()
    return psicologo

def verificar_login_paciente(username, password):
    """Verifica se o login do paciente é válido"""
    conn = get_db_connection()
    paciente = conn.execute(
        'SELECT * FROM pacientes WHERE username = ? AND password = ?',
        (username, password)
    ).fetchone()
    conn.close()
    return paciente

def listar_consultas():
    """Lista todas as consultas com informações do paciente e psicólogo"""
    conn = get_db_connection()
    consultas = conn.execute('''
        SELECT c.id, c.data_consulta, c.horario, c.status,
               p.nome as paciente_nome, p.cpf, p.data_nascimento, p.id as paciente_id,
               ps.nome as psicologo_nome
        FROM consultas c
        JOIN pacientes p ON c.paciente_id = p.id
        JOIN psicologos ps ON c.psicologo_id = ps.id
        ORDER BY c.data_consulta, c.horario
    ''').fetchall()
    conn.close()
    return consultas

def listar_psicologos():
    """Lista todos os psicólogos"""
    conn = get_db_connection()
    psicologos = conn.execute('SELECT * FROM psicologos ORDER BY nome').fetchall()
    conn.close()
    return psicologos

def criar_paciente(nome, cpf, data_nascimento, username, password):
    """Cria um novo paciente"""
    conn = get_db_connection()
    try:
        conn.execute('''
            INSERT INTO pacientes (nome, cpf, data_nascimento, username, password)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, cpf, data_nascimento, username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def agendar_consulta(paciente_id, psicologo_id, data_consulta, horario):
    """Agenda uma nova consulta"""
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO consultas (paciente_id, psicologo_id, data_consulta, horario)
        VALUES (?, ?, ?, ?)
    ''', (paciente_id, psicologo_id, data_consulta, horario))
    conn.commit()
    conn.close()

def listar_pacientes():
    """Lista todos os pacientes"""
    conn = get_db_connection()
    pacientes = conn.execute('SELECT * FROM pacientes ORDER BY nome').fetchall()
    conn.close()
    return pacientes

def consultas_paciente(paciente_id):
    """Lista consultas de um paciente específico"""
    conn = get_db_connection()
    consultas = conn.execute('''
        SELECT c.data_consulta, c.horario, c.status,
               ps.nome as psicologo_nome, ps.especialidade
        FROM consultas c
        JOIN psicologos ps ON c.psicologo_id = ps.id
        WHERE c.paciente_id = ?
        ORDER BY c.data_consulta, c.horario
    ''', (paciente_id,)).fetchall()
    conn.close()
    return consultas