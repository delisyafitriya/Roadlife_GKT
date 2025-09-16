import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

def refleksiSumbuY(objek):
    matrixA = np.array(objek)
    matrixB = np.array([
        [-1, 0],
        [0, 1]
    ])
    return (matrixA @ matrixB).tolist()

def refleksiXH(vertices, centerX):    
    matrixA = np.array(vertices)
    matrixB = np.array([
        [-1,0],
        [0,1]])
    matrixC = np.array(
        [2*(centerX), 0])
    return ((matrixA @ matrixB)+matrixC).tolist()

def rotasi(points, center, angle):
    theta = np.radians(angle)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)

    rotation_matrix = np.array([
        [cos_theta, -sin_theta],
        [sin_theta, cos_theta]
    ])

    translated_points = np.array(points) - np.array(center)
    rotated_points = np.dot(translated_points, rotation_matrix.T)
    final_points = rotated_points + np.array(center)

    return final_points

def translasi (points, dx, dy):
    translated_points = np.array(points) + np.array([dx, dy])
    return translated_points.tolist()

def scaling(points, skala):
    pointsX = [vertex[0] for vertex in points]   
    centerX = (max(pointsX) + min(pointsX))/2
    pointsY = [vertex[1] for vertex in points]   
    centerY = (max(pointsY) + min(pointsY))/2

    scaled_points = (np.array(points) - np.array((centerX, centerY))) * skala + np.array((centerX, centerY))
    return scaled_points.tolist()

def drawCircle(TitikTengah, radius, segments=360, color=(1.0, 1.0, 1.0)):
    x = TitikTengah[0]
    y = TitikTengah[1]
    glBegin(GL_POLYGON)
    glColor3f(*color)
    for i in range(segments):
        angle = 2.0 * np.pi * i / segments  
        x_offset = radius * np.cos(angle)
        y_offset = radius * np.sin(angle)
        glVertex2f(x + x_offset, y + y_offset)
    glEnd()

def drawJalan():
    Jalan = [
        [10, 360], [-10, 360],
    ]
    Jalan.extend(refleksiSumbuY(translasi(scaling(Jalan, 18), 0, -720)))
    GarisPinggir = [
        [8, 360], [6, 360], [160, -360], [140, -360]
    ]
    GarisPinggir.extend(refleksiSumbuY(GarisPinggir))
    GarisTengah = [
        [15, -260], [-15, -260], [-18, -360], [18, -360],
        [9, 60], [-9, 60], [-12, -60], [12, -60],
        [3, 280], [-3, 280], [-6, 200], [6, 200]
    ]

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    for titik in Jalan:
        glVertex2f(titik[0], titik[1])

    glColor3f(1.0, 1.0, 1.0)
    for titik in GarisPinggir:
        glVertex2f(titik[0], titik[1])
    for titik in GarisTengah:
        glVertex2f(titik[0], titik[1])
    glEnd()

def drawPohon():
    PohonDaun = [[360.5, -202.5], [280.5, -82.5], [200.5, -202.5], 
                 [360.5, -142.5], [280.5, -42.5], [200.5, -142.5], 
                 [177.5, 77.5], [137.5, 137.5], [97.5, 77.5], 
                 [177.5, 97.5], [137.5, 157.5], [97.5, 97.5], 
                 [90.5, 287.5], [60.5, 327.5], [30.5, 287.5], 
                 [90.5, 307.5], [60.5, 337.5], [30.5, 307.5]]
    PohonBatang = [[300.5, -202.5], [260.5, -202.5], [260.5, -282.5], [300.5, -282.5], 
                   [147.5, 37.5], [127.5, 37.5], [127.5, 77.5], [147.5, 77.5], 
                   [70.5, 287.5], [50.5, 287.5], [50.5, 267.5], [70.5, 267.5]]

    glBegin(GL_TRIANGLES)
    glColor3f(0.133, 0.545, 0.133)
    for titik in PohonDaun:
        glVertex2f(titik[0], titik[1])
    for titik in refleksiSumbuY(PohonDaun):
        glVertex2f(titik[0], titik[1])
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.5882, 0.3882, 0.2784)
    for titik in PohonBatang:
        glVertex2f(titik[0], titik[1])
    for titik in refleksiSumbuY(PohonBatang):
        glVertex2f(titik[0], titik[1])
    glEnd()

