import numpy as np
from math import *
import cv2

from point import *
from light import light
from player import player
from surface import surface

me = player()
li = light()
res = me.ppdist*2

img = np.zeros((res,res,3), np.uint8)
mytri = surface('tri', point(0,10,0), point(10,20,0), point(0,30,10))

k = cv2.waitKey(10) & 0xFF

norm = cross( sub(mytri.p2, mytri.p1), sub(mytri.p3, mytri.p1) )
mnorm = norm.mod()

while(k != 27):
    img = np.zeros((res,res,3), np.uint8)

    n1 = mytri.p1.add_ret(me.position)
    n2 = mytri.p2.add_ret(me.position)
    n3 = mytri.p3.add_ret(me.position)
    n1.project(me.ppdist)
    n2.project(me.ppdist)
    n3.project(me.ppdist)
    n1 = me.findfinal(n1)
    n2 = me.findfinal(n2)
    n3 = me.findfinal(n3)
    
    cv2.circle(img,(int(res/2+n1.x),int(res/2-n1.z)),2,(0,255,0),-1)
    cv2.circle(img,(int(res/2+n2.x),int(res/2-n2.z)),2,(0,255,0),-1)
    cv2.circle(img,(int(res/2+n3.x),int(res/2-n3.z)),2,(0,255,0),-1)

    cn = 40
    maxy = 0

    for x in range(0,cn):
        for y in range(0,cn):
            if x + y > cn:
                continue
            n = add(me.position, add( add( mul(sub(mytri.p2, mytri.p1), x*1.0/cn), mul(sub(mytri.p3, mytri.p1), y*1.0/cn) ), mytri.p1 )  )

            tolight = sub( li.pos, n )
            cos1 = dot(norm, tolight) / (tolight.mod() * mnorm)
            cos2 = dot(n   , norm) / (n.mod() * mnorm)

            col = 255/( abs(cos1-cos2) +1)
            if col>maxy:
               maxy = col 

            if x==0 and y==0:
                print cos1,cos2

            n.project(me.ppdist)
            #n = add( n1, add( mul( sub(n2,n1), x*1.0/cn ), mul( sub(n3,n1), y*1.0/cn ) ) )

            #n = add( n1, add( mul( sub(n2,n1), 0.5 ), mul( sub(n3,n1), 0.5 ) ) )

            

            cv2.circle(img,(int(res/2+n.x),int(res/2-n.z)),4,(col,col,col),-1)
    print maxy

    cv2.imshow("My Window", img)
    k = cv2.waitKey(10) & 0xFF
    moveIter = 0.1
    if k == 97:
        me.move(-moveIter,90,0)
    elif k == 100:
        me.move(moveIter,90,0)
    elif k == 119:
        me.move(moveIter,90,90)
    elif k == 115:
        me.move(-moveIter,90,90)
    elif k == 105:
        me.move(moveIter,0,90)
    elif k == 107:
        me.move(-moveIter,0,90)
