from vpython import *
import numpy as np

X=0
Y=0
Z=0
arrowl=30
arrowHeadl=0.6
arrowt=0.2

ballr=0.3

tickW=0.075
tickH=0.15
tickT=0.075
cnt=0

numH=tickH*4
numD=tickW*2

labelH=1
labelD=labelH/10

helplineR=0.08

# The transformation functions
def to_cylinder(x,y,z):
    R=(x**2+y**2)**(1/2)
    phi=(np.arctan2(y,x))*180/np.pi
    z_cyil=z
    return R,phi,z_cyil
    
def to_spherical(x,y,z):
    rho=np.sqrt(x**2+y**2+z**2)
    theta=(np.arccos(z/rho))*180/np.pi
    phi=(np.arctan2(y,x))*180/np.pi
    return rho, theta, phi

#apply new values
def newCords():
    global point

    X=xval.value
    Y=yval.value
    Z=zval.value
    
    WX.text=str(X)
    WY.text=str(Y)
    WZ.text=str(Z)
    coords.text="(X, Y, Z) = "+str((X, Y, Z))

    point=vector(X,Y,Z)
    pointArrow.axis=point
    helpPoint.pos=point
    helpYCurve.modify(0,vector(0,Y,0))
    helpYCurve.modify(1,point)
    helpYCurve.modify(2,vector(X,0,Z))
    helpYCurve.modify(3,vector(X,0,0))
    helpZCurve.modify(0,vector(X,0,Z))
    helpZCurve.modify(1,vector(0,0,Z))

    # Change the coordinates in realtime
    if choices.selected == "Cylindrical" :
        cylinderC.visible=True
        sphereC.visible=False
        rho,phi,z=to_cylinder(X,Y,Z)
        coords.text="(X, Y, Z) = "+str((X, Y, Z))+"\n(\u03C1, \u03C6, Z ) = "+f"({rho:.1f}, {phi:.1f}\u00B0, {Z:.1f})"
    
        helpArrow.pos=vector(0,0,Z)
        helpArrow.axis=vector(X,Y,0)
        cylinderC.axis=vector(0,0,1)
        cylinderC.size=vector(Z,(sqrt(X**2+Y**2))*2,(sqrt(X**2+Y**2))*2)
    
    if choices.selected == "Spherical" :
        R,theta,phi= to_spherical(X,Y,Z)
        cylinderC.visible=False
        sphereC.visible=True
        coords.text="(X, Y, Z) = "+str((X, Y, Z))+"\n(r, \u03B8, \u03C6 ) = "+f"({R:.1f}, {theta:.1f}\u00B0, {phi:.1f}\u00B0)"
        helpArrow.pos=vector(0,0,0)
        helpArrow.axis=vector(X,0,Z)
        sphereC.radius=R

# User interface
scene.append_to_caption("\n")
wtext(text='From Cartesian To: ')
choices=menu(choices=[" ","Cylindrical","Spherical"],bind=newCords)

scene.append_to_caption("\n")
wtext(text='X (-10 - 10)\n')
xval=slider(bind=newCords,vertical=False,min=-arrowl/3,max=arrowl/3,value=5,step=0.1)
WX=wtext(text='5')

scene.append_to_caption("\n")
wtext(text='Y (-10 - 10)\n')
yval=slider(bind=newCords,vertical=False,min=-arrowl/3,max=arrowl/3,value=5,step=0.1)
WY=wtext(text='5')

scene.append_to_caption("\n")
wtext(text='Z (-10 - 10)\n')
zval=slider(bind=newCords,vertical=False,min=-arrowl/3,max=arrowl/3,value=5,step=0.1)
WZ=wtext(text='5')

scene.append_to_caption("\n")
coords=wtext(text="(X, Y, Z) = "+str((5, 5, 5)),font=6,box=False)

# make the axis
xarrow=arrow(axis=vector(1,0,0),pos=vector(-arrowl/2,0,0),color=color.red,length=arrowl,shaftwidth=arrowt,headlength=arrowHeadl)
yarrow=arrow(axis=vector(0,1,0),pos=vector(0,-arrowl/2,0),color=color.green,length=arrowl,shaftwidth=arrowt,headlength=arrowHeadl)
zarrow=arrow(axis=vector(0,0,1),pos=vector(0,0,-arrowl/2),color=color.blue,length=arrowl,shaftwidth=arrowt,headlength=arrowHeadl)

XLabel=text(text='X',pos=vector(arrowl/2+1,0,0),align='center',height=labelH,depth=labelD)
YLabel=text(text='Y',pos=vector(0,arrowl/2+1,0),align='center',height=labelH,depth=labelD)
ZLabel=text(text='Z',pos=vector(0,0,arrowl/2+1),align='center',height=labelH,depth=labelD)

for ticks in np.linspace((-arrowl/2),(arrowl/2),int(arrowl+1)):
    if (ticks==0) :
        ticks=1
    cnt=int(ticks)    
    tick=box(pos=vector(ticks,-tickH/2,0),size=vector(tickW,tickH,tickT))
    nums=text(text=str(cnt),pos=vector(ticks,-numH-tickH,0),align='center',height=numH,depth=numD)

for ticks in np.linspace((-arrowl/2),(arrowl/2),int(arrowl+1)):
    if (ticks==0) :
        ticks=1
    cnt=int(ticks)
    tick=box(pos=vector(-tickH/2,ticks,0),size=vector(tickH,tickW,tickT))
    nums=text(text=str(cnt),pos=vector(-numH-tickH,ticks,0),align='center',height=numH,depth=numD)
    
for ticks in np.linspace((-arrowl/2),(arrowl/2),int(arrowl+1)):
    if (ticks==0) :
        ticks=1
    cnt=int(ticks)
    tick=box(pos=vector(0,-tickH/2,ticks),size=vector(tickW,tickH,tickT))
    nums=text(text=str(cnt),pos=vector(0,-numH-tickH,ticks),axis=vector(0,0,-1),align='center',height=numH,depth=numD)

# pointer and helper lines for better visualization
pointArrow=arrow(axis=vector(5,5,5),color=color.orange,shaftwidth=arrowt,headlength=arrowHeadl)
helpPoint=sphere(pos=vector(5,5,5),color=color.red,radius=ballr)
helpArrow=arrow(axis=vector(0,1,0),color=color.orange,length=Y,shaftwidth=arrowt/2,headlength=arrowHeadl/2)
helpYCurve=curve(pos=[vector(0,5,0),vector(5,5,5),vector(5,0,5),vector(5,0,0)],radius=helplineR,color=color.white)
helpZCurve=curve(pos=[vector(5,0,5),vector(0,0,5)],radius=helplineR,color=color.white)
sphereC=sphere(pos=vector(0,0,0),radius=0.1,color=color.cyan,opacity=0.4,visible=True)
cylinderC=cylinder(pos=vector(0,0,0),axis=vector(0,0,1),radius=0.1,color=color.cyan,opacity=0.5,visible=True)


while True:    
    pass