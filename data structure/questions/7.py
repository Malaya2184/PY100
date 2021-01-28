# find the centre of a rectangle


class Point:
    pass
    """in a 2D space, attributes: x,y """

#print(Point)

atom1Coord=Point()
atom1Coord.x=45
atom1Coord.y=30

def print_point(inputpoint):
    print(inputpoint.x,inputpoint.y)

print_point(atom1Coord)


#print(atom1Coord.x,atom1Coord.y)

class rectangle:
    pass
    """length, width, origin"""

sqr=rectangle()
sqr.length=20
sqr.width=20
sqr.origin=Point()
sqr.origin.x=0
sqr.origin.y=0

rectangle2=rectangle()
rectangle2.length=20
rectangle2.width=20
rectangle2.origin=Point()
rectangle2.origin.x=0
rectangle2.origin.y=0

def centre_of_rectangle(inputr):
    centre=Point()
    centre.x=inputr.length*0.5+inputr.origin.x
    centre.y=inputr.width*0.5+inputr.origin.y
    return centre

output_centre=centre_of_rectangle(sqr)
print_point(output_centre)
output_centre2=centre_of_rectangle(rectangle2)
print_point(output_centre2)