from numpy import transpose
from geometry import Point, Polygon
	
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

def calc_all_vertex(vertex,faces,tr_matrix):
	#new_vertex_faces will be something like [polygon1,polygon2,polygon3,...,polygonN]
	new_vertex_faces = []
	size = len(faces)
	#for i in range(size):
	#	new_vertex_faces.append(1)

	#faces something like [[0,1,2,3],[54,7,6]]
	for f in faces:
		#f something like [0,1,2,3]

		fp = []
		f_index = faces.index(f)
		print "f_index"
		print f_index
		
		for v in f:
		
			tr_matrix_i = tr_matrix[f_index]
			tr_matrix_i = tr_matrix_i.transpose()
			tr_matrix_i = tr_matrix_i.tolist()
			new_vertex=calc_vertex(tr_matrix_i,vertex[v])
				
			p = Point(new_vertex[0],new_vertex[1],new_vertex[2])
			fp.append(p)
			
			#print new_vertex[v]
		print fp
		face = Polygon(fp)
		new_vertex_faces.append(face)
	print new_vertex_faces	
	return new_vertex_faces

#modelview = [[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,-6.0,1.0]]

#p0 = [-1.0,-1.0,-1.0]

#print calc_vertex(modelview,p0)