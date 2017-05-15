from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import copy
from math import cos, sin

from numpy import *
from main import hedros, plan_hedros
from cube_func import *
from glut_loader import loader

from NeHeGL import *

from ArcBall import * 				# ArcBallT and this tutorials set of points/vectors/matrix types

PI2 = 2.0*3.1415926535			# 2 * PI (not squared!) 		// PI Squared

# *********************** Globals *********************** 
# Python 2.2 defines these directly
try:
	True
except NameError:
	True = 1==1	
	False = 1==0

g_Transform = Matrix4fT ()
g_LastRot = Matrix3fT ()
g_ThisRot = Matrix3fT ()

g_ArcBall = ArcBallT (640, 480)
g_isDragging = False
g_quadratic = None

global results
results = loader('cube.ply')

global zoom
zoom = 0

global mode
mode = 0
# Andrea mexeu

#results = loader('tetrahedron.ply')
#results = loader('octahedron.ply')
#results = loader('icosahedron.ply')
#results = loader('pyramid_v2.ply')
#number_of_vertex = results[0]
#number_of_faces = results[1]
#vertex=results[2]
#faces=results[3]
#Andrea terminou de mexer

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def Initialize (Width, Height):				# We call this right after our OpenGL window is created.
	global g_quadratic

	glClearColor(0.0, 0.0, 0.0, 1.0)					# This Will Clear The Background Color To Black
	glClearDepth(1.0)									# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LEQUAL)								# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)								# Enables Depth Testing
	glShadeModel (GL_FLAT);								# Select Flat Shading (Nice Definition Of Objects)
	glHint (GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) 	# Really Nice Perspective Calculations

	g_quadratic = gluNewQuadric();
	gluQuadricNormals(g_quadratic, GLU_SMOOTH);
	gluQuadricDrawStyle(g_quadratic, GLU_FILL); 
	# Why? this tutorial never maps any textures?! ? 
	# gluQuadricTexture(g_quadratic, GL_TRUE);			# // Create Texture Coords

	glEnable (GL_LIGHT0)
	glEnable (GL_LIGHTING)

	glEnable (GL_COLOR_MATERIAL)

	return True

def Upon_Drag (cursor_x, cursor_y):
	""" Mouse cursor is moving
		Glut calls this function (when mouse button is down)
		and pases the mouse cursor postion in window coords as the mouse moves.
	"""
	global g_isDragging, g_LastRot, g_Transform, g_ThisRot

	if (g_isDragging):
		mouse_pt = Point2fT (cursor_x, cursor_y)
		ThisQuat = g_ArcBall.drag (mouse_pt)						# // Update End Vector And Get Rotation As Quaternion
		g_ThisRot = Matrix3fSetRotationFromQuat4f (ThisQuat)		# // Convert Quaternion Into Matrix3fT
		# Use correct Linear Algebra matrix multiplication C = A * B
		g_ThisRot = Matrix3fMulMatrix3f (g_LastRot, g_ThisRot)		# // Accumulate Last Rotation Into This One
		g_Transform = Matrix4fSetRotationFromMatrix3f (g_Transform, g_ThisRot)	# // Set Our Final Transform's Rotation From This One
	return

def Upon_Click (button, button_state, cursor_x, cursor_y):
	""" Mouse button clicked.
		Glut calls this function when a mouse button is
		clicked or released.
	"""
	global g_isDragging, g_LastRot, g_Transform, g_ThisRot

	g_isDragging = False
	if (button == GLUT_RIGHT_BUTTON and button_state == GLUT_UP):
		# Right button click
		g_LastRot = Matrix3fSetIdentity ();							# // Reset Rotation
		g_ThisRot = Matrix3fSetIdentity ();							# // Reset Rotation
		g_Transform = Matrix4fSetRotationFromMatrix3f (g_Transform, g_ThisRot);	# // Reset Rotation
	elif (button == GLUT_LEFT_BUTTON and button_state == GLUT_UP):
		# Left button released
		g_LastRot = copy.copy (g_ThisRot);							# // Set Last Static Rotation To Last Dynamic One
	elif (button == GLUT_LEFT_BUTTON and button_state == GLUT_DOWN):
		# Left button clicked down
		g_LastRot = copy.copy (g_ThisRot);							# // Set Last Static Rotation To Last Dynamic One
		g_isDragging = True											# // Prepare For Dragging
		mouse_pt = Point2fT (cursor_x, cursor_y)
		tyi =g_ArcBall.click (mouse_pt);								# // Update Start Vector And Prepare For Dragging
		print "tyi: " + str(tyi)
	return

def Draw ():

	initial_face = 0

	global zoom

	global results

	global mode

	number_of_vertex = results[0]

	number_of_faces = results[1]
	vertex=results[2]
	
	faces=results[3]
	
	#print faces
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);				# // Clear Screen And Depth Buffer
	glLoadIdentity();												# // Reset The Current Modelview Matrix
	glTranslatef(-1.5,0.0,-6.0);									# // Move Left 1.5 Units And Into The Screen 6.0

	glPushMatrix();													# // NEW: Prepare Dynamic Transform
	glMultMatrixf(g_Transform);										# // NEW: Apply Dynamic Transform
	glColor3f(0.75,0.75,1.0);
	glScale(1+zoom,1+zoom,1+zoom)
	#Torus(0.30,1.00);
	#Andrea comecou a modificar aqui
	glColor4f(1.0,1.0,1.0,0.0)

	if mode == 0:
		hedros(vertex,faces)
	#cube(vertex,faces)
		
	if mode == 1:
		opened_cube(vertex,faces,3)
	#0 - ok
	#1 - ok

	#cube(vertex,faces)

	#hedros(vertex,faces)
	#plan_hedros(vertex,faces,initial_face)
	glPopMatrix();													# // NEW: Unapply Dynamic Transform
													# // NEW: Unapply Dynamic Transform

	glFlush ();														# // Flush The GL Rendering Pipeline
	glutSwapBuffers()
	return

def input_keyboard(*arg):

	global results
	global zoom
	global mode

	key = arg[0]

	if key =='c':
		results = loader('cube.ply')

	if key == 't':
		results = loader('tetrahedron.ply')

	if key == 'o':
		results = loader('octahedron.ply')

	if key == 'i':
		results =loader('icosahedron.ply')

	if key == 'd':
		results = loader('dodecahedron.ply')

	if key == 'a':
		zoom+=0.1
		print "zoom= ",zoom 

	if key == 'z':
		zoom-=0.1
		print "zoom= ",zoom

	if key == 'p':
		mode = 0

	if key =='l':
		mode = 1