from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao 

    def __str__(self):
        return f'{self.nome}'

    def aplicar_desconto(self):
            """Aplica um desconto de 10% no preço da bebida."""
            self._preco -= (self._preco * 0.10)