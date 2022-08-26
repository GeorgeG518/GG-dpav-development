import dpav as dpp
import numpy as np
import time

mvm = dpp.modelViewMatrix()
point = np.array([1,2,3,1])
mvm.translate(0,8,0)
mvm.scale(1,1,1)
print(mvm.mvm)
mvm.rotate(45)
point=mvm*point

vbuffer = dpp.VBuffer((800,800))
window = dpp.Window(vbuffer)
window.open()
iteration=0
while window.is_open():
    if window.events['q']:
        window.close()

    if window.events['d']:
        p1=(0,0)
        p2=(int(point[0]), int(point[1]))
        dpp.draw_rectangle(vbuffer, 0xFF0000, p1, p2)
        window.set_vbuffer(vbuffer)
    vbuffer.clear()
    window.set_vbuffer(vbuffer)

    if iteration % 6 == 0:
        iteration=0
        point = np.array([200,200,3,1])

        mvm.reset()

    iteration+=1
    mvm.scale(iteration, iteration,1)
    point=mvm*point
    
    p1=(0,0)
    p2=(int(point[0]), int(point[1]))

    dpp.draw_line(vbuffer, p1, p2, 0xFF0000) 
    window.set_vbuffer(vbuffer)
    
    time.sleep(0.5)

