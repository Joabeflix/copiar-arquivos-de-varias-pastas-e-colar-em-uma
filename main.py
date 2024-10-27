import shutil
import os
import time

local_raiz = os.getcwd()

def copiar():
    os.chdir(r'pastas')
    local = os.getcwd()
    
    for pasta in os.listdir():
        os.chdir(rf'{local}\{pasta}')

        for arquivo in os.listdir():
            caminho_origem = rf'{local}\{pasta}\{arquivo}'
            caminho_destino = rf'{local_raiz}\output'

            shutil.copy(caminho_origem, caminho_destino)
        print(f'Pasta copiada com sucesso: {pasta}')
        time.sleep(1)

copiar()
