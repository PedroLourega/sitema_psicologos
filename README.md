# 🧠 Connect Psicologos

Sistema web desenvolvido como trabalho da disciplina **Usabilidade, Desenvolvimento Web, Mobile e Jogos**, no curso de Análise e Desenvolvimento de Sistemas (Junho de 2025).

---

## 💡 Sobre o Projeto

**PsicoConnect** é uma aplicação web voltada para atendimentos psicológicos online em todo o Brasil.  
A aplicação simula o funcionamento de uma empresa fictícia chamada **Connect Psicólogos**, especializada em consultas remotas (home office), oferecendo praticidade e conectividade entre pacientes e profissionais da psicologia.

---

## 🛠 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 🌐 Funcionalidades

### 🔵 Landing Page
- Página inicial com apresentação da empresa fictícia.

### 🔐 Sistema de Acesso
- Tela de login com duas opções de acesso:
  - 👨‍⚕️ **Psicólogo**
  - 👤 **Paciente**

### 👩‍⚕️ Área do Psicólogo
- ✅ Adicionar novos pacientes
- 🗓️ Agendar consultas (data, horário e profissional)
- 📋 Visualizar consultas agendadas  
*(🔒 Ainda não foi implementada a opção de remover pacientes)*

### 🧍 Área do Paciente
- 🔐 Login com credenciais fornecidas pelo psicólogo
- 📅 Visualização de consultas:
  - Data
  - Horário
  - Nome do profissional responsável

---

## 📱 Responsividade

A aplicação foi desenvolvida com foco em **usabilidade** e **responsividade**, garantindo uma navegação fluida e agradável tanto no desktop quanto no mobile.

---

## 🚀 Como Rodar o Projeto

```bash
# 1. Clone este repositório
git clone https://github.com/PedroLourega/psicoconnect.git
cd psicoconnect

# 2. Crie e ative um ambiente virtual(Opcional) 
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

# 3. Instale as dependências
pip install flask

# 4. Inicie o servidor Flask
python app.py
```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

---

## 📌 Observações

- 🎓 Projeto com fins educacionais
- 🔧 Futuras melhorias:
  - Edição e remoção de pacientes
  - Envio de notificações por e-mail
  - Integração com APIs externas
  - Autenticação segura com tokens

---

## 👨‍💻 Autor <br>

**Pedro Henrique Lourega Rodrigues**  <br>
Estudante de Análise e Desenvolvimento de Sistemas  <br>
GitHub: [@PedroLourega](https://github.com/PedroLourega) <br>

