import math

def SUM(l):
	t = 0
	for i in l:
		t += i
	return t

def COS(a):
	return math.cos(math.radians(a))

def SIN(a):
	return math.sin(math.radians(a))

def CalculateCoord(CHNO):
    # Constants
    ANGLE = 60
    
    TAM_C1 = SUM(CHNO)
    CHNO_C2 = [CHNO[0]/TAM_C1, CHNO[1]/TAM_C1, CHNO[2]/TAM_C1, CHNO[3]/TAM_C1]

    TAM_C2 = CHNO_C2[0] + CHNO_C2[1] + CHNO_C2[3]
    CHNO_C3 = [CHNO_C2[0]/TAM_C2, CHNO_C2[1]/TAM_C2, CHNO_C2[2]/TAM_C2, CHNO_C2[3]/TAM_C2]

    LengthPlaneN = 100 - 2*100*CHNO_C2[2]*COS(ANGLE)

    InternalCicleRadius = 50*math.tan(0.523597)
    PlaneAngle = math.acos(InternalCicleRadius/86.6)
    TetrahedronAngle = math.sin(PlaneAngle)*86.6
    EdgeAngle = math.asin(TetrahedronAngle/100)
    
    XPlanoN = LengthPlaneN*(CHNO_C3[3] + COS(ANGLE)*CHNO_C3[0])
    YPlanoN = LengthPlaneN*SIN(ANGLE)*(CHNO_C3[0])

    OffsetX = 100*CHNO_C2[2]*COS(ANGLE)
    OffsetY = 100*CHNO_C2[2]*SIN(ANGLE)*math.cos(PlaneAngle)

    X = XPlanoN + OffsetX
    Y = YPlanoN + OffsetY
    Z = 100*CHNO_C2[2]*math.sin(EdgeAngle)

    return [round(X,3), round(Y,3), round(Z,3)]

def CalculateDistance(p1, p2):
	return round(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2), 3)


print("Values of the first CHNO:")
C1 = float(input("C: "))
H1 = float(input("H: "))
N1 = float(input("N: "))
O1 = float(input("O: "))
print()
print("Values of the second CHNO:")
C2 = float(input("C: "))
H2 = float(input("H: "))
N2 = float(input("N: "))
O2 = float(input("O: "))

Coord1 = CalculateCoord([C1, H1, N1, O1])
Coord2 = CalculateCoord([C2, H2, N2, O2])

print()
print("Point 1: " + str(Coord1))
print("Point 2: " + str(Coord2))
print("Distance: " + str(CalculateDistance(Coord1, Coord2)))
