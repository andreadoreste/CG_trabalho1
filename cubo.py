from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():

	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(100,100)
	glutCreateWindow("hello")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(reshape)
	#glutKeyboardFunc(keyboard)
	glutMainLoop()

def init():
	#glClearColor(RED,GREEN,BLUE,ALPHA)
	glClearColor(0.0,0.0,0.0,0.0)
	#glOrtho(GLdouble left, GL_double right, GLdouble bottom, GLdouble top,GLdouble zNear, GLdouble zFar)
	glOrtho(0.0,256,0,256,-1,1) #glOrtho define o volume de recorte

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glPushMatrix()
	
	glPushMatrix()
	glTranslatef(-2.0,0.0,0.0) #leva a origem do sistema de coordenadas para o ponto
	glScalef(3.0,2.0,5.0) #amplia o sistema de coordenadas
	glutWireCube(1.0)
	glPopMatrix()

	glPopMatrix()
	glutSwapBuffers()

	#Desenhar um poligono branco
	
def reshape(w,h):
	#glViewport(0,0, (GLsizei) w,(GLsizei) h,1.0,20.0)
	glViewport(0,0,w,h)
	glMatrixMode (GL_PROJECTION)
	glLoadIdentity()
	#gluPerspective(65.0, (GLfloat) w/(GLfloat) h,1.0,20.0)
	gluPerspective(65.0, w/h,1.0,20.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glTranslatef(0.0,0.0,-10.0)

#def keyboard():	

main()