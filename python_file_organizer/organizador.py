import os
import shutil

# Lista todos os arquivos e pastas dentro do caminho
def organizar_por_extensao(caminho):
    for item in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, item)

        # Organizar apenas arquivos (não pastas)
        if os.path.isfile(caminho_completo):
            # Separa nome e extensão
            nome_arquivo, extensao = os.path.splitext(item)

            # Remove o ponto da extensão e coloca em maiúsculo (ex: ".pdf" -> "PDF")
            extensao = extensao[1:].upper()

            # Previne mover um arquivo sem extensão
            if extensao:
                pasta_destino = os.path.join(caminho, extensao)

                # Cria a pasta da extensão se não existir
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                # Move o arquivo para a pasta da extensão
                novo_caminho = os.path.join(pasta_destino, item)
                shutil.move(caminho_completo, novo_caminho)
                print(f"Movido: {item} -> {pasta_destino}")