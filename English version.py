# -*- encoding: UTF-8 -*-

import motion
import sys
from naoqi import ALProxy
import almath
import time

#init the robot
class Instructor:


    def __init__(self, robotIp, robotPort):
        self.robotIp = robotIp
        self.robotPort = robotPort
        self.motionProxy = ALProxy("ALMotion", self.robotIp, self.robotPort)
        self.posture = ALProxy("ALRobotPosture", self.robotIp, self.robotPort)
        self.word = ALProxy("ALTextToSpeech", self.robotIp, self.robotPort)
        self.move = ALProxy("ALMotion", self.robotIp, self.robotPort)
        
    #set the robot stiffness on to let him move 
    def StiffnessOn(proxy):
        pNames = "Body" 
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

        
    def talk(self, texto):        #generic talk method instead of say
       self.word.say(texto)
       

    def walk(self): 
        self.move.moveInit()   #put the robot in the postition, init the movement process
        self.move.moveTo(0.3, 0, 0)        #move the robot as you needed, in my case was needed 0.5 in X, 0 in Y and 0 on Z
        
    
        
    def raiseArm(self): #move arm upward method
        self.posture.goToPosture("StandInit", 2.0)
        def StifnessOn(proxy):
         pNames = "Body" 
         pStiffnessLists = 1.0
         pTimeLists = 1.0
         proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Let's start with the right arm, lift it up and hold for a few seconds.")
        #Right arm
        effector   = "RArm"
        space      = motion.FRAME_ROBOT
        path       = [
           [4.44, 0.00, 0.00, 0.0, 0.0, 0.0],       # joint 1
           [3.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # joint 2
           [4.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # joint 3
           [1.0, 2.00, 0.00, 0.0, 0.0, 0.0],        # joint 4
           [2.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # joint 5
           [0.0, 2.00, 0.00, 0.0, 0.0, 0.0]]        # joint 6
        axisMask   = almath.AXIS_MASK_VEL
        times      = [4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        isAbsolute = False
        self.motionProxy.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)
        time.sleep(10)
        self.posture.goToPosture("StandInit", 2.0)
        #left arm
        def StifnessOn(proxy):
         pNames = "Body" 
         pStiffnessLists = 1.0
         pTimeLists = 1.0
         proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Let's go with the left one, but raise the arm higher.")
        effector   = "LArm"
        space      = motion.FRAME_ROBOT
        path       = [
        [4.4, 0.00, 0.00, 0.0, 0.0, 0.0],        # 1
        [3.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # 2
        [4.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # 3
        [1.0, 2.00, 0.00, 0.0, 0.0, 0.0],        # 4
        [2.0, 0.00, 0.00, 0.0, 0.0, 0.0],        # 5
        [0.0, 2.00, 0.00, 0.0, 0.0, 0.0]]        # 6
        axisMask   = almath.AXIS_MASK_VEL                             #control the position
        times      = [4.0, 5.0, 6.0, 7.0, 8.0, 9.0] # seconds values
        isAbsolute = False
        self.motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)
        time.sleep(10)
        self.posture.goToPosture("StandInit", 2.0)
        
        
        
    def relaxHeadLeft(self):   #method to simulate that nao is relaxing the head in the left way
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Now we're going to relax our head with a series of movements to both sides, follow me.")
        names      = ["Head"]
        angleLists = [1.1667,1.1667]
        timeLists  = [1.0, 1.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names  = ["HeadYaw","HeadPitch"]
        self.motionProxy.setStiffnesses("Head", 0.0)
        time.sleep(10)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Now a littble bit more")
        self.posture.goToPosture("StandInit", 2.0)
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.posture.goToPosture("StandInit", 2.0)
        names      = ["Head"]
        angleLists = [1.8800,1.8800]
        timeLists  = [2.0, 2.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names  = ["HeadYaw","HeadPitch"]
        self.motionProxy.setStiffnesses("Head", 0.0)
        time.sleep(10)
        self.posture.goToPosture("StandInit",0.5)
        self.talk("Perfect we are done")
    
    def relaxHeadRight(self): #same but right way
        self.motionProxy = ALProxy("ALMotion", self.robotIp, self.robotPort)
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("now let's move the head to the right")
        names      = ["Head"]
        angleLists = [-1.1667,-1.1667]
        timeLists  = [1.0, 1.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names  = ["HeadYaw","HeadPitch"]
        self.motionProxy.setStiffnesses("Head", 0.0)
        time.sleep(10)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Now let's stretch a little more.")
        self.posture.goToPosture("StandInit",2.0)
        self.motionProxy.setStiffnesses("Head", 1.0)
        self.posture.goToPosture("StandInit", 2.0)
        names      = ["Head"]
        angleLists = [-1.8800,-1.8800]
        timeLists  = [2.0, 2.2]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names  = ["HeadYaw","HeadPitch"]
        self.motionProxy.setStiffnesses("Head", 0.0)
        time.sleep(10)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Perfect we are done")
    
    def rotateArm(self):
        # start the stiffnes
        def StifnessOn(proxy):
         pNames = "Body" 
         pStiffnessLists = 1.0
         pTimeLists = 1.0
         proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Now we're going to rotate our arms. This movement will help with circulation in our body.")
        self.talk("let's start with the left arm")
        effector   = "LArm"
        space      = motion.FRAME_ROBOT #use this frame to the arms
        #space      =  motion.FRAME_WORLD this other for the chest if you need that later

        # x, y, z            wx.  wy.  wz
        path       = [
          [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # 1
          [0.0, +0.00, +0.04, 0.0, 0.0, 0.0],        # 2
          [0.0, +0.04, +0.00, 0.0, 0.0, 0.0],        # 3
          [0.0, +0.00, -0.02, 0.0, 0.0, 0.0],        # 4
          [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # 5
          [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]]        # 6
        axisMask   = almath.AXIS_MASK_VEL                #control the position
        times      = [0.5, 1.0, 2.0, 3.0, 4.0, 4.5] # seconds
        isAbsolute = False
        self.motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Ahora probemos con el brazo derecho")
        effector   = "RArm"
        space      = motion.FRAME_ROBOT
        path       = [
         [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # 1
         [0.0, +0.00, +0.04, 0.0, 0.0, 0.0],        # 2
         [0.0, +0.04, +0.00, 0.0, 0.0, 0.0],        # 3
         [0.0, +0.00, -0.02, 0.0, 0.0, 0.0],        # 4
         [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # 5
         [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]]        # 6
        axisMask   = almath.AXIS_MASK_VEL                 #control the position
        times      = [0.5, 1.0, 2.0, 3.0, 4.0, 4.5] # seconds
        isAbsolute = False
        self.motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Perfect we just finished")
        
    def stretchLegs(self): #stretch legs method :)
        self.posture.goToPosture("StandInit", 2.0)
        self.talk("Now let's sit down and stretch our legs. Repeat with me.")
        self.posture.goToPosture("SitRelax", 1.0)
        time.sleep(10)
        self.posture.goToPosture("StandInit", 2.0)
        
    def upDown(self): #squats method
        self.talk("we are ready to do some squats")
        self.talk("We're going to get on our knees and stand up a couple of times.")
        self.posture.goToPosture("StandInit", 2.0)
        self.posture.goToPosture("Crouch", 2.0)
        self.posture.goToPosture("StandZero", 2.0)
        self.talk("don't forget to breath")
        time.sleep(5)
        self.posture.goToPosture("Crouch", 2.0)
        self.posture.goToPosture("StandZero", 2.0)
        time.sleep(5)
        self.talk("excellent work")
        self.posture.goToPosture("StandInit", 2.0)
        
    def despedida(self):
        self.posture.goToPosture("sit", 2.0)
        self.talk("Alright, it's time to say goodbye. That's all for now.")
        self.talk("I appreciate your time in today's physical education routine. I look forward to seeing you in the next episode of your favorite program, Healthy Morning with NAO.")
        self.posture.goToPosture("StandInit", 2.0)
    
if __name__ == "__main__":
    robotIp = "127.0.0.1"
    robotPort = 62284
    robot = Instructor(robotIp, robotPort)
    robot.walk()
    robot.talk("Hello, my name is Nao, and today I'm going to be your physical education teacher. I will now give a stretching class. Follow me and repeat my exercises to warm up.")
    robot.talk("Alright, let's begin. We're going to stretch our arms, so lift your arms with me.")
    robot.raiseArm()
    robot.talk("This basic stretch will help us wake up a little from sleep.")
    robot.relaxHeadLeft()
    robot.relaxHeadRight()
    robot.talk("Perfect, students! So far, you have done really well, much better than me.")
    robot.talk("Now, how about a more dynamic exercise?")
    robot.rotateArm()
    robot.talk("Very good, you've been excellent today. Now, let's stretch our legs a bit.")
    robot.stretchLegs()
    robot.upDown()
    robot.despedida()
