class Produto:
    def __init__(self, codigo, nome, descricao, categoria, preco, estoque, perecivel):
        if type(codigo) != int or codigo <= 0:
            raise ValueError("Código Inválido")
        if type(nome) != str or len(nome) < 2:
            raise ValueError("Nome Inválido")
        if type(preco) != float or preco <= 0:
            raise ValueError("Preço Inválido")
        if type(preco) != float or preco <= 0:
            raise ValueError("Preço Inválido")
        if type(categoria) != str or categoria not in ["Frutas", "Eletrônicos", "Roupas", "Bebidas"]:
            raise ValueError("Categoria Inválida")
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.perecivel = perecivel

    def reajustar_preco(self, percentual):
        if percentual <= 0:
            raise ValueError("Percentual Inválido")
        self.preco = self.preco * (1 + percentual/100)