import pytest

from src.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    potencia,
    raiz_cuadrada,
    promedio,
    maximo,
    minimo,
)


def test_sumar_positivos():
    # Arrange
    a, b = 5, 3

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == 8


def test_restar_numeros():
    # Arrange
    a, b = 10, 4

    # Act
    resultado = restar(a, b)

    # Assert
    assert resultado == 6


def test_multiplicar_numeros():
    # Arrange
    a, b = 6, 7

    # Act
    resultado = multiplicar(a, b)

    # Assert
    assert resultado == 42


def test_dividir_numeros():
    # Arrange
    a, b = 12, 3

    # Act
    resultado = dividir(a, b)

    # Assert
    assert resultado == 4


def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0

    # Act y Assert
    with pytest.raises(ValueError):
        dividir(a, b)


def test_potencia():
    # Arrange
    base, exponente = 2, 3

    # Act
    resultado = potencia(base, exponente)

    # Assert
    assert resultado == 8


def test_raiz_cuadrada_positiva():
    # Arrange
    numero = 25

    # Act
    resultado = raiz_cuadrada(numero)

    # Assert
    assert resultado == 5


def test_raiz_cuadrada_negativa_lanza_error():
    # Arrange
    numero = -4

    # Act y Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


def test_promedio_lista():
    # Arrange
    numeros = [2, 4, 6]

    # Act
    resultado = promedio(numeros)

    # Assert
    assert resultado == 4


def test_promedio_lista_vacia_lanza_error():
    # Arrange
    numeros = []

    # Act y Assert
    with pytest.raises(ValueError):
        promedio(numeros)


def test_maximo_lista():
    # Arrange
    numeros = [2, 8, 3]

    # Act
    resultado = maximo(numeros)

    # Assert
    assert resultado == 8


def test_minimo_lista_positiva():
    # Arrange
    numeros = [2, 5, 3]

    # Act
    resultado = minimo(numeros)

    # Assert
    assert resultado == 2


def test_minimo_lista_negativa():
    # Arrange
    numeros = [-5, -2, -8]

    # Act
    resultado = minimo(numeros)

    # Assert
    assert resultado == -8
