import math
import random

import drawSvg as draw
from drawSvg import Drawing
from hyperbolic import euclid, util
from hyperbolic.poincare.shapes import *
from hyperbolic.poincare import Transform
p1 = Point(0,-.5)
p2 = Point(.5, .5)
hl = Line.fromPoints(*p1, *p2, segment=False)

transMirror = Transform.mirror(p1, p2)
pts = [
    Point(0,0.1),
    Point(0,0.3),
    Point(0,0.5),
    Point(0,0.7),
    Point(0,0.9),
    Point(0.1,0),
    Point(0.3,0),
    Point(0.5,0),
    Point(0.7,0),
    Point(0.9,0),
    Point(0,-0.1),
    Point(0,-0.3),
    Point(0,-0.5),
    Point(0,-0.7),
    Point(0,-0.9),
    Point(-0.1,0),
    Point(-0.3,0),
    Point(-0.5,0),
    Point(-0.7,0),
    Point(-0.9,0),
]
ptsMirror = transMirror.applyToList(pts)
#ptsMirror = transMirror.inverted().applyToList(ptsMirror)  # Put back

d = Drawing(2.1, 2.1, origin='center')
d.draw(euclid.shapes.Circle(0, 0, 1), fill='#ddd')

d.draw(hl, hwidth=0.2, fill='white')
d.draw(p1, hradius=0.1, fill='green')
d.draw(p2, hradius=0.1, fill='green')

for i, pt in enumerate(pts):
    d.draw(pt, hradius=0.1, fill='#eee')
    d.draw(draw.Text(str(i), 0.05, *pt, center=0.7))
for i, pt in enumerate(ptsMirror):
    d.draw(pt, hradius=0.1, fill='#eee')
    d.draw(draw.Text(str(i), 0.05, *pt, center=0.7))

d.setRenderSize(w=400)
d.saveSvg('/home/shivanand/Documents/mirrorTest.svg')
d
