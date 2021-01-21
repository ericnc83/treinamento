from flask import Flask, jsonify, request
import sqlite3


app = Flask(__name__)

conn = sqlite3.connect('database.db')
print ("Banco de dados aberto com sucesso!")

conn.execute('CREATE TABLE IF NOT EXISTS obras (titulo TEXT, editora TEXT, foto TEXT, autor TEXT)')
conn.commit()
print ("Tabela criada com sucesso!")
conn.close()

obras = [
    {
        "titulo":"O Silmarillion",
        "editora":"HarperCollins",
        "foto":"https://images-na.ssl-images-amazon.com/images/I/51aEcyyb3xL._SX331_BO1,204,203,200_.jpg",
        "autor":"J. R. R. Tolkien"
    },
    {
        "titulo":"Cem sonetos de amor",
        "editora":"L&PM",
        "foto":"https://images-na.ssl-images-amazon.com/images/I/41F27-HPN4L._SX297_BO1,204,203,200_.jpg",
        "autor":"Pablo Neruda"
    },
    {
        "titulo":"Poemas de Alvaro de Campos",
        "editora":"L&PM",
        "foto":"https://images-na.ssl-images-amazon.com/images/I/41s-htM5VwL._SX299_BO1,204,203,200_.jpg",
        "autor":"Fernando Pessoa"
    }
]

for dados in obras:
    
    conn = sqlite3.connect('database.db')
    print ("Banco de dados aberto com sucesso!")
    insert = f'INSERT INTO obras (titulo, editora, foto, autor) VALUES ("{dados.get("titulo")}", "{dados.get("editora")}", "{dados.get("foto")}", "{dados.get("autor")}")' # .get mesma coisa que {dados["titulo"]}
    print(insert)
    conn.execute(insert)
    conn.commit() 
    print ("Dados adicionados com sucesso!")
    conn.close()

@app.route("/obras", methods=["GET"])
def home():
    return jsonify(obras), 200


@app.route("/obras", methods=['POST'])
def add():
    titulo = request.args.get('titulo')
    autor = request.args.get('autor')
    editora = request.args.get('editora')
    obras.append({'titulo':titulo,'autor': autor, 'editora': editora})
    return "Obra adicionada com sucesso!", 200


if __name__ == "__main__":
    app.run(debug=True)



