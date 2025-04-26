
# 🤖 Proyecto Pepper

Este proyecto tiene como objetivo controlar al robot Pepper utilizando Python y la interfaz NAOqi, permitiéndole ejecutar una secuencia de movimientos tipo coreografía.

## 👨‍💻 Autores

- Miguel Ángel Jiménez Morales  
- Dikersson Alexis Cañon Vanegas  
- 📅 Fecha: 25 de abril de 2025

---

## 📦 Librerías utilizadas

- **naoqi**: Interfaz principal para comunicación con Pepper.
- **argparse**: Análisis de argumentos desde la terminal.
- **sys**: Acceso a variables del sistema.
- **os**: Funciones dependientes del sistema operativo.
- **almath**: Cálculos matemáticos para robótica.
- **math**: Funciones matemáticas estándar.
- **motion**: Control del movimiento del robot.
- **httplib**: Cliente HTTP para Python 2.
- **json**: Manejo de datos en formato JSON.

---

## 🛠 Requisitos

- Python 2.7
- Framework NAOqi
- Acceso a un robot Pepper (en la misma red)
- Choregraphe instalado

---

## 🚀 Instalación y uso

### Conexión con Pepper

1. Asegúrate de estar en la misma red que el robot.
2. Abre terminal en Ubuntu.
3. Usa el comando:
   ```bash
   ssh nao@<DIRECCIÓN_IP>
   ```

### Ejecución del script

1. Abre un archivo con `nano`:
   ```bash
   nano coreografia.py
   ```
2. Pega el código proporcionado.
3. Guarda con `CTRL + O`, cierra con `CTRL + X`.
4. Ejecuta con:
   ```bash
   python coreografia.py
   ```

---

## 🧠 Descripción del código

- **ALProxy**: Conexión a módulos como ALMotion, ALTextToSpeech, etc.
- **wakeUp()**: Activa al robot.
- **goToPosture("StandInit", 0.5)**: Posición inicial.
- **moveTo(x, y, θ)**: Movimiento en espacio 2D o rotación.
- **angleInterpolationWithSpeed()**: Movimiento de articulaciones con velocidad controlada.
- **angleInterpolation()**: Interpolación de ángulos de cabeza.

---

## 🎯 Funciones principales

- Movimientos de brazos y piernas.
- Síntesis de voz.
- Movimiento de cabeza.
- Giro completo final.

---

## 🧪 Guía rápida para Choregraphe

1. Abrir Choregraphe.
2. Aceptar términos y activar periodo de prueba.
3. Conectar al robot Pepper.
4. Usar bloques para diseñar la coreografía.
5. Ejecutar.

---

## 📌 Nota

Este proyecto fue realizado como parte de un ejercicio de control básico del robot Pepper. Está enfocado en comprender la integración entre Python y NAOqi para el desarrollo de movimientos predefinidos.
