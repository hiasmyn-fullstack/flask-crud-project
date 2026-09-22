from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

# ========== BANCO DE DADOS ==========
def create_database():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT
        )
    """)
    
    conexao.commit()
    conexao.close()

create_database()

# ========== PÁGINA INICIAL — SUAS EXPLICAÇÕES ==========
@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PROGRAMAÇÃO DE FORMA SIMPLES</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-4">
    <h1 class="text-center text-primary display-4">Explicando a programação de maneira simples</h1>
    <hr class="my-4">
    
    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Sou uma iniciante em programação, estou estudando para me tornar uma dev em backend, através deste site vim explicar alguns conceitos básicos e esclarecer algumas coisas e dúvidas frequentes...vamos lá?</p>
    <p>As pessoas costumam acreditar que a programação envolve inglês e matemática, porém é aí onde se enganam...não vou dizer que não existe inglês na programação, pois as variáveis e comandos são escritos em inglês, entretanto não é nada assustador e difícil de se aprender e memorizar, referente a matemática...não é necessário ser bom em matemática. A programação envolve lógica e nosso objetivo é resolver problemas com essa lógica e comandos dependendo da linguagem, então sim é um mito ser necessário ter inglês e matemática para esse aprendizado.</p>
    </div>
    
    <h4 class="text-dark mb-3">Conceitos Básicos:</h4>
    <ul class="list-group mb-4">
    <li class="list-group-item"><a href="/logica" class="text-decoration-none">Lógica de Programação</a></li>
    <li class="list-group-item"><a href="/variaveis" class="text-decoration-none">Variáveis</a></li>
    <li class="list-group-item"><a href="/funcoes" class="text-decoration-none">Funções</a></li>
    <li class="list-group-item"><a href="/poo" class="text-decoration-none">POO</a></li>
    <li class="list-group-item"><a href="/bancodedados" class="text-decoration-none">Banco de dados</a></li>
    <li class="list-group-item"><a href="/framework" class="text-decoration-none">Framework</a></li>
    <li class="list-group-item"><a href="/produtos" class="text-decoration-none">📦 Produtos — CRUD</a></li>
    </ul>
  </div>
</body>
</html>
    """

# ========== PÁGINAS DE CONCEITOS ==========
@app.route("/logica")
def logica():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LÓGICA DE PROGRAMAÇÃO</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container p-4">
    <h1 class="text-center text-primary display-4">Lógica de programação</h1>
    <hr class="my-4">
    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">A lógica de programação é a técnica de organizar o pensamento em uma sequência clara, lógica e ordenada de passos para resolver um problema que o computador consegue executar.</p>
    </div>
    <h5>Exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
numero = int(input("Digite um número:"))
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
    </pre>
    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>
  </div>
</body>
</html>
    """

@app.route("/variaveis")
def variaveis():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VARIÁVEIS</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container p-4">
    <h1 class="text-center text-primary display-4">Variáveis</h1>
    <hr class="my-4">
    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Uma variável é um espaço na memória para guardar um valor que pode mudar.</p>
    </div>
    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
nome = "Maria"
idade = 17
    </pre>
    <br>
    <a href="/" class="btn btn-primary">Volte a Página inicial</a>
  </div>
</body>
</html>
    """

@app.route("/funcoes")
def funcoes():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FUNÇÕES</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-4">
    <h1 class="text-center text-primary display-4">Funções</h1>
    <hr class="my-4">
    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Uma função é um bloco de código reutilizável projetado para realizar uma tarefa específica.</p>
    </div>
    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))
    </pre>
    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>
  </div>
</body>
</html>
    """

@app.route("/poo")
def poo():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>POO</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container p-4">
    <h1 class="text-center text-primary display-4">POO</h1>
    <hr class="my-4">
    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">A Programação Orientada a Objetos organiza o código em Classes e Objetos.</p>
    </div>
    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
        print(f"O {self.modelo} está ligado.")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.ligar()
    </pre>
    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>
  </div>
</body>
</html>
    """

@app.route("/bancodedados")
def bancodedados():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BANCO DE DADOS</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container p-4">
    <h1 class="text-center text-primary display-4">Banco de dados</h1>
    <hr class="my-4">
    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Bancos de dados guardam informações para usar depois.</p>
    </div>
    <h5>Por exemplo:</h5>
    <pre class="bg-light p-3 rounded border">
import sqlite3
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, idade INTEGER)")
cursor.execute("INSERT INTO usuarios VALUES ('Ana', 25)")
conexao.commit()
conexao.close()
    </pre>
    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>
  </div>
