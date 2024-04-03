#En proramación estructurada con solo variables
cel1_brand = "samsung"
cel2_brand = "apple"
cel3_brand = "huawei"

cel1_modelo = "S23"
cel1_modelo = "S23"
cel1_modelo = "S23"

#En programción orientada a objetos
class Celular:
    def __init__(self, brand, sistema_operativo, modelo):
        self.marca = brand
        self.modelo = modelo
        self.sistema_op = sistema_operativo

    def llamr(self):
        print('Ring, ring... ring ¡ring!')


class VideoJuegoDisponibleEnCelular(Celular):
    def __init__ (self, brand, sistema_operativo, modelo, juego):
        super().__init__(brand, sistema_operativo, modelo)
        self.juego = juego


phone = Celular("oppo", "iOS", "A53")

alto_game = VideoJuegoDisponibleEnCelular("Samsung", "Android", "C32", "Alto")

print(f'Marca: {phone.marca}    Sistema operativo: {phone.sistema_op}   Modelo: {phone.modelo}')
print(f"""
        Videjuego: {alto_game.juego}
        Disponible en: {alto_game.sistema_op}

        """)