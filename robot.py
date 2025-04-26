# -- coding: utf-8 --
from naoqi import ALProxy
import almath
import time

# Conexión local al robot Pepper
robotIP = "127.0.0.1"
port = 9559

# Inicialización de proxies para movimientos y posturas
motionProxy = ALProxy("ALMotion", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)

# Pepper despierta y adopta postura inicial
motionProxy.wakeUp()
postureProxy.goToPosture("StandInit", 0.5)
ttsProxy.say("Hola, estoy listo para bailar")

# Inicio de la coreografía

# Movimiento 1: Avance y saludo
ttsProxy.say("Observa esto")
motionProxy.moveTo(0.3, 0, 0)
motionProxy.angleInterpolationWithSpeed("RShoulderPitch", -1.0, 0.2)  # Brazo derecho arriba
motionProxy.angleInterpolationWithSpeed("RElbowYaw", 1.5, 0.2)
time.sleep(0.5)

# Movimiento 2: Regreso y cambio de brazo
motionProxy.moveTo(-0.3, 0, 0)
motionProxy.angleInterpolationWithSpeed("RShoulderPitch", 1.5, 0.2)  # Baja brazo derecho
motionProxy.angleInterpolationWithSpeed("LShoulderPitch", -1.0, 0.2)  # Brazo izquierdo arriba
motionProxy.angleInterpolationWithSpeed("LElbowYaw", -1.5, 0.2)
time.sleep(0.5)

# Movimiento 3: Movimiento lateral derecho
ttsProxy.say("Y ahora hacia la derecha")
motionProxy.moveTo(0, -0.2, 0)
time.sleep(0.5)

# Movimiento 4: Movimiento lateral izquierdo
ttsProxy.say("Ahora hacia la izquierda")
motionProxy.moveTo(0, 0.4, 0)
time.sleep(0.5)

# Movimiento 5: Girar cabeza
ttsProxy.say("Girando mi cabeza")
names = ["HeadYaw"]
angles = [almath.TO_RAD*45, almath.TO_RAD*-45, 0]
times = [1.0, 2.0, 3.0]
isAbsolute = True
motionProxy.angleInterpolation(names, angles, times, isAbsolute)

# Movimiento 6: Pequeña reverencia
ttsProxy.say("Gracias por tu atención")
motionProxy.angleInterpolationWithSpeed(["HipPitch", "KneePitch"], [-0.2, 0.4], 0.2)
time.sleep(1)
motionProxy.angleInterpolationWithSpeed(["HipPitch", "KneePitch"], [0, 0], 0.2)
time.sleep(0.5)

# Movimiento 7: Giro elegante final
ttsProxy.say("Hasta la próxima")
motionProxy.moveTo(0, 0, almath.TO_RAD*360)  # Giro completo

# Finaliza coreografía en postura inicial y descanso
postureProxy.goToPosture("StandInit", 0.5)
motionProxy.rest()
