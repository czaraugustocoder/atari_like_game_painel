import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


class SheetConn:

    def __init__(self, sheet):
        self.jsonkey = r'/home/czaraugusto/python_files/games_blackboard/server/database-backend-game-project-9018e6c2f3f1.json'
        self.idsheet = '1QTTJU_mhSUFJ8rbnmej_xfX4cfJK0WXlk84HWjI4tyw'
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
    
    def insertuser(self, data):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.jsonkey, scope)

        gc = gspread.authorize(credentials)

        wks = gc.open_by_key(self.idsheet).worksheet(self.sheet)

        wks.append_row(data)

    def timeuser(self, usuario, tempo):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.jsonkey, scope)

        gc = gspread.authorize(credentials)

        wks = gc.open_by_key(self.idsheet).worksheet(self.sheet)

        celula = wks.find(usuario)
        print(celula)
        if celula:
            name_usuario = usuario
            linha = celula.row
            print(f'A chave {name_usuario} está na linha: {linha}')
            coluna_linha = f'B{linha}'
            wks.update_acell(coluna_linha, tempo)

        return celula
    
    def timeusers(self):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.jsonkey, scope)

        gc = gspread.authorize(credentials)

        wks = gc.open_by_key(self.idsheet).worksheet(self.sheet)

        dados = wks.get_all_values()

        colunas = dados[0]

        linhas = dados[1:]

        users = pd.DataFrame(linhas, columns=colunas)

        users = users.loc[users['TEMPO'] != ""]

        users = users.sort_values(by=['TEMPO'],ascending=True)

        usuarios = users['USUARIO'].tolist()
        tempo = users['TEMPO'].tolist()

        users_dic = {"USUARIOS":usuarios, "TEMPO": tempo}

        return users_dic