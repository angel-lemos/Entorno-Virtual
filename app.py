from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')

@app.route('/lista_clientes')
def lista_clientes():
    clientes = [
        {'nombre':"Juan Perez",'DNI':'3.333.333-1'},
        {'nombre':"José Lopez",'DNI':'4.444.444-2'},
        {'nombre':"Luisa Mieres",'DNI':'5.555.555-3'}
    ]
    return render_template('lista_clientes.html', Clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)