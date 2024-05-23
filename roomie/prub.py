class cartas:
    def __init__(self, valor, color, orden):
        self.valor = valor
        self.color = color
        self.orden = orden #***

    def p_mazo(self, orden):
        self.orden = orden

    def p_carta(self):
        if (self.valor == 0):
            x = "Comodín 🤡"
        else:
            x = self.valor
        print(f"Valor: {x}, Color: {self.color}, Numero visible x ahora xD: {self.orden}\n")

    def carta_archivo(self):
        x = f"${self.valor} /{self.color} @{self.orden}"
        return(x)
carta1 = cartas(1, "rojo", 1)
carta1.p_carta()