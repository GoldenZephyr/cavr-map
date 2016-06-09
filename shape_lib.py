class AbstractObject(object):
        def __init__(self, x, y, dx, dy, rot):
                self.x = x
                self.y = y
                self.dx = dx
                self.dy = dy
                self.rot = rot
class Rectangle(AbstractObject):
        def __init__(self, x, y, dx, dy, rot):
                AbstractObject.__init__(self, x, y, dx, dy, rot)
class Square(Rectangle):
        def __init__(self, x, y, l, rot):
                Rectangle.__init__(self, x, y, l, l, rot)

