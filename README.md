# Sabor Express — Orientação a Objetos em Python

Projeto de estudo feito durante o curso de Python e Orientação a Objetos da Alura. Ele modela um sistema simples de restaurantes, com avaliações de clientes e um cardápio com bebidas, pratos e sobremesas.

## Conceitos praticados

- **Classes e objetos**: `Restaurante`, `Avaliacao` e os itens do cardápio
- **Encapsulamento**: atributos "protegidos" (`_nome`, `_preco`) expostos com `@property`
- **Atributos e métodos de classe**: lista `restaurantes` e `@classmethod listar_restaurantes()`
- **Herança**: `Bebida`, `Prato` e `Sobremesa` herdam de `ItemCardapio`
- **Classe abstrata e polimorfismo**: `ItemCardapio` herda de `ABC` e cada item implementa seu próprio `aplicar_desconto()`
- **Validação de dados**: notas de avaliação só são aceitas entre 1 e 5

## Estrutura

```
oo-sabor-express/
├── app.py                  # ponto de entrada
└── modelos/
    ├── restaurante.py      # classe Restaurante
    ├── avaliacao.py        # classe Avaliacao
    └── cardapio/
        ├── item_cardapio.py  # classe base abstrata
        ├── bebida.py         # 10% de desconto
        ├── prato.py          # 10% de desconto
        └── sobremesa.py      # 15% de desconto
```

## Como rodar

Requer Python 3.

```bash
git clone https://github.com/DaviHonorioDEV/oo-sabor-express.git
cd oo-sabor-express
python3 app.py
```

Saída esperada:

```
Cardápio do Restaurante Praça

1. Nome: suco de laranja | Preço: R$3.6 | Tamanho: grande
2. Nome: pãozinho | Preço: R$1.8 | Descrição: um pãozinho fresquinho
```

## Autor

Davi Ricardo Patrício Cunha — [GitHub](https://github.com/DaviHonorioDEV)
