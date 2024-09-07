import pytest
from models.ventana import Ventana
from models.vidrio import Vidrio
from models.aluminio import Aluminio
from models.descuento import Descuento
from main import calcular_total

@pytest.fixture
def ventana():
    return Ventana("OXXO", 100, 150)  # Ancho 100 cm, Alto 150 cm

@pytest.fixture
def vidrio():
    return Vidrio("Transparente", False, 8.25)  # No esmerilado, costo 8.25

@pytest.fixture
def aluminio():
    return Aluminio("Pulido", 50.7)  # Costo 50.7 por cm lineal

@pytest.fixture
def descuento():
    return Descuento(10, 100)  # 10% de descuento si la cantidad es mayor a 100

def test_calculo_total_sin_descuento(ventana, vidrio, aluminio, descuento):
    # Prueba para calcular el total sin descuento
    cantidad = 10
    total = calcular_total(ventana, vidrio, aluminio, descuento, cantidad)
    
    # Verificar si el total es el esperado
    assert total == pytest.approx(1932767.0, 0.1), f"Total calculado {total} no es correcto"

def test_calculo_total_con_descuento(ventana, vidrio, aluminio, descuento):
    # Prueba para calcular el total con descuento
    cantidad = 200
    total = calcular_total(ventana, vidrio, aluminio, descuento, cantidad)
    
    # Verificar si el total es el esperado
    assert total == pytest.approx(3496454.6, 0.1), f"Total calculado {total} no es correcto"
