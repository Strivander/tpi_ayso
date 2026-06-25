# Calculadora de Promedios en Python

## Descripción
Este script es una herramienta de consola desarrollada en Python que calcula el promedio aritmético de tres calificaciones numéricas ingresadas por el usuario. 

Fue diseñado específicamente como un **caso de prueba práctico** para validar el correcto despliegue, la estabilidad y la operatividad de un entorno de desarrollo aislado (Ubuntu Server en versión minimizada) montado sobre una máquina virtual.

## Características Técnicas
* **Interacción por consola:** Solicitud iterativa de datos mediante la terminal pura, sin dependencias de interfaces gráficas (GUI).
* **Gestión de memoria:** Almacenamiento dinámico de los valores de entrada utilizando listas mutables.
* **Procesamiento optimizado:** Cálculo aritmético delegado a las funciones integradas nativas del lenguaje (`sum()` y `len()`).
* **Salida estandarizada:** Presentación del resultado formateado a dos espacios decimales mediante el uso de *f-strings* (`:.2f`).

## Requisitos del Entorno
* Sistema Operativo: Linux (Testeado en Ubuntu Server) / Windows / macOS.
* Intérprete: **Python 3.x** instalado en el sistema.

## Instrucciones de Ejecución
1. Abrir la terminal o consola de comandos del servidor.
2. Navegar hasta el directorio donde se encuentra alojado el archivo `promedios.py`.
3. Iniciar el script ejecutando el siguiente comando:
   ```bash
   python3 promedios.py