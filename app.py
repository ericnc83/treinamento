from flask import Flask, jsonify, request

app = Flask(__name__)

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


