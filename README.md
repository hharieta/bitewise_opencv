
# Aplicación de BiteWise con OpenCV

Tomado del canal de [OMES](https://www.youtube.com/c/OMES-va) de realizan la aplicación de operadores a nivel de bits con OpenCV y Python 🐍️ para visualizar la región de interés de una imagen

***

## Prepara tu entorno virtual 

1.  Crear entorno virtual

* Windows:

```powershell
python -m venv c:\ruta\al\entorno\virtual
```

* MacOS y Linux:

```bash
python -m venv ruta/al/entorno/virtual
```

2. Activar entorno virual

* Windows:

```
c:\ruta\al\entorno\virtual\scripts\activate.bat
```

* MacOs y Linux:

```
source ruta/al/entorno/virtual/bin/activate
```

3. Desactivar entorno virtual

* Windos, MacOS y Linux:

```
deactivate
```

4. Eliminar entorno virtual

* Windows:

```
rmdir c:\ruta\al\entorno\virtual /s
```

MacOS y Linux:

```
rm -rf ruta/al/entorno/virtual
```

***

🗒️ **NOTA**: Buenas prácticas sobre los entornos virtuales

* No se debe añadir manualmente ningún fichero dentro de una carpeta que almacena un entorno virtual. Esta carpeta sólo debe contener los ficheros que se crean por defecto al crear el entorno virtual y los paquetes adicionales que hayamos instalado con el comando pip.
* La carpeta del entorno virtual no debe incluirse a nuestra herramienta de control de versiones. En lugar de ello es recomendado añadir un fichero requirements.txt con el listado de los paquetes necesarios para ejecutar el proyecto.

## Tablas de la verdad 🕶️


A   |   B | A `&` B | A `|` B | A `^` B | `~`A
--- | --- | --- | --- | --- | ---
0   | 0   | 0   | 0   | 0   |   1
0   | 1   | 0   | 1   | 1  |   1  
1   | 0   | 0   | 1   | 1  |   0   
1   | 1   | 1  |  1   | 0  |   0  

