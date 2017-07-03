from PIL.Image import open
import time, sys, math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class TestContext(object):

	initialPosition=(0,0,0)

	def __init__(self):

		self.imageID = self.loadImage()

	def loadImage(self,imageName='8316_128x128.png'):
		im = open(imageName)
		print im.getbands()
		print im.mode
		#try:
		#image = im.tobytes()	
		ix = im.size
		iy = im.size[1]
		image = im.tobytes("raw", "RGBA",0,-1)
		#image = im.tostring()
		#ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBA", 0, -1)
		#except (SystemError, ValueError):
		#	ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)
		#except AttributeError:
		#	ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)
		ID = glGenTextures(1)

		glBindTexture(GL_TEXTURE_2D, ID)
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)

		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
		return ID


if __name__ == "__main__":
	a = TestContext()
	#a.loadImage()