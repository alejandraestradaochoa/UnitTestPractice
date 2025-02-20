class ErrorMontoInvalido(Exception):
    def __init__(self, monto:float):
        super().__init__(f"el monto {monto} debe ser superior a cero")
