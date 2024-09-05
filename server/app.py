from flask import Flask
from flask import render_template, request
from markupsafe import escape

app = Flask(__name__)

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



# inserção de um novo usuario

@app.route("/", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        for a in users:
            if a['name'] == name:
                    return '<p>Usuario já existe, escolha outro</p>'

        users.append(
            {
            'name' : name,
            'email' : email,
            "pwd" : pwd
            }
        )

        return "você foi registrado com o nome: "+name
    
    return render_template("register.html")

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




@app.route("/labirinto")
def labirinto():
    return render_template("labirinto.html")