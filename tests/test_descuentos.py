import pytest

from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado,
)


def test_aplicar_descuento():
    # Arrange
    precio = 100
    porcentaje = 20

    # Act
    resultado = aplicar_descuento(precio, porcentaje)

    # Assert
    assert resultado == 80


def test_aplicar_descuento_cero():
    # Arrange
    precio = 100
    porcentaje = 0

    # Act
    resultado = aplicar_descuento(precio, porcentaje)

    # Assert
    assert resultado == 100


def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio = -10

    # Act y Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, 10)


def test_aplicar_descuento_porcentaje_invalido_lanza_error():
    # Arrange
    porcentaje = 110

    # Act y Assert
    with pytest.raises(ValueError):
        aplicar_descuento(100, porcentaje)


def test_calcular_descuento():
    # Arrange
    precio = 200
    porcentaje = 15

    # Act
    resultado = calcular_descuento(precio, porcentaje)

    # Assert
    assert resultado == 30


def test_calcular_precio_final_con_descuento_e_impuesto():
    # Arrange
    precio = 100
    impuesto = 10
    descuento = 20

    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)

    # Assert
    assert resultado == 88


def test_calcular_precio_final_sin_descuento():
    # Arrange
    precio = 100
    impuesto = 10
    descuento = 0

    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)

    # Assert
    assert resultado == 110


def test_descuento_por_volumen_cantidad_menor_a_diez():
    # Arrange
    cantidad = 5
    precio_unitario = 10

    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)

    # Assert
    assert resultado == 50


def test_descuento_por_volumen_cien_unidades():
    # Arrange
    cantidad = 100
    precio_unitario = 10

    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)

    # Assert
    assert resultado == 800


def test_descuento_cumulativo():
    # Arrange
    precio = 100
    descuentos = [10, 20]

    # Act
    resultado = descuento_cumulativo(precio, descuentos)

    # Assert
    assert resultado == 72


def test_descuento_cumulativo_lista_vacia():
    # Arrange
    precio = 100
    descuentos = []

    # Act
    resultado = descuento_cumulativo(precio, descuentos)

    # Assert
    assert resultado == 100


def test_descuento_apilado():
    # Arrange
    precio = 100
    descuentos = [10, 20]

    # Act
    resultado = descuento_apilado(precio, descuentos)

    # Assert
    assert resultado == 70


def test_descuento_apilado_total_superior_a_cien_lanza_error():
    # Arrange
    precio = 100
    descuentos = [60, 50]

    # Act y Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)
