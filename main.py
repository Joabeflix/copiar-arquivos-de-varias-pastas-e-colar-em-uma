import shutil
import os
import time

def copiar():

    os.chdir(r'pastas')
    local = os.getcwd()
    print(f'Aqui é o local {local}')
    for pasta in os.listdir():
        
        os.chdir(rf'{local}\{pasta}')

        for arquivo in os.listdir():
            caminho_origem = rf'{local}\{pasta}\{arquivo}'
            caminho_destino = r'C:\Users\joab.alves\Desktop\Programas Ecommerce\copiar arquivos de varias pastas e colar em uma\arquivos_juntos'

            shutil.copy(caminho_origem, caminho_destino)
        print(f'Pasta copiada com sucesso: {pasta}')
        time.sleep(1)

copiar()
