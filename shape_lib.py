class Abstract2D(object):
        def __init__(self, x, y, dx, dy, rot):
                self.x = x
                self.y = y
                self.dx = dx
                self.dy = dy
                self.rot = rot
class Abstract3D(object):
	def __init__(self, x, y, z, dx, dy, dz, rot):
		self.x = x
		self.y = y
		self.z = z
		self.dx = dx
		self.dy = dy
		self.dz = dz
		self.rot = rot
class Rectangle(Abstract2D):
        def __init__(self, x, y, dx, dy, rot):
                Abstract2D.__init__(self, x, y, dx, dy, rot)
class Ellipse(Abstract2D):
	def __init__(self, x, y, dx, dy, rot):
		Abstract2D.__init__(self, x, y, dx, dy, rot)
class Square(Rectangle):
        def __init__(self, x, y, l, rot):
                Rectangle.__init__(self, x, y, l, l, rot)
class Circle(Ellipse):
	def __init__(self, x, y, l, rot):
		Ellipse.__init__(self, x, y, l, l, rot)
class Rectangle3D(Abstract3D):
	def __init__(self, x, y, z, dx, dy, dz, rot):
		Abstract3D.__init__(self, x, y, z, dx, dy, dz, rot)
class Ellipse3D(Abstrarct3D):
	def __init__(self, x, y, z, dx, dy, dz, rot):
		Abstract3D.__init__(self, x, y, x, dx, dy, dz, rot)
class Square3D(Rectangle3D):
	def __init__(self, x, y, z, l, rot):
		Rectangle3D.__init__(self, x, y, z, l, l, l, rot)
class Circle3D(Ellipse3D):
	def __init__(self, x, y, z, l, rot):
		Ellipse3D).__init__(self, x, y, z, l, l, l, rot)

