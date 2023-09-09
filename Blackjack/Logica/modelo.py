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

    def jugador_se_planta(self):
        pass

    def jugada_jugador(self):
        pass

    def jugador_gano(self):
        pass

    def se_paga_jugador(self):
        pass

    def se_resta_jugador(self):
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

    def reoartir_cartas(self, cartas: list):
        pass

    def jugada_jugador(self):
        pass

    def jugador_se_planta(self):
        pass

    def calcular_mano_jugador(self):
        pass

    def jugada_casa(self):
        pass

    def mostrar_cartas_casa(self, cartas: list):
        pass

    def casa_gano(self):
        pass

    def comparar_manos(self):
        pass

    def jugador_gano(self):
        pass

    def empate(self):
        pass

    def se_paga_jugador(self):
        pass

    def se_resta_jugador(self):
        pass

    def jugar_de_nuevo(self):
        pass
