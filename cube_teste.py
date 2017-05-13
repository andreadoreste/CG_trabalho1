#!/usr/bin/env python

"""This demonstrates a simple rotating cube in 3D using OpenGL.
"""

import sys
import os
import linecache
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

from main import *
from glut_loader import loader
#from matrix_opengl import *
from matrix import *


# Andrea mexeu
results = loader('cube.ply')
number_of_vertex = results[0]
number_of_faces = results[1]
vertex=results[2]
faces=results[3]
#Andrea terminou de mexer


ROTATE_X = 0.0
ROTATE_Y = 0.0
ROTATE_Z = 0.0

colors = [(0.0,1.0,0.0,1.0),(0.0,0.0,1.0,1.0),(0.0,1.0,1.0,1.0),(1.0,1.0,1.0,1.0),(1.0,1.0,0.0,1.0),(1.0,0.0,0.0,1.0)]
faces_matrix = []
for i in range(6):
    faces_matrix.append(identity())
print faces_matrix


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
        glRotatef(ROTATE_X,1.0,0.0,0.0)
        glRotatef(ROTATE_Y,0.0,1.0,0.0)
        glRotatef(ROTATE_Z,0.0,0.0,1.0)

        #dfs: [1,2,0,3,4,5]

        glPushMatrix()
        #green
        #face 1: 
        glColor4fv(colors[0])
        opened_cube(vertex,faces,3)
        glBegin(GL_QUADS)
        glVertex3fv(vertex[5])
        glVertex3fv(vertex[4])
        glVertex3fv(vertex[7])
        glVertex3fv(vertex[6])
        glEnd()
        #glPopMatrix()
        #T = glGetDoublev(GL_MODELVIEW_MATRIX) 
        #faces_matrix.insert(0,T)
        #print T
        glPopMatrix()
        #start face 2
        edge = compare(faces[1],faces[2])
        print edge
        v1= edge[0]
        v1 = vertex[v1]
        #v1 = Point(v1[0],v1[1],v1[2])
        #print v1
        v2 = edge[1]
        v2 = vertex[v2]
        #v2 = Point(v2[0],v2[1],v2[2])
        #print v2
        
        #face 2:
        glLoadIdentity()
        axis = difference(v1,v2)
        axis= Point(axis[0],axis[1],axis[2])
        
        v1 = Point(v1[0],v1[1],v1[2])
        v2 = Point(v2[0],v2[1],v2[2])
   #     print'v1'
 #       print (v1.x,v1.y,v1.z)

    #    print "axis"
  #      print (axis.x,axis.y,axis.z)
        #t1 = translate(-v1.x,-v1.y,-v1.z)
        #t2 = rotate(-90,axis.x,axis.y,axis.z)
        #t2 = translate(v2.x,v2.y,v2.z)
        #        glTranslatef(-1.5,0.0,-6.0);
        #axis = difference(vertex[4],vertex[5])
        #t1 = translate(0.0,0.0,-6.0)
        t =translateAndRotate(90,v1,axis)
     #   print t

