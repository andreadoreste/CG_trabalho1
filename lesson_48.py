 # -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import copy
import TextureMap_PauloRoma as tmap
from math import cos, sin

from numpy import *
from main import *
from glut_loader import loader
import cal_point as cp
from NeHeGL import *
from geometry import Box, Line, Point

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
mode = 1

global is_texture
is_texture = False

global initial_face
initial_face = 0

global new_vertex_faces
new_vertex_faces=[]

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def Initialize (Width,	 Height):				# We call this right after our OpenGL window is created.
	global g_quadratic
	global gl_context

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

	gl_context = tmap.TestContext()

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
	global initial_face
	global mode
	global g_isDragging, g_LastRot, g_Transform, g_ThisRot

	g_isDragging = False
	if (button == GLUT_RIGHT_BUTTON and button_state == GLUT_UP):
		# Right button click
		mouse_pt = Point2fT (cursor_x, cursor_y)
		print "cursors:",(cursor_x,cursor_y)
		print 'mouse_pt:',mouse_pt
		if mode==0:

			mode=1
			pos = getMousePos3D(mouse_pt[0],mouse_pt[1])
			#Point on screen
			pout = [pos[0],pos[1],0]
			print 'pout',pout
			#Point in infinite
			paway = [pos[0],pos[1],-1000]

			pout = Matrix3fMulMatrix3f(g_ThisRot,pout)
			print 'pout_after transform',pout

			#paway = Matrix3fMulMatrix3f(g_ThisRot,paway)

			pout = Point(pout[0],pout[1],pout[2])
			paway = Point(paway[0],paway[1],paway[2])
			print 'pout'
			print pout
			print 'paway'
			print paway

			line = Line(pout,paway)
			print "Line"
			print line

			#List of faces
			faces=results[3]

			#List of vertex
			vertex=results[2]

			initial_face = getIntersections(line,faces,vertex)


		else:
			mode=0
		
	elif (button == GLUT_LEFT_BUTTON and button_state == GLUT_UP):
		# Left button released
		g_LastRot = copy.copy (g_ThisRot);							# // Set Last Static Rotation To Last Dynamic One
	elif (button == GLUT_LEFT_BUTTON and button_state == GLUT_DOWN):
		# Left button clicked down
		g_LastRot = copy.copy (g_ThisRot);							# // Set Last Static Rotation To Last Dynamic One
		g_isDragging = True											# // Prepare For Dragging
		mouse_pt = Point2fT (cursor_x, cursor_y)
		print 'mouse_pt rotation',mouse_pt
		g_ArcBall.click (mouse_pt);								# // Update Start Vector And Prepare For Dragging
		
		
	return

def Draw ():
	global gl_context

	global initial_face
	
	global zoom

	global results

	global mode

	global new_vertex_faces

	#gl_context.setCamera()	

	#Setup Texture
	gl_context.setupTexture()


	number_of_vertex = results[0]

	number_of_faces = results[1]
	#List of vertex
	vertex=results[2]
	
	#List of faces
	faces=results[3]
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);				# // Clear Screen And Depth Buffer
	glLoadIdentity();												# // Reset The Current Modelview Matrix
	
	glTranslatef(0.0,0.0,-6.0);									# // Move Left 1.5 Units And Into The Screen 6.0

	glPushMatrix();													# // NEW: Prepare Dynamic Transform
	glMultMatrixf(g_Transform);										# // NEW: Apply Dynamic Transform
	glColor3f(0.75,0.75,1.0);
	glScale(1+zoom,1+zoom,1+zoom)
	
	#glColor4f(1.0,1.0,1.0,0.0)
	#Mode 0 is when 'p' is pressed and the solid closed is displayed
	if mode == 0:
		
		#is_Texture is True when 'h' is pressed
		#new_vertex_faces is true when the solid was opened before and 'h' was pressed
		if (is_texture==True and new_vertex_faces):
			t_hedros(new_vertex_faces,faces,vertex)
			
		else:
				
			hedros(vertex,faces)
		
	#Mode 1 is when 'l' is pressed and the solid must be opened			
	if mode == 1:
		
		if is_texture==True and new_vertex_faces:
			
			t_open_hedros(new_vertex_faces)	
		
		else:
		
			tr_matrix = opened_cube(vertex,faces,initial_face)
		
			#List of new faces with transformations
			new_vertex_faces= cp.calc_all_vertex(vertex,faces,tr_matrix)

	glPopMatrix();													# // NEW: Unapply Dynamic Transform
													# // NEW: Unapply Dynamic Transform
	glFlush ();														# // Flush The GL Rendering Pipeline
	glutSwapBuffers()
	return

