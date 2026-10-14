from  modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self,nome,preco,tamanho):
       super().__init__(nome,preco)
       self.tamanho = tamanho

    def __str__(self):
        return f'{self.nome} - {self.tamanho}'

    def aplicar_desconto(self):
        """Aplica um desconto de 10% no preço da bebida."""
        self._preco -= (self._preco * 0.10)