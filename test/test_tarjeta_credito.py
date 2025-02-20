import pytest
from src.model.compra import Compra
from src.model.tarjeta_credito import TarjetaCredito
from src.model.error_tasa_usura import ErrorTasaUsura
from src.model.error_monto_invalido import ErrorMontoInvalido


def test_caso_36_cuotas():
    tarjeta_credito : TarjetaCredito = TarjetaCredito(3.4, 1000000) 
    compra : Compra = Compra(850000, 3.4, 24)
    tarjeta_credito.registrar_compra(compra)
    total_interes = tarjeta_credito.calcular_total_interes()
    assert total_interes == 521.08
    
def tasa_de_usura():
    with pytest.raises(ErrorTasaUsura):
        tarjeta_credito : TarjetaCredito = TarjetaCredito(12.5, 1000000)
        compra : Compra = Compra(50000, 12.5, 60)
        tarjeta_credito.registrar_compra(compra)
        total_interes = tarjeta_credito.calcular_total_interes()

def test_cuota_unica():
    tarjeta_credito : TarjetaCredito = TarjetaCredito(2.4, 1000000)
    compra : Compra = Compra(90000, 2.4,1)
    tarjeta_credito.registrar_compra(compra)
    total_interes = tarjeta_credito.calcular_total_interes()
    assert total_interes == 0

def monto_invalido():
    with pytest.raises(ErrorMontoInvalido):
        tarjeta_credito = TarjetaCredito = TarjetaCredito(2.4, 1000000)
        compra : Compra = Compra (0, 2.4, 60)
        tarjeta_credito.registrar_compra(compra)
        total_interes = tarjeta_credito.calcular_total_interes()
        


