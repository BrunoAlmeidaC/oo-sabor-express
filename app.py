from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 5)
restaurante_praca.receber_avaliacao('Lais', 4)
restaurante_praca.receber_avaliacao('Bruno', 2)

def main():
    Restaurante.listar_restaurantes()

restaurante_praca.alternar_estado()

if __name__ == '__main__':
    main()