def input_keyboard(*arg):

	global results
	global zoom
	global mode
	global is_texture

	global g_isDragging, g_LastRot, g_Transform, g_ThisRot

	key = arg[0]

	#load cube.ply
	if key =='c':
		results = loader('cube.ply')

	#load tetrahedron.ply
	if key == 't':
		results = loader('tetrahedron.ply')

	#load octahedron.ply
	if key == 'o':
		results = loader('octahedron.ply')
	
	#load icosahedron.ply
	if key == 'i':
		results =loader('icosahedron.ply')
	
	#load dodecahedron.ply
	if key == 'd':
		results = loader('dodecahedron.ply')

	#Zoom in	
	if key == 'a':
		zoom+=0.1
	
	#Zoom out
	if key == 'z':
		zoom-=0.1
	
	#Close the solid
	if key == 'p':
		mode = 0

	#Open the solid
	if key =='l':
		mode = 1

	#Active texture
	if key =='h':
		is_texture = True

	#Reset	
	if key == 'r':
		is_texture=False
		g_LastRot = Matrix3fSetIdentity ();							# // Reset Rotation
		g_ThisRot = Matrix3fSetIdentity ();							# // Reset Rotation
		g_Transform = Matrix4fSetRotationFromMatrix3f (g_Transform, g_ThisRot);	# // Reset Rotation

def getMousePos3D(x, y):
	
	modelview = glGetDoublev( GL_MODELVIEW_MATRIX)
	projection = glGetDoublev( GL_PROJECTION_MATRIX)
	viewport = glGetIntegerv( GL_VIEWPORT)

	winX = float(x)
	winY = ((viewport[3]) - (y))
	winZ = glReadPixels(x, int(winY),1,1,GL_DEPTH_COMPONENT,GL_FLOAT)
	print"win",(winX,winY,winZ)
	
	color = glReadPixels(x,int(winY),1,1, GL_RGBA,GL_FLOAT)
	
	teste_i = compare_color(color,colors)
	
	pos=gluUnProject(winX,winY,winZ, modelview, projection,viewport)
	print 'pos',pos
	
	#object coordinates
	posX = pos[0]
	posY = pos[1]
	posZ = pos[2]
	
	#return teste_i
	return pos

def compare_color(color,colors_list):
	try:
		color=color[0][0]
		color = list(color)
		color = tuple(color)
		itc = colors_list.index(color)
		return itc
	except:
		pass

def getIntersections(line,faces,vertex):
	t = 'inf'

	new_faces =[]
	for face in faces:
		fp = []
		#f something like [0,1,2,3]
		for v in face:
			p = vertex[v]
			#print 'p',p
			#print 'v',v
			p = Point(p[0],p[1],p[2])
			fp.append(p)
		f = Polygon(fp)
		print "f"
		print f
		teste = line.intersectToPlane(f)
		if teste:
			if teste[1]<t:
				t =teste[1]
				initial_face = faces.index(face)
				print 'teste'
				print teste
				print initial_face
		else:

			print 'there is no t'
			print faces.index(face)
	print 'initial_face'
	print initial_face
	return initial_face