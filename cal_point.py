

def calc_vertex(matrix,point):
	px = point[0]
	py = point[1]
	pz = point[2]

	#xp = matrix[0]*px + matrix[4]*py + matrix[8]*pz + matrix[12]
	#print xp	
	xp = matrix[0][0]*px + matrix[0][1]*py + matrix[0][2]*pz + matrix[0][3]
	yp = matrix[1][0]*px + matrix[1][1]*py + matrix[1][2]*pz + matrix[1][3]
	zp = matrix[2][0]*px + matrix[2][1]*py + matrix[2][2]*pz + matrix[2][3]
	wp = matrix[3][0]*px + matrix[3][1]*py + matrix[3][2]*pz + matrix[3][3]
	
	xp = xp/wp
	yp = yp/wp
	zp = zp/wp
	return [xp,yp,zp]

#modelview = [[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,-6.0,1.0]]

#p0 = [-1.0,-1.0,-1.0]

#print calc_vertex(modelview,p0)