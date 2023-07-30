import os
import random
import string

def gerar_nome_aleatorio(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def renomear_arquivos_na_pasta(pasta_alvo):
    if not os.path.exists(pasta_alvo):
        print("A pasta nao existe")
        return

    for nome_arquivo in os.listdir(pasta_alvo):
        caminho_completo = os.path.join(pasta_alvo, nome_arquivo)
        
        if os.path.isfile(caminho_completo):
            nome, extensao = os.path.splitext(nome_arquivo)
            novo_nome = gerar_nome_aleatorio() + extensao
            novo_caminho_completo = os.path.join(pasta_alvo, novo_nome)

            # Evita possiveis colisoes de nome, caso ja exista um arquivo com o mesmo nome gerado
            while os.path.exists(novo_caminho_completo):
                novo_nome = gerar_nome_aleatorio() + extensao
                novo_caminho_completo = os.path.join(pasta_alvo, novo_nome)

            os.rename(caminho_completo, novo_caminho_completo)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Digite os nomes das pastas como argumentos separados por espaço")
    else:
        for pasta_alvo in sys.argv[1:]:
            renomear_arquivos_na_pasta(pasta_alvo)