def drawMobil(dx, dy, skala):
    MobilBody = [
        [-10, 360], [10, 360], [10, 354], [-10, 354],        
        [-12, 354], [12, 354], [12, 345], [-12, 345],
        [-11, 345], [-9, 345], [-9, 341], [-11, 341],
        [11, 345], [9, 345], [9, 341], [11, 341],
        [-14, 352], [-12, 352], [-12, 350], [-14, 350], 
        [14, 352], [12, 352], [12, 350], [14, 350],
    ]
    MobilBody = translasi(MobilBody, dx, dy)
    MobilBody = scaling(MobilBody, skala)
    MobilKaca =[
        [-8, 358], [8, 358], [8, 355], [-8, 355],
        [-10,349], [-8,349], [-8,348], [-10,348],
        [10,349], [8,349], [8,348], [10,348],
        [-5, 347], [5, 347], [5, 346], [-5, 346]
    ]
    MobilKaca = translasi(MobilKaca, dx, dy)
    MobilKaca = scaling(MobilKaca, skala)

    glBegin(GL_QUADS)
    glColor3f(0.502, 0.0, 0.0)
    for titik in MobilBody:
        glVertex2f(titik[0], titik[1])

    glColor3f(1.0, 1.0, 1.0)
    for titik in MobilKaca:
        glVertex2f(titik[0], titik[1])
    glEnd()
    
def drawOrang(dx, dy, refleksi):
    TitikTengah = [[-14, -16]]
    Orang = [[-16, -31], [-2, -65], [14, -60], [0, -25], 
             [-16, -31], [-23, -42], [-20, -53], [-11, -44], 
             [-23, -42], [-20, -53], [-37, -49], [-37, -38], 
             [0, -25], [5, -36], [14, -35], [19, -23], 
             [14, -35], [19, -23], [29, -45], [22, -49], 
             [-26, -94], [-17, -99], [1, -68], [-7, -54], 
             [0, -64], [8, -82], [18, -69], [14, -61], 
             [18, -69], [8, -82], [37, -78], [37, -67]]

    if refleksi == True:
        KoorX = [vertex[0] for vertex in Orang]   
        centerX = (max(KoorX) + min(KoorX))/2
        Orang = refleksiXH(Orang, centerX)
        TitikTengah = refleksiXH(TitikTengah, centerX)

    Orang = translasi(Orang, dx, dy)
    TitikTengah = translasi(TitikTengah, dx, dy)

    drawCircle(TitikTengah[0],14, 360, (0.0, 0.0, 1.0))
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    for titik in Orang:
        glVertex2f(titik[0], titik[1])
    glEnd()

def drawKincir(angle):
    TitikTengah = [[238.0, -57.5]]
    TitikTengah2 = refleksiSumbuY(TitikTengah)
    Stick = [[236.0, -49.5], [240.0, -49.5], [240.0, -7.5], [236.0, -7.5]]
    Stick2 = []
    Stick2.extend(refleksiSumbuY(Stick))
    Baling =[[236.0, -7.5], [224.0, -27.5], [236.0, -47.5]]
    Baling2 = []
    Baling2.extend(refleksiSumbuY(Baling))
    TitikRotasi = [[238.0, -7.5]]
    TitikRotasi2 = []
    TitikRotasi2.extend(refleksiSumbuY(TitikRotasi))
    Baling.extend(rotasi(Baling, TitikRotasi, 90))
    Baling.extend(rotasi(Baling, TitikRotasi, 180))
    Baling.extend(rotasi(Baling, TitikRotasi, 270))
    Baling2.extend(rotasi(Baling2, TitikRotasi2, -90))
    Baling2.extend(rotasi(Baling2, TitikRotasi2, -180))
    Baling2.extend(rotasi(Baling2, TitikRotasi2, -270))
    Baling = rotasi(Baling, TitikRotasi, angle)  
    Baling2 = rotasi(Baling2, TitikRotasi2, -angle)

    drawCircle(TitikTengah[0], 10, 360, (0.514, 0.361, 0.047))
    drawCircle(TitikTengah2[0], 10, 360, (0.514, 0.361, 0.047))

    glBegin(GL_QUADS)
    glColor3f(0.514, 0.361, 0.047)
    for titik in Stick:
        glVertex2f(titik[0], titik[1])
    for titik in Stick2:
        glVertex2f(titik[0], titik[1])
    glEnd()

    glBegin(GL_TRIANGLES)   
    glColor3f(1.0, 1.0, 0.0)
    for titik in Baling:
        glVertex2f(titik[0], titik[1])
    for titik in Baling2:
        glVertex2f(titik[0], titik[1])
    glEnd()  

