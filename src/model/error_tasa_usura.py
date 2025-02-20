class ErrorTasaUsura(Exception):
    def __init__(self, interes:float):
        super().__init__(f"Interes de (interes) supera la tasa de usura")