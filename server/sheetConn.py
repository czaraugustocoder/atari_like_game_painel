import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SheetConn:

    def __init__(self, jsonkey, idsheet, sheet):
        self.jsonkey = jsonkey
        self.idsheet = idsheet
        self.sheet = sheet
        
    def takeuser(self, usuario):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.jsonkey, scope)

        gc = gspread.authorize(credentials)

        wks = gc.open_by_key(self.idsheet).worksheet(self.sheet)

        user_credentials = []

        celula = wks.find(usuario)
        print(celula)
        if celula:
            name_usuario = usuario
            linha = celula.row
            print(f'A chave {name_usuario} está na linha: {linha}')
            user_credentials.append(name_usuario)
            coluna = 3
            senha = wks.cell(linha, coluna).value
            print(senha)
            user_credentials.append(senha)

        return user_credentials
    
user = SheetConn(r'/home/czaraugusto/python_files/games_blackboard/server/database-backend-game-project-9018e6c2f3f1.json', 
          '1QTTJU_mhSUFJ8rbnmej_xfX4cfJK0WXlk84HWjI4tyw',
          'USUARIOS').takeuser('cesar')

print(user)