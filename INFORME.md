PRUEBAS UNITARIAS Y CORRECCIÓN DE ERRORES
INFORME FINAL
Datos generales
Estudiante: MARIANA ALZATE SOTO
Grupo: INTRODUCCIÓN A DEVOPS
Fecha: 18 DE OCTUBRE DE 2026
Introducción
El presente informe documenta el trabajo realizado en el proyecto de pruebas unitarias y corrección de errores. El propósito de la práctica fue analizar el comportamiento de diferentes funciones, identificar problemas en su implementación, corregirlos y comprobar su funcionamiento mediante pruebas automatizadas.
El trabajo se concentró en tres módulos de Python: calculadora.py, descuentos.py y manipulador_texto.py. A partir de estos archivos se desarrollaron y ejecutaron pruebas para verificar operaciones matemáticas, cálculos comerciales y procesamiento de cadenas de texto. También se abordaron casos límite y entradas que requieren un manejo explícito de errores.
Adicionalmente, se utilizó Git para registrar los cambios y hacer seguimiento a la evolución del proyecto. Finalmente, se midió la cobertura del código con pytest-cov para identificar las instrucciones que todavía no se ejecutan durante las pruebas.
La práctica permitió relacionar la programación, las pruebas automatizadas y el control de versiones como actividades complementarias dentro de un proceso de desarrollo de software.
1.	Análisis técnico de los módulos
a.	Módulo calculadora.py
Este módulo contiene funciones para realizar operaciones matemáticas básicas y otros cálculos con números y listas. Entre las funciones evaluadas se encuentran la suma, la resta, la multiplicación, la división, la potencia, la raíz cuadrada, el promedio y la búsqueda de valores máximos y mínimos.
Durante la práctica se identificaron y corrigieron problemas relacionados con la validación de entradas y la inicialización de variables. En particular, se ajustó la función de raíz cuadrada para rechazar números negativos mediante una excepción ValueError, y se corrigió la inicialización de la función minimo(lista) para que comenzara con un elemento real de la lista.
Las pruebas también contemplaron situaciones como la división por cero, el cálculo del promedio de una lista vacía y la búsqueda de máximos y mínimos cuando la lista no contiene elementos.
Estos casos son importantes porque permiten comprobar no solo el resultado de una operación válida, sino también el comportamiento del programa ante entradas que no puede procesar de manera normal.
b.	Módulo descuentos.py
Este módulo reúne funciones relacionadas con la aplicación de descuentos y el cálculo de precios finales. Las pruebas abarcan descuentos individuales, descuentos por volumen, descuentos acumulativos y descuentos apilados, además de validaciones sobre precios, porcentajes y cantidades.
Una de las correcciones verificadas consistió en modificar la base sobre la cual se calcula el impuesto. La implementación anterior calculaba el impuesto sobre el precio original, incluso después de aplicar un descuento. La modificación utiliza el precio descontado como base para el cálculo.
También se evaluaron entradas inválidas, como precios negativos, porcentajes fuera del rango permitido, cantidades negativas y descuentos acumulados que superan el total permitido por la función.
La validación de estos escenarios es relevante porque un error en la secuencia de los cálculos puede producir resultados incorrectos aun cuando el programa no genere una excepción.
c.	Módulo manipulador_texto.py
Este módulo contiene funciones para transformar y analizar cadenas de texto. Entre los comportamientos evaluados se encuentran invertir cadenas, contar vocales y consonantes, reconocer palíndromos, eliminar duplicados, cambiar la capitalización, reemplazar subcadenas, dividir textos en palabras, extraer dominios y normalizar espacios.
En este módulo se corrigieron dos problemas concretos. El primero correspondía al reconocimiento de palíndromos, que no normalizaba adecuadamente mayúsculas, espacios y signos de puntuación. El segundo se relacionaba con la separación de palabras mediante espacios repetidos, que podía generar elementos vacíos.
Las pruebas incluyeron cadenas vacías, textos con mayúsculas y espacios, correos inválidos y otros escenarios particulares. Estos casos permitieron verificar diferentes comportamientos del procesamiento de texto y no limitar las comprobaciones a entradas sencillas.
2.	Errores identificados y correcciones realizadas
Las siguientes correcciones están respaldadas por las diferencias de código registradas en los commits revisados.
N.º	Función	Problema identificado	Ejemplo o situación	Corrección realizada
1	raiz_cuadrada(numero)	No se validaban los números negativos antes del cálculo.	La entrada -9 podía producir un resultado complejo.	Se agregó una condición que genera ValueError cuando el número es negativo.
2	minimo(lista)	La variable que almacenaba el mínimo provisional comenzaba en cero.	Para [3, 5, 8], el resultado podía ser 0, aunque no pertenecía a la lista.	Se inicializó la variable con lista[0], después de comprobar que la lista no estuviera vacía.
3	calcular_precio_final(precio, impuesto, descuento)	El impuesto se calculaba sobre el precio original y no sobre el precio descontado.	Precio de 100.000, descuento del 10 % e impuesto del 20 %.	Se cambió la base del impuesto a precio_con_descuento.
4	es_palindromo(cadena)	La comparación no normalizaba mayúsculas, espacios ni signos de puntuación.	"Anita lava la tina" debía reconocerse como palíndromo.	Se convirtió el texto a minúsculas y se conservaron únicamente los caracteres alfanuméricos.
5	dividir_en_palabras(cadena)	La separación mediante un espacio literal podía producir elementos vacíos ante espacios consecutivos.	"hola mundo" podía generar elementos vacíos entre las palabras.	Se reemplazó split(' ') por split().
3.	 Ejecución de las pruebas unitarias
Para verificar el funcionamiento de los módulos, ejecuté las pruebas desde la terminal de Debian, con el entorno virtual de Python activo. El comando utilizado fue:
pytest tests/ -v
El resultado fue el siguiente:
collected 69 items
La distribución de las pruebas aprobadas fue:
Archivo de pruebas	Pruebas aprobadas
tests/test_calculadora.py	15
tests/test_descuentos.py	26
tests/test_manipulador_texto.py	28
Total	69
Las 69 pruebas finalizaron satisfactoriamente y no se registraron fallos en esta ejecución. Entre los escenarios evaluados se encuentran la división por cero, las raíces cuadradas negativas, las listas vacías, los porcentajes inválidos, los descuentos y el procesamiento de cadenas con espacios o diferencias entre mayúsculas y minúsculas.
Este resultado indica que las funciones evaluadas respondieron de acuerdo con las condiciones y los resultados esperados definidos en las pruebas. Sin embargo, una ejecución satisfactoria no garantiza que el programa esté libre de todos los errores posibles: también es necesario considerar la variedad y calidad de los casos evaluados.
4.	Análisis de cobertura del código
Comando utilizado
Para medir la cobertura de los tres módulos se ejecutó el siguiente comando:
pytest tests/ -v --cov=src.calculadora --cov=src.descuentos --cov=src.manipulador_texto --cov-report=term-missing
La herramienta pytest-cov permitió identificar las instrucciones ejecutadas y las que permanecieron sin cobertura durante esta ejecución.
La cobertura global fue del 91 %, correspondiente a 195 instrucciones.
Líneas sin cobertura
La ejecución identificó las siguientes líneas sin cobertura:
•	src/calculadora.py: líneas 62–64 y 68–70.
•	src/descuentos.py: línea 64.
•	src/manipulador_texto.py: líneas 15, 55, 70, 80, 87, 97, 108, 115, 119, 134 y 142.
Estas líneas representan oportunidades para revisar la estrategia de pruebas. Para decidir qué pruebas adicionales conviene incorporar, es necesario examinar qué instrucciones contienen y determinar si corresponden a condiciones, excepciones u otros comportamientos relevantes.
La cobertura es una medida de las instrucciones ejecutadas, no una medida directa del porcentaje de errores detectados. Por esa razón, un porcentaje alto no garantiza que todos los comportamientos posibles hayan sido comprobados.




