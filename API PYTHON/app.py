from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R.Tolkien'},
    {'id': 2, 'titulo': '1984', 'autor': 'George Orwell'},
    {'id': 3, 'titulo': 'Cem Anos de Solidão', 'autor': 'Gabriel García Márquez'}
]

@app.route('/livros', methods=['GET'])
def Obter_Livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def Obter_Livro_ID(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

@app.route('/livros/<int:id>', methods=['PUT'])
def Editar_Livro_Por_ID(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

@app.route('/livros', methods=['POST'])
def Incluir_Novo_Livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201  
   

@app.route('/livros/<int:id>', methods=['DELETE'])
def Excluir_Livro_ID(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
