#! /usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

def Cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
	glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(800,600)
	gluPerspective(45,(800/600),0.1,50.0)
	#glTranslatef(0.0,0.0,-5)

	glutCreateWindow("hello")
	
	#glRotatef(1,3,1,1)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glutDisplayFunc(Cube)
	glutMainLoop()

main()




