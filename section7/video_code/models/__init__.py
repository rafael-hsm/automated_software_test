import sys
from pathlib import Path

# Cria um objeto Path chamado file que representa o caminho absoluto para o arquivo que contém este código. __file__ é uma variável especial em Python que se refere ao nome do arquivo atual.
file = Path(__file__).resolve()

# Usa o método parent para obter o diretório pai do arquivo (ou seja, o diretório que contém o arquivo). file.parents[1] obtém o diretório pai do diretório pai, que é o diretório raiz do projeto.
parent, root = file.parent, file.parents[1]

# Converte o caminho do diretório raiz para uma string e o adiciona à lista sys.path. Isso tem o efeito de adicionar o diretório raiz ao caminho de pesquisa do Python, permitindo que você importe módulos desse diretório em seu código sem a necessidade de usar caminhos absolutos.
sys.path.append(str(root))