from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    """Classe base para os itens do cardápio (bebidas, pratos e sobremesas)."""

    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass
