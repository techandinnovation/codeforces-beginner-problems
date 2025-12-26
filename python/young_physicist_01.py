n = int(input())
ALL_FORCES = []
isEquilibrium = True
while (n > 0):
    coors = input()
    coorsArr = coors.split()
    ALL_FORCES.append(coorsArr)    
    n -= 1
NET_FORCE = [0 , 0 , 0]
for force in ALL_FORCES:
    NET_FORCE[0] += int(force[0])
    NET_FORCE[1] += int(force[1])
    NET_FORCE[2] += int(force[2])
for i in NET_FORCE:
    if (i != 0):
        isEquilibrium = False
        break
if (isEquilibrium):
    print("YES")
else:
    print("NO")