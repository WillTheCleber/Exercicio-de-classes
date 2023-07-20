#Aqui fica a classe principal do meu exercicio:


#Vou começar criando uma classe cliente que ira recer os atributos preço nome cpf e contato, não consigo imaginar mais o que colocar aqui.

# from classe_cliente import datetime


from classe_estoque_livro import estoqueLivro
#Importei a classe do estoque para saber quais livros o cliente tem alugado

class clientes(estoqueLivro):
    

    def __init__(self, nome, preco,quantidade,cpf,contato, nomeLivro):
        self.nome= nome
        self.preco= preco
        self.quantidade= quantidade
        self.__cpf= cpf
        self._contato = contato
        super().__init__(nomeLivro)



        