def drawRumahA():
    RumahBaseA = [[128.5, 276.0], [128.5, 200.0], [298.5, 200.0], [298.5, 276.0]]
    RumahBaseB = []
    RumahBaseB.extend(scaling(RumahBaseA, 0.93))
    RumahJndlA = [[140.5, 252.0], [140.5, 226.0], [166.5, 226.0], [166.5, 252.0]]
    RumahJndlB = translasi(RumahJndlA, 36, 0)
    RumahJndlC = translasi(RumahJndlA, 120, 0)
    RumahPintu =[[210.5, 264.0], [210.5, 200.0], [250.5, 200.0], [250.5, 264.0]]
    RumahHandle = [[240.5, 230.0], [240.5, 224.0], [244.5, 224.0], [244.5, 230.0]]
    RumahKaca = []
    RumahKaca.extend(scaling(RumahJndlA, 0.6))
    RumahKaca.extend(scaling(RumahJndlB, 0.6))
    RumahKaca.extend(scaling(RumahJndlC, 0.6))
    RumahKaca.extend([[216.5, 248.0], [216.5, 206.0], [244.5, 206.0], [244.5, 248.0], 
                      [244.5, 254.0], [244.5, 260.0], [216.5, 260.0], [216.5, 254.0]])
    RumahAtapA = [[182.5, 324.0], [116.5, 288.0], [116.5, 276.0]]
    RumahAtapB = [[310.5, 276.0], [310.5, 288.0], [244.5, 324.0]]

    glBegin(GL_QUADS)
    glColor3f(0.996, 0.729, 0.321)
    for titik in RumahBaseA:
        glVertex2f(titik[0], titik[1])

    glColor3f(1.0, 1.0, 0.623)
    for titik in RumahBaseB:
        glVertex2f(titik[0], titik[1])
    
    glColor3f(0.408, 0.169, 0.184)
    for titik in RumahJndlA:
        glVertex2f(titik[0], titik[1])
    for titik in RumahJndlB:
        glVertex2f(titik[0], titik[1])
    for titik in RumahJndlC:
        glVertex2f(titik[0], titik[1])
    for titik in RumahPintu:
        glVertex2f(titik[0], titik[1])

    glColor3f(0.765, 0.973, 0.988)
    for titik in RumahKaca:
        glVertex2f(titik[0], titik[1])

    glColor3f(0.976, 0.953, 0.012)
    for titik in RumahHandle:
        glVertex2f(titik[0], titik[1])
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.651, 0.427, 0.706)
    for titik in RumahAtapA:
        glVertex2f(titik[0], titik[1])
    glColor3f(0.251, 0.098, 0.286)
    for titik in RumahAtapB:
        glVertex2f(titik[0], titik[1])
    glEnd()

