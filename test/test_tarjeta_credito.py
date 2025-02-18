import pytest
from src.model.compra import Compra
from src.model.tarjeta_credito import TarjetaCredito


def test_caso_36_cuotas():
    tarjeta_credito : TarjetaCredito = TarjetaCredito(3.4, 1000000) 
    compra : Compra = Compra(850000, 3.4, 24)
    tarjeta_credito.registrar_compra(compra)
    total_interes = tarjeta_credito.calcular_total_interes()
    assert total_interes == 521.08
    
