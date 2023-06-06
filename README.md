# Robotifest-NAO
This is the English notes, Spanish notese will be down below

NOTE: check for you Language version, i will upload it Spanish (Original) and English
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

SPANISH NOTES:
NOTA: Verifique la versión de idioma que desea, subiré la versión en español (original) e inglés. Este fue el código ganador de un desafío de Python de Robotifest NAO en 2022. El desafío consiste en una rutina en la que el robot NAO pretende ser el instructor. Aquí está la idea principal...

Introducción: NAO les agradece por estar de vuelta en una mañana saludable con NAO y menciona que ahora dará una clase de estiramientos para que el público y los oyentes puedan seguir y tener una mejor mañana.

Desarrollo:

"Hola, mi nombre es Nao y hoy seré su profesor de educación física. Ahora daré una clase de estiramientos. Por favor, síganme y repitan mis ejercicios para calentar". "Muy bien, vamos a empezar. Vamos a estirar los brazos. Levanten los brazos conmigo:" a- "Vamos a estirar los brazos. Levanten los brazos conmigo." "Este estiramiento básico nos ayudará a despertarnos un poco del sueño". // Nao levanta los brazos durante aproximadamente 5 segundos, el izquierdo no funciona bien. b- "Ahora vamos a relajar un poco la cabeza y tomen su cabeza con un brazo y jálala hacia un lado. Mantengámoslo así durante unos 10 segundos". // Tanto en el lado izquierdo como en el derecho. c- "Vamos a girar los brazos..." // NAO asume la posición "StandInit", levanta sus manos hasta que estén alineadas con su cuerpo y cuando estén completamente extendidas, hará 5 giros en sentido horario // 15 segundos d. "Vamos a estirar las piernas durante unos 10 segundos". // Colocar a NAO en la pose "sitRelax" para simular un estiramiento en esa posición. Esto tomará aproximadamente 1 minuto y algo... e. "Ahora hagamos algunas sentadillas". // Utilizando las poses de agacharse y ponerse de pie. f. NAO se despide. Conclusión: "Muy bien, es hora de despedirnos. Eso es todo por ahora". "Agradezco su tiempo en la rutina de educación física de hoy. Nos vemos en el próximo episodio de su programa favorito, Mañana Saludable con NAO". // Hacer que los brazos vayan hacia la cabeza y luego lanzar los brazos hacia afuera, simulando un movimiento de estiramiento.

NOTA: el programa principal debe estar en Python 2.7 para que se ejecute, ya que la versión de naoqi es compatible con esta versión de Python. También puedes ver el repositorio de Aldebaran aquí: http://doc.aldebaran.com/1-14/dev/python/index.html y es posible que necesite instalar algunas cosas antes de intentarlo. También para el robot virtual en Choregraphe.
