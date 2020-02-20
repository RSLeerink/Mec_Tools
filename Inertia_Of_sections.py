#Test

from numpy import pi
def Rectangle(w,h):
    Ixx = (w*h**3)/(12)
    Iyy = (h*w**3)/12
    return Ixx,Iyy

def Hollow_Rectangular_Section(W,H,w,h):
    Ixx = ((W*H**3)/12) - ((w*h**3)/12)
    Iyy = ((H*W**3)/12) - ((h*w**3)/12)
    return Ixx,Iyy

def Circular_Section(D):
    Ixx = (pi/64)*D**4
    Iyy = Ixx
    return Ixx,Iyy

def Hollow_Circular_Section(D,d):
    Ixx = (pi/64) * (D**4 - d**4)
    Iyy = Ixx
    return Ixx,Iyy



T = Hollow_Circular_Section(100,90)
print(T)