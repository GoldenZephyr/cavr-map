class Abstract2D(object):
        def __init__(self, x, y, lx, ly, rot):
                self.x = x
                self.y = y
                self.lx = lx
                self.ly = ly
                self.rot = rot
class Abstract3D(object):
	def __init__(self, x, y, z, lx, ly, lz, rot):
		self.x = x
		self.y = y
		self.z = z
		self.lx = lx
		self.ly = ly
		self.lz = lz
		self.rot = rot
class Rectangle(Abstract2D):
        def __init__(self, x, y, lx, ly, rot):
                Abstract2D.__init__(self, x, y, lx, ly, rot)
class Ellipse(Abstract2D):
	def __init__(self, x, y, lx, ly, rot):
		Abstract2D.__init__(self, x, y, lx, ly, rot)
class Square(Rectangle):
        def __init__(self, x, y, l, rot):
                Rectangle.__init__(self, x, y, l, l, rot)
class Circle(Ellipse):
	def __init__(self, x, y, l, rot):
		Ellipse.__init__(self, x, y, l, l, rot)
class Rectangle3D(Abstract3D):
	def __init__(self, x, y, z, lx, ly, lz, rot):
		Abstract3D.__init__(self, x, y, z, lx, ly, lz, rot)
class Ellipse3D(Abstract3D):
	def __init__(self, x, y, z, lx, ly, lz, rot):
		Abstract3D.__init__(self, x, y, x, lx, ly, lz, rot)
class Square3D(Rectangle3D):
	def __init__(self, x, y, z, l, rot):
		Rectangle3D.__init__(self, x, y, z, l, l, l, rot)
class Circle3D(Ellipse3D):
	def __init__(self, x, y, z, l, rot):
		Ellipse3D.__init__(self, x, y, z, l, l, l, rot)

