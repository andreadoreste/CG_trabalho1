#!/usr/bin/env python

import sys
import os
import linecache

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from main import cube
from glut_loader import loader

# Andrea mexeu
results = loader('cube.ply')
number_of_vertex = results[0]
number_of_faces = results[1]
vertex=results[2]
faces=results[3]
#Andrea terminou de mexer
"""
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
"""

def init():

	glClearColor(0.0,0.0,0.0,0.0)
	glClearDepth(1.0)
	glDepthFunc(GL_LESS)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_POLYGON_SMOOTH)


def display():
	glBegin(GL_QUADS)
	cube(vertex,faces)
	glEnd()
	glPopMatrix()
	glutSwapBuffers()




def reshape(width, height):

	glViewport(0,0,width,height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glTranslatef(0.0,0.0,-6.0)




def main():
	glutInit()
	glutCreateWindow("cube")
	glutInitWindowSize(480,272)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_DOUBLE | GLUT_DEPTH)
	glutDisplayFunc(display)
	glutReshapeFunc(reshape)
	init()
	glutMainLoop()


main() 
