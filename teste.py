from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
	
	glMatrixMode(GL_MODELVIEW)
	#glLoadIdentity()
	#Limpar todos os pixels
	glClear(GL_COLOR_BUFFER_BIT)

	#Desenhar um poligono branco
	glColor3f(1.0,1.0,1.0)
	#glTranslatef(0.5,0.5,0.0)
	glRotatef(60,0.0,1.0,.0)
	#glTranslatef(-0.5,-0.5,0.0)
	glBegin(GL_QUADS)
	glVertex3f(0.0,0.0,0.0)
	glVertex3f(0.5,0.0,0.0)
	glVertex3f(0.5,0.5,0.0)
	glVertex3f(0.0,0.5,0.0)
	glEnd()

	glFlush()

def init():

	#selecionar cor de fundo
	glClearColor(0.0,0.0,0.0,0.0)

	#Inicializar sistema de visualizacao
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	#pode dar problema aqui
	#glOrtho(5.0,5.0,0.0,5.0,5.0,5.0)

if __name__ == '__main__':
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(400,350)
	glutInitWindowPosition(100,100)
	glutCreateWindow("hello")
	init()
	glutDisplayFunc(display)
	glutMainLoop()

