from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para sessões

db = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=logn;"
    "Trusted_Connection=logn;"
)

@app.route("/")
def homepage():
    return render_template("login.html")  

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        senha_hash = generate_password_hash(senha)  # Criptografa a senha

        cursor = db.cursor()

        # Verifica se o email já existe
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
        if cursor.fetchone():
            flash("Este e-mail já está cadastrado!")
            return redirect(url_for("cadastro"))

        # Insere novo usuário no banco
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (%s, %s)", (email, senha_hash))
        db.commit()

        flash("Cadastro realizado com sucesso! Faça login.")
        return redirect(url_for("homepage"))

    return render_template("cadastro.html")

@app.route("/home")
def aposlogin():
    if 'user' in session:
        return render_template("home.html", user=session['user'])
    else:
        flash("Faça login para acessar esta página.")
        return redirect(url_for("homepage"))

# Rota para processar login
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    cursor = db.cursor()
    cursor.execute("SELECT id, email, senha FROM usuarios WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and check_password_hash(user[2], senha):  # Verifica senha com hash
        session["user"] = user[1]  # Armazena na sessão
        flash("Login bem-sucedido!")
        return redirect(url_for("aposlogin"))
    else:
        flash("Email ou senha incorretos!")
        return redirect(url_for("homepage"))

# Rota para logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Você saiu da conta.")
    return redirect(url_for("homepage"))

if __name__ == "__main__":
    app.run(debug=True)