def drawRumahB():
    RumahBaseA = [[-301, 261], [-301, 135], [-98, 135], [-98, 261]]
    RumahBaseB = []
    RumahBaseB.extend(scaling(RumahBaseA, 0.93))
    RumahJndlA = [[-281, 222], [-281, 174], [-243, 174], [-243, 222]]
    RumahJndlB = translasi(RumahJndlA, 125, 0)
    RumahPintu = [[-233, 241], [-233, 135], [-166, 135], [-166, 241]]
    RumahHandle = [[-185, 183], [-185, 173], [-175, 173], [-175, 183]]
    RumahKaca = []
    RumahKaca.extend(scaling(RumahJndlA, 0.7))
    RumahKaca.extend(scaling(RumahJndlB, 0.7))
    RumahKaca.extend([[-224, 213], [-224, 144], [-175, 144], [-175, 213], 
                      [-224, 232], [-224, 222], [-175, 222], [-175, 232]])
    RumahAtapA = [[-214, 335], [-320, 280], [-320, 260]]
    RumahAtapB = [[-79, 260], [-79, 280], [-185, 335]]

    glBegin(GL_QUADS)
    glColor3f(0.996, 0.729, 0.321)
    for titik in RumahBaseA:
        glVertex2f(titik[0], titik[1])

    glColor3f(1.0, 1.0, 0.623)
    for titik in RumahBaseB:
        glVertex2f(titik[0], titik[1])
    
    glColor3f(0.408, 0.169, 0.184)
    for titik in RumahJndlA:
        glVertex2f(titik[0], titik[1])
    for titik in RumahJndlB:
        glVertex2f(titik[0], titik[1])
    for titik in RumahPintu:
        glVertex2f(titik[0], titik[1])

    glColor3f(0.765, 0.973, 0.988)
    for titik in RumahKaca:
        glVertex2f(titik[0], titik[1])

    glColor3f(0.976, 0.953, 0.012)
    for titik in RumahHandle:
        glVertex2f(titik[0], titik[1])
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.651, 0.427, 0.706)
    for titik in RumahAtapA:
        glVertex2f(titik[0], titik[1])
    glColor3f(0.251, 0.098, 0.286)
    for titik in RumahAtapB:
        glVertex2f(titik[0], titik[1])
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(720, 720, "2D Object Transformation", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-360, 360, -360, 360)
    glMatrixMode(GL_MODELVIEW)

    translasiXMobil, translasiYMobil = 0, -800
    dxMobil, dyMobil = 0, 0
    skala = 1

    translasiXOrang, translasiYOrang = -170, 0
    dxOrang, dyOrang = 0, 0
    refleksi = False
    
    angle = 0
    while not glfw.window_should_close(window):
        stepMobil = 3.5
        stepXMobil = stepMobil if translasiXMobil > 0 else -stepMobil
        stepYMobil = stepMobil if translasiYMobil > 0 else -stepMobil
        
        stepOrang = 1.5
        stepXOrang = stepOrang if translasiXOrang > 0 else -stepOrang
        stepYOrang = stepOrang if translasiYOrang > 0 else -stepOrang

        glClearColor(0.133, 0.694, 0.298, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        drawJalan()
        drawRumahA()
        drawRumahB()
        drawPohon()

        if ((dxMobil >= translasiXMobil) if translasiXMobil > 0 else (dxMobil <= translasiXMobil)):
            dxMobil = 0    
        else:
            dxMobil += stepXMobil   
        if ((dyMobil >= translasiYMobil) if translasiYMobil > 0 else (dyMobil <= translasiYMobil)):
            dyMobil = 0    
        else:
            dyMobil += stepYMobil          
        if (dxMobil == 0 and dyMobil == 0):
            skala = 1
        else:
            skala += 0.05
        drawMobil(dxMobil, dyMobil, skala)
        
        if ((dxOrang >= translasiXOrang) if translasiXOrang >= 0 else (dxOrang <= translasiXOrang)):
            translasiXOrang = translasiXOrang*-1
            refleksi = not refleksi
        else:
            dxOrang += stepXOrang   
        if ((dyOrang >= translasiYOrang) if translasiYOrang >= 0 else (dyOrang <= translasiYOrang)):
            translasiYOrang = translasiYOrang*-1
        else:
            dyOrang += stepYOrang 
        drawOrang(dxOrang, dyOrang, refleksi)

        angle += 5
        if angle >= 360:
            angle -= 360
        drawKincir(angle)

        glfw.swap_buffers(window)
        glfw.poll_events()
        time.sleep(1/60)

    glfw.terminate()

if __name__ == "__main__":
    main()