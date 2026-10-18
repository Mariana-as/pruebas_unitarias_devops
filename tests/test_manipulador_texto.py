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
    assert invertir_cadena("hola") == "aloh"


def test_invertir_cadena_vacia():
    assert invertir_cadena("") == ""


def test_contar_vocales():
    assert contar_vocales("Hola Mundo") == 4


def test_contar_vocales_sin_vocales():
    assert contar_vocales("rhythm") == 0


def test_contar_consonantes():
    assert contar_consonantes("Hola123!") == 2


def test_contar_consonantes_vacio():
    assert contar_consonantes("") == 0


def test_es_palindromo_simple():
    assert es_palindromo("reconocer") is True


def test_es_palindromo_con_mayusculas_y_espacios():
    assert es_palindromo("Anita lava la tina") is True


def test_es_palindromo_no_palindromo():
    assert es_palindromo("casa") is False


def test_es_palindromo_vacio():
    assert es_palindromo("") is False


def test_eliminar_duplicados():
    assert eliminar_duplicados("banana") == "ban"


def test_capitalizar_palabras():
    assert capitalizar_palabras("hola MUNDO") == "Hola Mundo"


def test_convertir_a_titulo():
    assert convertir_a_titulo("el mundo feliz") == "El Mundo Feliz"


def test_reemplazar_subcadena():
    assert reemplazar_subcadena("uno dos uno", "uno", "tres") == "tres dos tres"


def test_reemplazar_subcadena_con_limite():
    assert reemplazar_subcadena("a-a-a", "a", "b", 2) == "b-b-a"


def test_dividir_en_palabras():
    assert dividir_en_palabras("hola mundo") == ["hola", "mundo"]


def test_dividir_en_palabras_con_espacios_multiples():
    assert dividir_en_palabras("hola   mundo") == ["hola", "mundo"]


def test_extraer_dominio():
    assert extraer_dominio("persona@ejemplo.com") == "ejemplo.com"


def test_extraer_dominio_correo_invalido():
    assert extraer_dominio("correo-invalido") == ""


def test_enmascarar_email():
    assert enmascarar_email("mariana@ejemplo.com") == "m*****a@ejemplo.com"


def test_enmascarar_email_usuario_corto():
    assert enmascarar_email("ab@ejemplo.com") == "ab@ejemplo.com"


def test_normalizar_espacios():
    assert normalizar_espacios("  hola   mundo  ") == "hola mundo"


def test_truncar():
    assert truncar("abcdef", 5) == "ab..."


def test_truncar_texto_corto():
    assert truncar("hola", 10) == "hola"


def test_es_anagrama():
    assert es_anagrama("Roma", "amor") is True


def test_es_anagrama_con_espacios():
    assert es_anagrama("la mar", "alma r") is True


def test_es_anagrama_no_coincide():
    assert es_anagrama("casa", "perro") is False


def test_es_anagrama_con_cadena_vacia():
    assert es_anagrama("", "amor") is False