</body>
</html>
    """

@app.route("/framework")
def framework():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FRAMEWORK</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container p-4">
    <h1 class="text-center text-primary display-4">Framework</h1>
    <hr class="my-4">
    <div class="card p-4 shadow-sm mb-4">
    <p class="lead">Framework = ferramentas prontas para acelerar o trabalho.</p>
    </div>
    <h5>Exemplos:</h5>
    <pre class="bg-light p-3 rounded border">
Flask   → Sites web
Django  → Sites mais completos
FastAPI → Criar APIs
    </pre>
    <br>
    <a href="/" class="btn btn-primary">Volte a página inicial</a>
  </div>
</body>
</html>
    """

# ========== CRUD COMPLETO — O QUE CONSTRUÍMOS ==========

# READ — Listar todos
@app.route("/produtos")
def produtos():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    
    # Cadastra exemplos se estiver vazio
    cursor.execute("SELECT * FROM produtos")
    if not cursor.fetchall():
        cursor.execute("INSERT INTO produtos (nome, descricao) VALUES (?, ?)",
                      ('Flask', 'Framework para sites em Python'))
        cursor.execute("INSERT INTO produtos (nome, descricao) VALUES (?, ?)",
                      ('SQLite', 'Banco leve que já vem no Python'))
    
    cursor.execute("SELECT * FROM produtos")
    lista = cursor.fetchall()
    conexao.close()
    
    html_inicio = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PRODUTOS</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-4">
    <h1 class="text-center text-primary display-5">📦 Lista de Produtos</h1>
    <hr class="my-4">
    <a href="/novo" class="btn btn-success mb-3">➕ Cadastrar Novo</a>
    
    <table class="table table-striped table-bordered">
    <thead class="table-dark">
    <tr>
        <th>ID</th>
        <th>Nome</th>
        <th>Descrição</th>
        <th>Ações</th>
    </tr>
    </thead>
    <tbody>
    """
    html_linhas = ""
    for item in lista:
        html_linhas += f"""
        <tr>
            <td>{item[0]}</td>
            <td>{item[1]}</td>
            <td>{item[2]}</td>
            <td>
                <a href="/editar/{item[0]}" class="btn btn-sm btn-warning">✏️ Editar</a>
                <a href="/excluir/{item[0]}" class="btn btn-sm btn-danger" onclick="return confirm('Tem certeza?')">🗑️ Excluir</a>
            </td>
        </tr>
        """
    html_fim = """
    </tbody>
    </table>
    <a href="/" class="btn btn-secondary">← Voltar</a>
    </div>
</body>
</html>
    """
    return html_inicio + html_linhas + html_fim

# CREATE — Formulário novo
@app.route("/novo")
def novo():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CADASTRAR PRODUTO</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-4">
    <h1 class="text-center text-success display-5">➕ Cadastrar Produto</h1>
    <hr class="my-4">
    <div class="card p-4 shadow-sm">
    <form action="/cadastrar" method="POST">
        <div class="mb-3">
            <label class="form-label">Nome:</label>
            <input type="text" name="nome" class="form-control" required>
        </div>
        <div class="mb-3">
            <label class="form-label">Descrição:</label>
            <textarea name="descricao" class="form-control" rows="3"></textarea>
        </div>
        <button type="submit" class="btn btn-success">Salvar</button>
        <a href="/produtos" class="btn btn-secondary">Cancelar</a>
    </form>
    </div>
  </div>
</body>
</html>
    """

# CREATE — Salvar no banco
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (nome, descricao) VALUES (?, ?)",
                  (nome, descricao))
    conexao.commit()
    conexao.close()
    
    return redirect("/produtos")

# UPDATE — Formulário editar
@app.route("/editar/<int:id>")
def editar(id):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produto = cursor.fetchone()
    conexao.close()
    
    return f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-4">
    <h1 class="text-center text-warning display-5">✏️ Editar Produto</h1>
    <hr class="my-4">
    <div class="card p-4 shadow-sm">
    <form action="/atualizar/{id}" method="POST">
        <div class="mb-3">
            <label class="form-label">Nome:</label>
            <input type="text" name="nome" class="form-control" value="{produto[1]}" required>
        </div>
        <div class="mb-3">
            <label class="form-label">Descrição:</label>
            <textarea name="descricao" class="form-control" rows="3">{produto[2]}</textarea>
        </div>
        <button type="submit" class="btn btn-warning">Atualizar</button>
        <a href="/produtos" class="btn btn-secondary">Cancelar</a>
    </form>
    </div>
  </div>
</body>
</html>
    """

# UPDATE — Salvar alteração
@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE produtos SET nome = ?, descricao = ? WHERE id = ?",
                  (nome, descricao, id))
    conexao.commit()
    conexao.close()
    
    return redirect("/produtos")

# DELETE — Excluir
@app.route("/excluir/<int:id>")
def excluir(id):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    
    return redirect("/produtos")

if __name__ == '__main__':
    app.run(debug=True)