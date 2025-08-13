import numpy as np

def get_angle(a,b,c):
    radians = np.arctan2(c[1]-b[1],c[0]-b[0])- np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(np.degrees(radians))
    return angle 
    
def get_distance(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    L = np.hypot(x2 - x1, y2 - y1)
    return np.interp(L, [0, 1], [0, 1000])