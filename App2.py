from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacoes('Gui', 4)
restaurante_praca.receber_avaliacoes('Emanuel', 5)
restaurante_praca.receber_avaliacoes('Kaylane', 1)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()