# Sistema de Cotización de Ventanas PQR

Este es un sistema de cotización para la empresa PQR, que fabrica ventanas de aluminio. El programa interactúa con el usuario, solicitando datos sobre el cliente, el tipo de ventana, el tipo de vidrio, el aluminio, la cantidad de ventanas, y calcula el costo total aplicando un descuento si corresponde.

## Estructura del Proyecto

El proyecto contiene las siguientes clases, cada una en su archivo correspondiente:

- `Cliente.py`: Representa la información del cliente.
- `Ventana.py`: Representa la ventana, con su estilo, ancho y alto.
- `Nave.py`: Representa las naves o paneles de la ventana.
- `Vidrio.py`: Representa los tipos de vidrio y si es esmerilado.
- `Aluminio.py`: Representa el acabado de aluminio y su costo.
- `Descuento.py`: Representa los descuentos aplicables a la cotización.
- `Cotizacion.py`: Calcula la cotización de las ventanas.
- `main.py`: El script principal que ejecuta la aplicación.

## Requerimientos

Asegúrate de tener los siguientes requisitos instalados antes de ejecutar el proyecto:

- **Python 3.x**: Puedes verificar tu versión de Python ejecutando:
  ```bash
  python --version
## Instalación y Configuración
 # Clona este repositorio: Abre una terminal y ejecuta el siguiente comando:
 ```bash
 git clone https://github.com/tuusuario/nombre-del-repositorio.git 
```
 # Accede al directorio del proyecto:
 ```bash
 cd Parcial_Proyecto
```
## Activa el entorno virtual:
# En Windows:
```bash
 .\venv\Scripts\activate
```
# En Linux/MacOS:
```bash
 source venv/bin/activate
```
# Instala las dependencias: Este proyecto no tiene dependencias externas, pero si decides agregar bibliotecas más adelante, puedes instalar las dependencias ejecutando:
```bash
pip install -r requirements.txt
```
## Ejecución del Proyecto
# Ejecuta el archivo main.py: En la terminal, ejecuta el siguiente comando:
```bash
python main.py
```
# Interacción: El programa te pedirá ingresar los detalles necesarios para calcular la cotización de las ventanas (cliente, ventana, vidrio, aluminio, etc.).
# Salida: Al final de la ejecución, el programa te mostrará el total a pagar por las ventanas especificadas.

# Autor: Santiago Jimenez Martinez