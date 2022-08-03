import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

def lista_arquivos():
        
        path = "C:\\Users\\fflose\\Lab\\Pessoal\\python\csv\\teste_internet\\"
        ListaArquivos = os.listdir(path)
        return list(ListaArquivos)

for upload_file in lista_arquivos():
	gfile = drive.ListFile(upload_file)
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.