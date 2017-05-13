from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():

	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(256,256)
	glutInitWindowPosition(100,100)
	glutCreateWindow("hello")
	init()
	glutDisplayFunc(display)
#	glutKeyboardFunc(keyboard)
	glutMainLoop()

def init():

	glClearColor(1.0,1.0,1.0,1.0)
	glOrtho(0.0,256,0,256,-1,1)

def display():
	glClear(GL_COLOR_BUFFER_BIT)

	#Desenhar um poligono branco
	glColor3f(0,0,0)
	glBegin(GL_LINES)
	glVertex2i(40,200)
	glVertex2i(200,10)
	glEnd()

	glFlush()

#def keyboard():	

main()