#        v6 = Point(vertex[6][0],vertex[6][1],vertex[6][2])
#        v2 = Point(vertex[2][0],vertex[2][1],vertex[2][2])
#        v1 = Point(vertex[1][0],vertex[1][1],vertex[1][2])
#        v5 = Point(vertex[5][0],vertex[5][1],vertex[5][2])
        
        #t6 = translateAndTransform(t,v6)
        #print "t6"
        #print t6

        #t2 = translateAndTransform(t,v2)
        #t1 = translateAndTransform(t,v1)
        #t5 = translateAndTransform(t,v5) 
        
        #t = faces_matrix[2]*t
        tr = faces_matrix[0]*t
        #print "T"
        #print t
        #print "TR"
        print tr
        #print faces_matrix[0]
        glMultMatrixf(tr.view(type=np.ndarray))

        glPushMatrix()
        glPopMatrix()
        print "T"
        T = glGetDoublev(GL_MODELVIEW_MATRIX)
        #blue
        #desenha
        
        #T = glGetDoublev(GL_MODELVIEW_MATRIX)
        print T
        #print faces_matrix[0]
        print 
        #translateAndRotate(90,v1,axis)
        glPushMatrix()
        glPushMatrix()
        glColor4fv(colors[1])
        
        glBegin(GL_QUADS)
        glVertex3fv(vertex[6])
        glVertex3fv(vertex[2])
        glVertex3fv(vertex[1])
        glVertex3fv(vertex[5])
        glEnd()
        T = glGetDoublev(GL_MODELVIEW_MATRIX)

        glPopMatrix()
        
        #start face 0

        edge = compare(faces[2],faces[0])
        print edge
        v1= edge[0]
        v1 = vertex[v1]
        print v1
        v2 = edge[1]
        v2 = vertex[v2]
        print v2
        
        #cyan
        #face 0:
        axis = difference(v2,v1)
        print axis
        #axis = difference(vertex[4],vertex[5])
        translateAndRotate(90,v1,axis)


        #desenha face 0
        glPushMatrix()
        glColor4fv(colors[2])
        glBegin(GL_QUADS)
        glVertex3fv(vertex[0])
        glVertex3fv(vertex[1])
        glVertex3fv(vertex[2])
        glVertex3fv(vertex[3])
        glEnd()
        glPopMatrix()
        #start face 3
        edge = compare(faces[0],faces[3])
        print edge
        v1= edge[0]
        v1 = vertex[v1]
        print v1
        v2 = edge[1]
        v2 = vertex[v2]
        print v2
        #white
        #face 3:
        axis = difference(v1,v2)
        print axis
        #axis = difference(vertex[4],vertex[5])
        translateAndRotate(90,v1,axis)


        #desenha face 3
        glPushMatrix()
        glColor4fv(colors[3])
        glBegin(GL_QUADS)
        glVertex3fv(vertex[3])
        glVertex3fv(vertex[7])
        glVertex3fv(vertex[4])
        glVertex3fv(vertex[0])
        glEnd()
        glPopMatrix()
        #glPushMatrix()
        #start face 4
        edge = compare(faces[3],faces[4])
        print edge
        v1= edge[0]
        v1 = vertex[v1]
        print v1
        v2 = edge[1]
        v2 = vertex[v2]
        print v2
        
        #teste
        t =find_angle(v2,v1)
        print t
        if (t==1):
            axis =(0,0,2)    
        if (t==-1):
            axis =(0,0,-2)
        #face 4:
        #axis = difference(v2,v1)
        #axis =(0,0,2)
        print axis
        #axis = difference(vertex[4],vertex[5])
        translateAndRotate(90,v1,axis)


        #desenha face 4
        glPushMatrix()
        glColor4fv(colors[4])
        glBegin(GL_QUADS)
        glVertex3fv(vertex[7])
        glVertex3fv(vertex[3])
        glVertex3fv(vertex[2])
        glVertex3fv(vertex[6])
        glEnd()
        glPopMatrix()
        #glPopMatrix()

        #start face 5
        edge = compare(faces[3],faces[5])
        print edge
        v1= edge[0]
        v1 = vertex[v1]
        print v1
        v2 = edge[1]
        v2 = vertex[v2]
        print v2
        
        #face 5:
        axis = difference(v2,v1)
        print axis
        #axis = difference(vertex[4],vertex[5])
        translateAndRotate(90,v1,axis)


        #desenha face 5
        glPushMatrix()
        glPushMatrix()
        glColor4fv(colors[5])
        glBegin(GL_QUADS)
        glVertex3fv(vertex[5])
        glVertex3fv(vertex[1])
        glVertex3fv(vertex[0])
        glVertex3fv(vertex[4])
        glEnd()
        glPopMatrix()
        #glColor4f(1.0,0.0,0.0,1.0)
        #opened_cube(vertex,faces,1)
          
                 
        glPopMatrix()
        glutSwapBuffers()
        

def main():

        glutInit(sys.argv)
        # pyopengl bug causes a "Segmentation fault" when glutCreateWindow is called after glutInitDisplayMode.
        window = glutCreateWindow('cube')
        glutInitWindowSize(800,800)
        glutInitWindowPosition(0,0)
        # Setting only GLUT_DOUBLE seems to have the same effect. What are the others good for?
        glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_DOUBLE | GLUT_DEPTH)
        glutDisplayFunc(DrawGLScene)
        #glutIdleFunc uses 50% of the CPU while "idle". Seems to run fine without it.
#        glutIdleFunc(DrawGLScene)
        glutReshapeFunc(ReSizeGLScene)
        glutKeyboardFunc(input_handler)
        #glutFullScreen()
        InitGL(800,800)
        glutMainLoop()


if __name__ == "__main__":

        main()

#colors = [glColor4f(0.0,1.0,0.0,1.0),glColor4f(0.0,0.0,1.0,1.0),glColor4f(0.0,1.0,1.0,1.0),glColor4f(1.0,1.0,1.0,1.0),glColor4f(1.0,1.0,0.0,1.0),glColor4f(1.0,0.0,0.0,1.0)]

'''
0 -> green
1 -> blue
2 -> cyan
3 -> white
4 -> yellow
5 -> red
'''