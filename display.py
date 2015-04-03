import numpy as np
from math import *
import cv2

from point import point
from player import player
from surface import surface

me = player()
res = me.ppdist*2

img = np.zeros((res,res,3), np.uint8)
mytri = surface('tri', point(10,20,0), point(-10,20,0), point(0,20,10))

k = cv2.waitKey(10) & 0xFF

while(k != 27):
    img = np.zeros((res,res,3), np.uint8)

    n1 = mytri.p1
    n2 = mytri.p2
    n3 = mytri.p3
    n1.add(me.position)
    n2.add(me.position)
    n3.add(me.position)
    n1.project(me.ppdist)
    n2.project(me.ppdist)
    n3.project(me.ppdist)

    cv2.circle(img,(res/2+n1.x,res/2-n1.z),2,(0,255,0),-1)
    cv2.circle(img,(res/2+n2.x,res/2-n2.z),2,(0,255,0),-1)
    cv2.circle(img,(res/2+n3.x,res/2-n3.z),2,(0,255,0),-1)

    #for i in range(-me.ppdist, me.ppdist):
        #for j in range(-me.ppdist,me.ppdist):
            #ptat20 = point(i,me.ppdist,j)
            #ptat20.project(20)
            #ptat20.add(me.position)
            #if mytri.liesontri(ptat20):
                #cv2.circle(img,(res/2 + i, res/2 - j),2,(0,255,0),-1)

    cv2.imshow("My Window", img)
    k = cv2.waitKey(10) & 0xFF
    if k == 97:
        me.move(-2,90,0)
    elif k == 100:
        me.move(2,90,0)
    elif k == 105:
        me.move(2,0,90)
    elif k == 107:
        me.move(-2,0,90)
