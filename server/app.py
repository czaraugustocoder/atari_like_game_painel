from flask import Flask
from flask import render_template, request, redirect, url_for, session
from markupsafe import escape
from sheetconn import SheetConn

app = Flask(__name__)

app.secret_key = "123456"

users = [
    {
        'name' : "pablo",
        'email' : "pablo@gmail.com",
        "pwd" : "123456"
    },
    {
        'name' : "nuchy",
        'email' : "nucky@gmail.com",
        "pwd" : "654321"
    }
]

print(users)

name_auth_true = True
name_auth_false = False

# painel do usuário

@app.route("/painel/<user>")
def index(user):
    
    if (user in session["user"]):
        return render_template("index.html", user = session["user"])
    
    if (user not in session["user"]):
        return redirect(url_for('login'))

# login

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        name_auth = request.form['name']
        print(name_auth)
        pwd = request.form['password']
        print(pwd)

        user_cred = SheetConn('USUARIOS').takeuser(name_auth)

        if (len(user_cred) > 0):
            if ((str(user_cred[0]) == name_auth) and (str(user_cred[1]) == pwd)):
                print("autenticado")
                session["user"] = name_auth
                print(session)
                print(session["user"])
                return redirect(url_for('index', user = session["user"]))
            else:
                print("não autenticado")    

        print("usuario não ncontrado")
        return render_template("login.html", attempt = name_auth_true)

    return render_template("login.html", attempt = name_auth_false)

#labirinto

@app.route("/labirinto")
def labirinto():
    return redirect(url_for('labirinto_user', user = session["user"]))


#labirinto/user

@app.route("/labirinto/<user>")
def labirinto_user(user):

    if (user in session["user"]):
        return render_template("labirinto.html")
    

    if (user not in session["user"]):
        return redirect(url_for('login'))

# inserção de um novo usuario

@app.route("/cadastrar", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user_info = [name, email, pwd]

        user_cred = SheetConn('USUARIOS').takeuser(name)

        if (len(user_cred) > 0):
            mensagem = "usuário já existe, escolha outro"
            return render_template("register.html", attempt = name_auth_true, msg = mensagem)

        SheetConn('USUARIOS').insertuser(user_info)

        mensagem = "usuário cadastrado com sucesso, faça login"

        return render_template("register.html", attempt = name_auth_true, msg = mensagem)
    
    return render_template("register.html", attempt = name_auth_false)

# consulta de todos os usuarios

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", users=users)

# consulta de apenas 1 usuarios

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    print(username)
    for a in users:
        if a['name'] == username:
            return 'User %s' % escape(username)
        
    return '<p>Usuario não encontrado</p>'


# edição do nome de um usuario

@app.route('/edit/user/<username>/<nusername>')
def edit_user_profile(username, nusername):
    # show the user profile for that user

    print(username)
    for a in users:
        if a['name'] == username:
            for b in users:
                if b['name'] == nusername:
                    return '<p>Usuario já existe, escolha outro</p>'
                
            print(a['name'])    
            a['name'] = nusername   
            return 'New User %s' % escape(nusername)
        
    return '<p>Usuario não encontrado</p>'


# deletando um usuario

@app.route('/delete/user/<username>')
def delete_user_profile(username):
    # show the user profile for that user

    print(username)
    count = 0
    for a in users:
        if a['name'] == username:
            del users[count]
            return '<p>Usuario deletado</p>'
        count += 1
        print(count)
    count = 0
        
    return '<p>Usuario não encontrado</p>'


if __name__ == '__main__':
    app.run(debug=True)