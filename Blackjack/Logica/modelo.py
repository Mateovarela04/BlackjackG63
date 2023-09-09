class Carta:

    def __init__(self, pinta: str, valor: str):
        self.pinta = pinta
        self.valor = valor
        self.tapada = False


class Mano:

    def __init__(self, cartas):
        self.cartas = list(cartas)

    def es_blackjack(self):
        pass


class Baraja:

    def __init__(self):
        self.cartas = []

    def revolver(self):
        pass

    def repartir_carta(self):
        pass


class Jugador:

    def __init__(self, nombre: str, fichas: int):
        self.nombre = nombre
        self.fichas = fichas
        self.mano = None

    def inicializador_mano(self, cartas):
        pass


class Blackjack:

    def __init__(self):
        self.jugador = None
        self.cupier = None
        self.baraja = None

    def registrar_jugador(self, nombre: str):
        pass

    def iniciar_juego(self, apuesta: int):
        pass
