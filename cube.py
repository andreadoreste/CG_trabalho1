#!/usr/bin/env python

"""This demonstrates a simple rotating cube in 3D using OpenGL.
"""

import sys
import os
import linecache
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#from main import cube
from glut_loader import loader

# Andrea mexeu
#results = loader('cube.ply')
#number_of_vertex = results[0]
#number_of_faces = results[1]
#vertex=results[2]
#faces=results[3]
#Andrea terminou de mexer


ROTATE_X = 0.0
ROTATE_Y = 0.0
ROTATE_Z = 0.0


def InitGL(Width, Height): #def init

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)  # glDepthFunc(GL_LEQUAL)
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_POLYGON_SMOOTH)
    glEnable(GL_BLEND)
    # Wire frame:  glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glShadeModel(GL_SMOOTH)  # glShadeModel(GL_FLAT)
    ReSizeGLScene (Width,Height)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


def ReSizeGLScene (width, height): #def reshape

    if height==0:
        height=1
    glViewport (0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # set perspective and aspect ratio.
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,80,200,0,0,0,0,1,0)

def input_handler (*args):

    """args: a tuple of (key, x, y)"""

    global ROTATE_X,ROTATE_Y,ROTATE_Z
    if args[0] == '\033' or args[0] == 'q':
        sys.exit()
    elif args[0] == 'h':
        ROTATE_Y = ROTATE_Y - 2.333
    elif args[0] == 'l':
        ROTATE_Y = ROTATE_Y + 2.333
    elif args[0] == 'j':
        ROTATE_X = ROTATE_X + 2.333
    elif args[0] == 'k':
        ROTATE_X = ROTATE_X - 2.333
    elif args[0] == 'i':
        ROTATE_Z = ROTATE_Z - 2.333
    elif args[0] == 'u':
        ROTATE_Z = ROTATE_Z + 2.333
    if ROTATE_X > 360 or ROTATE_X == 0 or ROTATE_X < -360:
        ROTATE_X = 0.0
    if ROTATE_Y > 360 or ROTATE_Y == 0 or ROTATE_Y < -360:
        ROTATE_Y = 0.0
    if ROTATE_Z > 360 or ROTATE_Z == 0 or ROTATE_Z < -360:
        ROTATE_Z = 0.0
    DrawGLScene()


