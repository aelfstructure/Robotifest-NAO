# -*- encoding: UTF-8 -*-

import motion
import sys
from naoqi import ALProxy
import almath
import time

#inicializar el robot
class Instructor:


    def __init__(self, robotIp, robotPort):
        self.robotIp = robotIp
        self.robotPort = robotPort
        self.motionProxy = ALProxy("ALMotion", self.robotIp, self.robotPort)
        self.postura = ALProxy("ALRobotPosture", self.robotIp, self.robotPort)
        self.palabra = ALProxy("ALTextToSpeech", self.robotIp, self.robotPort)
        self.mover = ALProxy("ALMotion", self.robotIp, self.robotPort)

    def StiffnessOn(proxy):
        pNames = "Body" 
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

        
    def hablar(self, texto):        #método generico para que el robot hable
       self.palabra.say(texto)
       

    def caminar(self): 
        self.mover.moveInit()   #coloca el robot en la posición correcta para caminar, inicializa el proceso de movimiento
        self.mover.moveTo(0.3, 0, 0)        #mover el NAO hacia la pose dada, en este caso 0.5 en X, 0 en Y y 0 en Z
        
    
        
    def moverBrazosArriba(self): #A.
        self.postura.goToPosture("StandInit", 2.0)
        def StifnessOn(proxy):
         pNames = "Body" 
         pStiffnessLists = 1.0
         pTimeLists = 1.0
         proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("Iniciemos con el brazo derecho, levantenlo y sostengamos unos segundos")
        #brazo derecho
        effector   = "RArm"
        space      = motion.FRAME_ROBOT
        path       = [
           [4.44, 0.00, 0.00, 0.0, 0.0, 0.0],       # punto 1
           [3.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # punto 2
           [4.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # punto 3
           [1.0, 2.00, 0.00, 0.0, 0.0, 0.0],        # punto 4
           [2.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # punto 5
           [0.0, 2.00, 0.00, 0.0, 0.0, 0.0]]        # punto 6
        axisMask   = almath.AXIS_MASK_VEL
        times      = [4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        isAbsolute = False
        self.motionProxy.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)
        time.sleep(10)
        self.postura.goToPosture("StandInit", 2.0)
        #brazo izquierdo
        def StifnessOn(proxy):
         pNames = "Body" 
         pStiffnessLists = 1.0
         pTimeLists = 1.0
         proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("vamos con el izquierdo, pero levanten mas arriba el brazo")
        effector   = "LArm"
        space      = motion.FRAME_ROBOT
        path       = [
        [4.4, 0.00, 0.00, 0.0, 0.0, 0.0],        # punto 1
        [3.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # punto 2
        [4.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # punto 3
        [1.0, 2.00, 0.00, 0.0, 0.0, 0.0],        # punto 4
        [2.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # punto 5
        [0.0, 2.00, 0.00, 0.0, 0.0, 0.0]]        # punto 6
        axisMask   = almath.AXIS_MASK_VEL                             #controlar la posición
        times      = [4.0, 5.0, 6.0, 7.0, 8.0, 9.0] # segundos
        isAbsolute = False
        self.motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)
        time.sleep(10)
        self.postura.goToPosture("StandInit", 2.0)
        
        
        
    def relajarCabezaIzquierda(self):   
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("ahora vamos a relajar nuestra cabeza con una serie de movimientos hacia ambos lados, siganme")
        names      = ["Head"]
        angleLists = [1.1667,1.1667]
        timeLists  = [1.0, 1.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names  = ["HeadYaw","HeadPitch"]
        self.motionProxy.setStiffnesses("Head", 0.0)
        time.sleep(10)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("Ahora estiremos un poco más")
        self.postura.goToPosture("StandInit", 2.0)
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.postura.goToPosture("StandInit", 2.0)
        names      = ["Head"]
        angleLists = [1.8800,1.8800]
        timeLists  = [2.0, 2.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names  = ["HeadYaw","HeadPitch"]
        self.motionProxy.setStiffnesses("Head", 0.0)
        time.sleep(10)
        self.postura.goToPosture("StandInit",0.5)
        self.hablar("Perfecto hemos terminado")
    
    def relajarCabezaDerecha(self):
        self.motionProxy = ALProxy("ALMotion", self.robotIp, self.robotPort)
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("ahora vamos hacia la derecha")
        names      = ["Head"]
        angleLists = [-1.1667,-1.1667]
        timeLists  = [1.0, 1.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names  = ["HeadYaw","HeadPitch"]
        self.motionProxy.setStiffnesses("Head", 0.0)
        time.sleep(10)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("Ahora estiremos un poco más")
        self.postura.goToPosture("StandInit",2.0)
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.postura.goToPosture("StandInit", 2.0)
        names      = ["Head"]
        angleLists = [-1.8800,-1.8800]
        timeLists  = [2.0, 2.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names  = ["HeadYaw","HeadPitch"]
        self.motionProxy.setStiffnesses("Head", 0.0)
        time.sleep(10)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("Perfecto hemos terminado")
    
    def girarBrazos(self):
        # Dar inicio a la rigidez del Nao
        def StifnessOn(proxy):
         pNames = "Body" 
         pStiffnessLists = 1.0
         pTimeLists = 1.0
         proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("ahora vamos a girar los brazos, este movimiento va a ayudarnos con la circulacion en nuestro cuerpo")
        self.hablar("Iniciemos con el brazo izquierdo")
        effector   = "LArm"
        space      = motion.FRAME_ROBOT #usarla para brazos
        #space      =  motion.FRAME_WORLD usarla para torso

        # x, y, z            wx.  wy.  wz
        path       = [
          [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # punto 1
          [0.0, +0.00, +0.04, 0.0, 0.0, 0.0],        # punto 2
          [0.0, +0.04, +0.00, 0.0, 0.0, 0.0],        # punto 3
          [0.0, +0.00, -0.02, 0.0, 0.0, 0.0],        # punto 4
          [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # punto 5
          [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]]        # punto 6
        axisMask   = almath.AXIS_MASK_VEL                #controlar la posición
        times      = [0.5, 1.0, 2.0, 3.0, 4.0, 4.5] # segundos
        isAbsolute = False
        self.motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("Ahora probemos con el brazo derecho")
        effector   = "RArm"
        space      = motion.FRAME_ROBOT
        path       = [
         [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # punto 1
         [0.0, +0.00, +0.04, 0.0, 0.0, 0.0],        # punto 2
         [0.0, +0.04, +0.00, 0.0, 0.0, 0.0],        # punto 3
         [0.0, +0.00, -0.02, 0.0, 0.0, 0.0],        # punto 4
         [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # punto 5
         [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]]        # punto 6
        axisMask   = almath.AXIS_MASK_VEL                 #controlar la posición
        times      = [0.5, 1.0, 2.0, 3.0, 4.0, 4.5] # segundos
        isAbsolute = False
        self.motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("Perfecto hemos terminado")
        
    def estirarPiernas(self):
        self.postura.goToPosture("StandInit", 2.0)
        self.hablar("Ahora vamos a sentarnos y estirar las piernas, repitan conmigo")
        self.postura.goToPosture("SitRelax", 1.0)
        time.sleep(10)
        self.postura.goToPosture("StandInit", 2.0)
        
    def arribaAbajo(self):
        self.hablar("ahora estamos listos para hacer un par de sentadillas")
        self.hablar("vamos a ponernos de rodillas y levantarnos un par de veces")
        self.postura.goToPosture("StandInit", 2.0)
        self.postura.goToPosture("Crouch", 2.0)
        self.postura.goToPosture("StandZero", 2.0)
        self.hablar("no se olviden de respirar un poco")
        time.sleep(5)
        self.postura.goToPosture("Crouch", 2.0)
        self.postura.goToPosture("StandZero", 2.0)
        time.sleep(5)
        self.hablar("excelente trabajo")
        self.postura.goToPosture("StandInit", 2.0)
        
    def despedida(self):
        self.postura.goToPosture("sit", 2.0)
        self.hablar("Muy bien es hora de despedirnos, esto ha sido todo por ahora")
        self.hablar("Les agradezco su tiempo en la rutina del día de hoy, de educación física, los espero en el próximo episodio de su programa favorito, mañana saludable con NAO")
        self.postura.goToPosture("StandInit", 2.0)
    
if __name__ == "__main__":
    robotIp = "127.0.0.1"
    robotPort = 62284
    robot = Instructor(robotIp, robotPort)
    robot.caminar()
    robot.hablar("hola mi nombres es Nao y hoy voy a hacer de profesor de educacion fisica, a continuacion dare una clase de estiramientos, siganme y repitan mis ejercicios para calentar")
    robot.hablar("Muy bien empecemos, Vamos a estirar los brazos, levanten los brazos conmigo ")
    robot.moverBrazosArriba()
    robot.hablar("Este estiramiento básico nos va a ayudar a despertar un poco del sueño")
    robot.relajarCabezaIzquierda()
    robot.relajarCabezaDerecha()
    robot.hablar("perfecto estudiantes, hasta el momento lo han hecho muy bien, mucho mejor que yo")
    robot.hablar("ahora que les parece un ejercicio un poco mas movido")
    robot.girarBrazos()
    robot.hablar("muy bien, han estado excelente el dia de hoy, ahora estiraremos nuestras piernas un poco")
    robot.estirarPiernas()
    robot.arribaAbajo()
    robot.despedida()
