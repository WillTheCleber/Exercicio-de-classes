from classe_estoque_livro import estoqueLivro
from classe_cliente import clientes
#Aqui to importando as duas classes pq aqui vou precisar dos dados do cliente e do nivel de estoque


class locadora(estoqueLivro, clientes):
    def __init__(self, nomeLivro, quantidadeEstoque, autor, preco):
        super().__init__(nomeLivro, quantidadeEstoque, autor, preco)
        super().__init__()