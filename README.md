# Robotifest-NAO
This was the code winner of a Robotifest NAO Python challenge in 2022
The challenge consts of a rutine, which NAO robot pretend to be the instructor.
Here was the main idea...

Introduction:
NAO thanks you for being back on a healthy morning with NAO, and mentions that he will now give a stretching class so that the audience and listeners can follow along and have a better morning.

Development:

"Hello, my name is Nao, and today I will be your physical education teacher. I will now give a stretching class. Please follow me and repeat my exercises to warm up."
"Alright, let's begin. Let's stretch our arms. Lift your arms with me:"
a- "Let's stretch our arms. Lift your arms with me."
"This basic stretch will help us wake up a bit from sleep."
// Nao raises his arms for about 5 seconds, the left one doesn't work well.
b- "Now let's relax our head a bit and take our head with one arm and pull it to the side. Let's hold it like that for about 10 seconds."
// On both the left and right sides.
c- "Let's rotate our arms..."
// NAO assumes the "StandInit" position, raises his hands until they are in line with his body, and when they are fully extended, he will make 5 clockwise rotations // 15 seconds
d. "Let's stretch our legs for about 10 seconds."
// Put NAO in the "sitRelax" pose to simulate a stretch in that position. This will take about 1 minute and something...
e. "Now let's do some squats."
// Using the crouch and stand zero poses.
f. NAO says goodbye.
Conclusion:
"Alright, it's time to say goodbye. That's all for now."
"I appreciate your time in today's physical education routine. I'll see you in the next episode of your favorite program, Healthy Morning with NAO."
// Make the arms go to the head and then throw the arms out, simulating a stretching motion.

NOTE: the main program need to be on Python 2.7 to run as the naoqi version its compatible with this py version, also you may see aldebaran repository here: 
http://doc.aldebaran.com/1-14/dev/python/index.html
and you must need to install a few things before you want to attempt it. Also for the Virtual robot in choregraphe.
