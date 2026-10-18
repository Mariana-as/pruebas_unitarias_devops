from src.manipulador_texto import (
    invertir_cadena,
    contar_vocales,
    contar_consonantes,
    es_palindromo,
    eliminar_duplicados,
    capitalizar_palabras,
    convertir_a_titulo,
    reemplazar_subcadena,
    dividir_en_palabras,
    extraer_dominio,
    enmascarar_email,
    normalizar_espacios,
    truncar,
    es_anagrama,
)


def test_invertir_cadena():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'hola'
    esperado = 'aloh'

    # Act: ejecutar la función
    resultado = invertir_cadena(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_invertir_cadena_vacia():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = ''
    esperado = ''

    # Act: ejecutar la función
    resultado = invertir_cadena(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_contar_vocales():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'Hola Mundo'
    esperado = 4

    # Act: ejecutar la función
    resultado = contar_vocales(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_contar_vocales_sin_vocales():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'rhythm'
    esperado = 0

    # Act: ejecutar la función
    resultado = contar_vocales(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_contar_consonantes():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'Hola123!'
    esperado = 2

    # Act: ejecutar la función
    resultado = contar_consonantes(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_contar_consonantes_vacio():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = ''
    esperado = 0

    # Act: ejecutar la función
    resultado = contar_consonantes(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_es_palindromo_simple():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'reconocer'
    esperado = True

    # Act: ejecutar la función
    resultado = es_palindromo(entrada_1)

    # Assert: comprobar el resultado
    assert resultado is esperado


def test_es_palindromo_con_mayusculas_y_espacios():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'Anita lava la tina'
    esperado = True

    # Act: ejecutar la función
    resultado = es_palindromo(entrada_1)

    # Assert: comprobar el resultado
    assert resultado is esperado


def test_es_palindromo_no_palindromo():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'casa'
    esperado = False

    # Act: ejecutar la función
    resultado = es_palindromo(entrada_1)

    # Assert: comprobar el resultado
    assert resultado is esperado


def test_es_palindromo_vacio():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = ''
    esperado = False

    # Act: ejecutar la función
    resultado = es_palindromo(entrada_1)

    # Assert: comprobar el resultado
    assert resultado is esperado


def test_eliminar_duplicados():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'banana'
    esperado = 'ban'

    # Act: ejecutar la función
    resultado = eliminar_duplicados(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_capitalizar_palabras():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'hola MUNDO'
    esperado = 'Hola Mundo'

    # Act: ejecutar la función
    resultado = capitalizar_palabras(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_convertir_a_titulo():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'el mundo feliz'
    esperado = 'El Mundo Feliz'

    # Act: ejecutar la función
    resultado = convertir_a_titulo(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_reemplazar_subcadena():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'uno dos uno'
    entrada_2 = 'uno'
    entrada_3 = 'tres'
    esperado = 'tres dos tres'

    # Act: ejecutar la función
    resultado = reemplazar_subcadena(entrada_1, entrada_2, entrada_3)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_reemplazar_subcadena_con_limite():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'a-a-a'
    entrada_2 = 'a'
    entrada_3 = 'b'
    entrada_4 = 2
    esperado = 'b-b-a'

    # Act: ejecutar la función
    resultado = reemplazar_subcadena(entrada_1, entrada_2, entrada_3, entrada_4)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_dividir_en_palabras():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'hola mundo'
    esperado = ['hola', 'mundo']

    # Act: ejecutar la función
    resultado = dividir_en_palabras(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_dividir_en_palabras_con_espacios_multiples():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'hola   mundo'
    esperado = ['hola', 'mundo']

    # Act: ejecutar la función
    resultado = dividir_en_palabras(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_extraer_dominio():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'persona@ejemplo.com'
    esperado = 'ejemplo.com'

    # Act: ejecutar la función
    resultado = extraer_dominio(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_extraer_dominio_correo_invalido():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'correo-invalido'
    esperado = ''

    # Act: ejecutar la función
    resultado = extraer_dominio(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_enmascarar_email():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'mariana@ejemplo.com'
    esperado = 'm*****a@ejemplo.com'

    # Act: ejecutar la función
    resultado = enmascarar_email(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_enmascarar_email_usuario_corto():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'ab@ejemplo.com'
    esperado = 'ab@ejemplo.com'

    # Act: ejecutar la función
    resultado = enmascarar_email(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_normalizar_espacios():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = '  hola   mundo  '
    esperado = 'hola mundo'

    # Act: ejecutar la función
    resultado = normalizar_espacios(entrada_1)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_truncar():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'abcdef'
    entrada_2 = 5
    esperado = 'ab...'

    # Act: ejecutar la función
    resultado = truncar(entrada_1, entrada_2)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_truncar_texto_corto():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'hola'
    entrada_2 = 10
    esperado = 'hola'

    # Act: ejecutar la función
    resultado = truncar(entrada_1, entrada_2)

    # Assert: comprobar el resultado
    assert resultado == esperado


def test_es_anagrama():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'Roma'
    entrada_2 = 'amor'
    esperado = True

    # Act: ejecutar la función
    resultado = es_anagrama(entrada_1, entrada_2)

    # Assert: comprobar el resultado
    assert resultado is esperado


def test_es_anagrama_con_espacios():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'la mar'
    entrada_2 = 'alma r'
    esperado = True

    # Act: ejecutar la función
    resultado = es_anagrama(entrada_1, entrada_2)

    # Assert: comprobar el resultado
    assert resultado is esperado


def test_es_anagrama_no_coincide():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = 'casa'
    entrada_2 = 'perro'
    esperado = False

    # Act: ejecutar la función
    resultado = es_anagrama(entrada_1, entrada_2)

    # Assert: comprobar el resultado
    assert resultado is esperado


def test_es_anagrama_con_cadena_vacia():
    # Arrange: preparar entradas y resultado esperado
    entrada_1 = ''
    entrada_2 = 'amor'
    esperado = False

    # Act: ejecutar la función
    resultado = es_anagrama(entrada_1, entrada_2)

    # Assert: comprobar el resultado
    assert resultado is esperado
