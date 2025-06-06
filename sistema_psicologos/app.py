from flask import Flask, render_template #Importa a classe Flask

app = Flask(__name__) #cria uma instância do Flask

#Cria uma URL para a página principal do site
@app.route('/')
def home():
    return render_template('index.html')

#garante que o app só será executado se este arquivo for rodado diretamente
if __name__ == '__main__':
    app.run(debug=True)  #Inicia o servidor Flask em modo debug