def DrawGLScene(): #def display

        global ROTATE_X,ROTATE_Y,ROTATE_Z

        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        
        glTranslatef(0.0,0.0,-6.0)
        #glRotatef(ROTATE_X,1.0,0.0,0.0)
        #glRotatef(ROTATE_Y,0.0,1.0,0.0)
        #glRotatef(ROTATE_Z,0.0,0.0,1.0)

        glPushMatrix()
        #glBegin(GL_QUADS)
        #glColor4f(0.4,0.4,0.4,1.0) # 0.666)
        #glVertex3f( 1.5, 1.5,-1.5)
        #glVertex3f( 1.5, 1.5, 1.5)
        #glVertex3f( 1.5,-1.5, 1.5)
        #glVertex3f( 1.5,-1.5,-1.5)

        # side 1: blue
        
        glBegin(GL_QUADS)
        glColor4f(0.0,0.0,1.0,1.0) # 0.666)
        # upper right -> upper left -> lower left -> lower right
        glVertex3f( 1.0, 1.0,-1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f( 1.0, 1.0, 1.0)
        glEnd()

<<<<<<< HEAD
        #glColor4f(0.0,1.0,0.0,1.0) # 0.666)
        #glBegin(GL_QUADS)
        # upper right -> upper left -> lower left -> lower right
        #glVertex3f( 1.0,-1.0, 1.0)
        #glVertex3f(-1.0,-1.0, 1.0)
        #glVertex3f(-1.0,-1.0,-1.0)
        #glVertex3f( 1.0,-1.0,-1.0)
        #glEnd()
        #glPushMatrix()        
        # red
=======
        # side 2: green
        glBegin(GL_QUADS)
        glColor4f(0.0,1.0,0.0,1.0) # 0.666)
        # upper right -> upper left -> lower left -> lower right
        glVertex3f( 1.0,-1.0, 1.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f( 1.0,-1.0,-1.0)
        glEnd()

        # side 3: red
>>>>>>> origin/master
        glBegin(GL_QUADS)
        glColor4f(1.0,0.0,0.0,1.0) # 0.666)
        # upper right -> upper left -> lower left -> lower right
        glVertex3f( 1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0) # arestas
        glVertex3f(-1.0,-1.0, 1.0) # que ligam face vermelha e branca
        glVertex3f( 1.0,-1.0, 1.0)
        glEnd()
<<<<<<< HEAD
        
        glPushMatrix()
        #WHITE
        p = [-1.0,-1.0,1.0]
        axis = [0.0,2.0,0.0]
        #print axis.x,axis.y,axis.z
        translateAndRotate(90,p,axis)
        #glTranslatef(-1.0,-1.0,1.0)
        #glRotatef(90,0.0,2.0,0.0)
        #glTranslatef(+1.0,+1.0,-1.0)
        
        glBegin(GL_QUADS)
        glColor4f(1.0,1.0,1.0,1.0) # 0.666)
        # upper right -> upper left -> lower left -> lower right
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glEnd()


        #glTranslatef(-1.0,-1.0,1.0)
        #glRotatef(90,0.0,2.0,0.0)
        #glTranslatef(+1.0,+1.0,-1.0)
        
        #YELLOW
        glPushMatrix()
        glTranslatef(-1.0,-1.0,-1.0)
        glRotatef(90,0.0,2.0,0.0)
        glTranslatef(+1.0,+1.0,+1.0)
        
=======

        # side 4: yellow
>>>>>>> origin/master
        glBegin(GL_QUADS)
             # 0.666)
        # upper right -> upper left -> lower left -> lower right
        glVertex3f( 1.0,-1.0,-1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f( 1.0, 1.0,-1.0)
        glEnd()
        # side 5: white
        #glTranslatef(0.0,0.0,6.0)
        glTranslatef(+1.0,+1.0,-1.0)
        glRotatef(90,0.0,2.0,0.0)
        glTranslatef(-1.0,-1.0,1.0)
        #glTranslatef(0.0,0.0,-6.0)
        #glPushMatrix()
        glBegin(GL_QUADS)
        #glLoadIdentity()
        #glRotatef(90,-1.0,1.0,1.0)
        glColor4f(1.0,1.0,1.0,1.0) # 0.666)
        # upper right -> upper left -> lower left -> lower right
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f(-1.0,-1.0, 1.0)
<<<<<<< HEAD
        glEnd()'''

        glPushMatrix()
        #CYAN
        glTranslatef(1.0,-1.0,-1.0)
        glRotatef(90,0.0,2.0,0.0)
        glTranslatef(-1.0,1.0,1.0)
        
=======
        glEnd()
        #glPopMatrix()
        #glPushMatrix()
        glLoadIdentity()
        # side 6: cyan
        glRotatef(0,0.0,0.0,0.0)
>>>>>>> origin/master
        glBegin(GL_QUADS)
        glColor4f(0.0,1.0,1.0,1.0) # 0.666)
        # upper right -> upper left -> lower left -> lower right
        glVertex3f( 1.0, 1.0,-1.0)
        glVertex3f( 1.0, 1.0, 1.0)
        glVertex3f( 1.0,-1.0, 1.0)
        glVertex3f( 1.0,-1.0,-1.0)

        glEnd()
<<<<<<< HEAD
        glPushMatrix()
        #blue
        glTranslatef(1.0,1.0,1.0)
        glRotatef(-90,0,0,2)
        glTranslatef(-1.0,-1.0,-1.0)

        glBegin(GL_QUADS)
        glColor4f(0.0,0.0,1.0,1.0) # 0.666)
        
        # upper right -> upper left -> lower left -> lower right
        glVertex3f( 1.0, 1.0,-1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f( 1.0, 1.0, 1.0)
        glEnd()
        
        glPopMatrix()
        #green
        glTranslatef(1.0,-1.0,-1.0)
        glRotatef(90,0,0,2)
        glTranslatef(-1.0,1.0,1.0)
        glColor4f(0.0,1.0,0.0,1.0) # 0.666)
        glBegin(GL_QUADS)
        #upper right -> upper left -> lower left -> lower right
        glVertex3f( 1.0,-1.0, 1.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f( 1.0,-1.0,-1.0)
        glEnd()





=======
>>>>>>> origin/master
        glPopMatrix()
        glutSwapBuffers()
        

def main():

        glutInit(sys.argv)
        # pyopengl bug causes a "Segmentation fault" when glutCreateWindow is called after glutInitDisplayMode.
        window = glutCreateWindow('cube')
<<<<<<< HEAD
        glutInitWindowSize(800,800)
=======
        glutInitWindowSize(690,690)
>>>>>>> origin/master
        glutInitWindowPosition(0,0)
        # Setting only GLUT_DOUBLE seems to have the same effect. What are the others good for?
        glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_DOUBLE | GLUT_DEPTH)
        glutDisplayFunc(DrawGLScene)
        #glutIdleFunc uses 50% of the CPU while "idle". Seems to run fine without it.
#        glutIdleFunc(DrawGLScene)
        glutReshapeFunc(ReSizeGLScene)
        #glutKeyboardFunc(input_handler)
        #glutFullScreen()
<<<<<<< HEAD
        InitGL(800,800)
=======
        InitGL(690,690)
>>>>>>> origin/master
        glutMainLoop()


if __name__ == "__main__":

        main()