HISTORIAL DE COMMITS Y TRAZABILIDAD
El historial de Git permite seguir la evolución del proyecto y diferenciar los cambios previos de las contribuciones registradas durante la práctica.
Contribuciones registradas a nombre de Mariana.AS
Los siguientes ocho commits aparecen registrados a nombre de Mariana.AS, con fecha del 18 de octubre de 2026.
Fecha	Commit	Mensaje del commit	Aporte al proyecto
18/10/2026	503d117	config: agregar gitignore para entorno Python y pruebas	Configuración de .gitignore para excluir archivos que no deben incorporarse al repositorio.
18/10/2026	a10c6dd	test: agregar pruebas unitarias de calculadora	Incorporación de pruebas para el módulo de calculadora.
18/10/2026	bc0fcc6	fix: corregir raiz cuadrada y minimo	Corrección de la validación de raíces cuadradas negativas y de la inicialización del mínimo.
18/10/2026	22cbc5f	test: cubrir listas vacias en maximo y minimo	Ampliación de las pruebas para listas vacías.
18/10/2026	16c7ae1	test: agregar pruebas unitarias de descuentos	Incorporación de pruebas para las funciones de descuentos.
18/10/2026	00e2658	fix: calcular impuesto sobre precio descontado	Corrección de la base utilizada para calcular el impuesto.
18/10/2026	90fd3c8	Agrega pruebas y corrige manipulador de texto	Ajustes en el manipulador de texto e incorporación de pruebas.
18/10/2026	5dbc855	test: unificar estructura AAA en pruebas unitarias	Organización de las pruebas mediante la estructura AAA.
Antecedentes del repositorio
El historial también contiene cinco commits anteriores, fechados el 8 de abril de 2026 y registrados a nombre de otros autores. Estos constituyen antecedentes del proyecto y no se presentan como contribuciones personales de esta práctica.
Fecha	Commit	Cambio registrado	Relevancia
08/04/2026	0312a40	Proyecto inicial: Código para pruebas unitarias	Creación de la estructura base, los módulos iniciales y la documentación.
08/04/2026	033c5e5	Eliminar solución de bugs - solo ejercicio para estudiantes	Conservación del propósito formativo del ejercicio.
08/04/2026	4f33acf	Actualizar README: Eliminar instrucciones de push, objetivo es que todas las pruebas pasen	Ajustes en las instrucciones del proyecto.
08/04/2026	92abef7	Agregar 4 nuevos módulos con 6 bugs adicionales (total: 14 bugs)	Ampliación del alcance del ejercicio.
08/04/2026	f0c93ae	Update README headings for clarity	Mejora de los encabezados de la documentación.
Interpretación del historial
La secuencia de commits del muestra un proceso de trabajo que combina configuración, incorporación de pruebas, corrección de errores y organización del código de prueba.
Primero se configuró el repositorio y se incorporaron pruebas para la calculadora. Posteriormente se registraron correcciones en funciones matemáticas y pruebas para casos límite. El proceso continuó con las pruebas de descuentos, el ajuste del cálculo del impuesto y las modificaciones del manipulador de texto.
Finalmente, el commit 5dbc855 registró la unificación de la estructura AAA. Esta organización separa la preparación de los datos (Arrange), la ejecución de la función (Act) y la comprobación del resultado (Assert), facilitando la lectura y el mantenimiento de las pruebas.
El historial evidencia la utilidad del control de versiones para documentar cambios, facilitar su revisión y mantener una secuencia comprensible de trabajo. Los mensajes de los commits también ayudan a relacionar cada modificación con su propósito técnico.
5.	Reflexión sobre el aprendizaje
Esta práctica me permitió comprender mejor la relación entre la corrección de errores, las pruebas unitarias y el control de versiones. Al principio, el trabajo no consistió únicamente en escribir código, sino también en preparar el entorno y resolver dificultades para acceder y trabajar con la instancia Debian en AWS. Esta experiencia me mostró que el desarrollo de software requiere atender tanto los problemas de configuración como los relacionados con la lógica del programa.
Al analizar las funciones, comprendí que una implementación puede parecer correcta en situaciones sencillas y, aun así, presentar fallos en casos particulares. La función minimo(lista), por ejemplo, evidenció la importancia de elegir adecuadamente los valores iniciales. En el cálculo del precio final, el problema no estaba en la operación matemática de manera aislada, sino en el orden en que se aplicaban el descuento y el impuesto. En el procesamiento de texto, fue necesario considerar diferencias entre mayúsculas, espacios repetidos y caracteres que no debían intervenir en la comparación de un palíndromo.
También comprendí que las pruebas unitarias no deben limitarse a comprobar resultados habituales. Es necesario incluir entradas inválidas, listas vacías, valores límite y situaciones que permitan verificar el manejo de errores. La ejecución final de 69 pruebas aprobadas fue una evidencia del funcionamiento esperado en los escenarios definidos, mientras que la cobertura del 91 % permitió reconocer que todavía existen instrucciones que podrían evaluarse con pruebas adicionales.
Otro aprendizaje importante fue el uso de Git para registrar la evolución del trabajo. Los commits permitieron identificar cuándo se agregaron pruebas, cuándo se corrigieron funciones y cuándo se reorganizó su estructura. Esto hizo posible revisar las modificaciones y sustentar las conclusiones del informe con evidencias concretas del repositorio.
Considero que todavía debo fortalecer mi práctica en la configuración de entornos, el manejo de la terminal y la interpretación de herramientas de automatización. Sin embargo, el ejercicio me permitió avanzar en la comprensión de un proceso de trabajo más ordenado: identificar un problema, proponer una corrección, verificarla mediante pruebas y registrar los cambios realizados.
En conclusión, la práctica me ayudó a entender que la calidad del software no depende únicamente de que el programa se ejecute, sino también de que su comportamiento se compruebe de forma sistemática y de que los cambios puedan rastrearse. Estos aprendizajes constituyen una base importante para continuar estudiando las prácticas de integración, entrega y mejora continua asociadas con DevOps.
Conclusiones
1.	Se realizaron correcciones verificables en los módulos de calculadora, descuentos y manipulación de texto, respaldadas por diferencias de código registradas en Git.
2.	La ejecución final de las pruebas reportó 69 pruebas aprobadas y ninguna fallida, lo que confirma el funcionamiento esperado de las situaciones cubiertas por los casos de prueba implementados.
3.	La cobertura global alcanzó el 91 % de 195 instrucciones contabilizadas. Los resultados permiten identificar oportunidades para ampliar las pruebas, especialmente en los módulos de calculadora y manipulación de texto.
4.	El historial de commits documenta las contribuciones registradas a nombre de Mariana.AS y permite diferenciarlas de los antecedentes del repositorio.
5.	La práctica fortaleció la comprensión de las pruebas automatizadas, la corrección de errores, la cobertura y el control de versiones como elementos complementarios del desarrollo de software.

