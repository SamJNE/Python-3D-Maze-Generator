import numpy as np
import random

length = int(input("Enter length of maze: "))
height = int(input("Enter height of maze: "))
floors = int(input("Enter number of floors: "))
unvisited = []
visited = []
directions = ["N", "S", "E", "W", "U", "D"]
arr = [[[-1 for l in range(length)] for h in range(height)] for f in range(floors)]
print()


for x in range(floors):
    startR = int(input("Enter start row of floor {} (0 to {}): ".format(x + 1, height - 1)))
    endR =   int(input("Enter end row of floor {} (0 to {}): ".format(x + 1, height - 1)))
    startC = int(input("Enter start column of floor {} (0 to {}): ".format(x + 1, length - 1)))
    endC =   int(input("Enter end column of floor {} (0 to {}): ".format(x + 1, length - 1)))
    print()

    for m in range(startR, endR + 1):
        for n in range(startC, endC + 1):
            arr[x][m][n] = 0
            unvisited.append((x, m, n))

#array[floor][row][column]

##unvisited.remove((3,8,8))
##unvisited.remove((3,8,9))
##unvisited.remove((3,8,10))
##unvisited.remove((3,8,11))
##unvisited.remove((3,9,8))
##unvisited.remove((3,9,9))
##unvisited.remove((3,9,10))
##unvisited.remove((3,9,11))
##unvisited.remove((3,10,8))
##unvisited.remove((3,10,9))
##unvisited.remove((3,10,10))
##unvisited.remove((3,10,11))
##unvisited.remove((3,11,8))
##unvisited.remove((3,11,9))
##unvisited.remove((3,11,10))
##unvisited.remove((3,11,11))
##unvisited.remove((4,8,8))
##unvisited.remove((4,8,9))
##unvisited.remove((4,8,10))
##unvisited.remove((4,8,11))
##unvisited.remove((4,9,8))
##unvisited.remove((4,9,9))
##unvisited.remove((4,9,10))
##unvisited.remove((4,9,11))
##unvisited.remove((4,10,8))
##unvisited.remove((4,10,9))
##unvisited.remove((4,10,10))
##unvisited.remove((4,10,11))
##unvisited.remove((4,11,8))
##unvisited.remove((4,11,9))
##unvisited.remove((4,11,10))
##unvisited.remove((4,11,11))

current = random.choice(unvisited)
unvisited.remove(current)
visited.append(current)

while len(visited) > 0:
    i = random.choice((1,2))
    if i == 1:
        current = random.choice(visited)
    elif i == 2:
        current = visited[-1]
    dirs = [x for x, in directions]
    random.shuffle(dirs)

    x = current[0]
    y = current[1]
    z = current[2]
    
    while len(dirs) > 0:
        if dirs[0] == "N":
            if y == 0:
                dirs.remove("N")
            else:
                new = (x, y - 1, z)
                if new in unvisited:
                    unvisited.remove(new)
                    visited.append(new)
                    arr[x][y][z] += 1
                    arr[x][y - 1][z] += 2
                    break
                else:
                    dirs.remove("N")                    

        elif dirs[0] == "S":
            if y == height - 1:
                dirs.remove("S")
            else:
                new = (x, y + 1, z)
                if new in unvisited:
                    unvisited.remove(new)
                    visited.append(new)
                    arr[x][y][z] += 2
                    arr[x][y + 1][z] += 1
                    break
                else:
                    dirs.remove("S")

        elif dirs[0] == "E":
            if z == 0:
                dirs.remove("E")
            else:
                new = (x, y, z + 1)
                if new in unvisited:
                    unvisited.remove(new)
                    visited.append(new)
                    arr[x][y][z] += 4
                    arr[x][y][z + 1] += 8
                    break
                else:
                    dirs.remove("E")

        elif dirs[0] == "W":
            if z == length - 1:
                dirs.remove("W")
            else:
                new = (x, y, z - 1)
                if new in unvisited:
                    unvisited.remove(new)
                    visited.append(new)
                    arr[x][y][z] += 8
                    arr[x][y][z - 1] += 4
                    break
                else:
                    dirs.remove("W")

        elif dirs[0] == "U":
            if x == floors - 1:
                dirs.remove("U")
            else:
                if random.choice((1,2)) == 1:                  
                    new = (x + 1, y, z) #1 up from current
                    if new in unvisited:
                        if arr[x][y][z] == 1 and y < height - 1:   #if current only has neighbour to north
                            newer = (x + 1, y + 1, z) #1 up, 1 south from current
                            if newer in unvisited:
                                unvisited.remove(new)
                                unvisited.remove(newer)
                                visited.append(newer)
                                visited.remove(current)
                                arr[x][y][z] += 16
                                arr[x + 1][y][z] += 34
                                arr[x + 1][y + 1][z] += 1
                                break
                            else:
                                dirs.remove("U")
                        elif arr[x][y][z] == 2 and y > 0:   #if current only has neighbour to south
                            newer = (x + 1, y - 1, z) #1 up, 1 north from current
                            if newer in unvisited:
                                unvisited.remove(new)
                                unvisited.remove(newer)
                                visited.append(newer)
                                visited.remove(current)
                                arr[x][y][z] += 16
                                arr[x + 1][y][z] += 33
                                arr[x + 1][y - 1][z] += 2
                                break
                            else:
                                dirs.remove("U")
                        elif arr[x][y][z] == 4 and z > 0:   #if current only has neighbour to east
                            newer = (x + 1, y, z - 1) #1 up, 1 west from current
                            if newer in unvisited:
                                unvisited.remove(new)
                                unvisited.remove(newer)
                                visited.append(newer)
                                visited.remove(current)
                                arr[x][y][z] += 16
                                arr[x + 1][y][z] += 40
                                arr[x + 1][y][z - 1] += 4
                                break
                            else:
                                dirs.remove("U")
                        elif arr[x][y][z] == 8 and z < length - 1:   #if current only has neighbour to west
                            newer = (x + 1, y, z + 1) #1 up, 1 east from current
                            if newer in unvisited:
                                unvisited.remove(new)
                                unvisited.remove(newer)
                                visited.append(newer)
                                visited.remove(current)
                                arr[x][y][z] += 16
                                arr[x + 1][y][z] += 36
                                arr[x + 1][y][z + 1] += 8
                                break
                            else:
                                dirs.remove("U")
                        else:
                            dirs.remove("U")
                    else:
                        dirs.remove("U")
                else:
                    dirs.remove("U")   #puts up at end of list
                    dirs.append("U")

        elif dirs[0] == "D":
            if x == 0:
                dirs.remove("D")
            else:
                if random.choice((1,2)) == 1:
                    new = (x - 1, y, z) #1 up from current
                    if new in unvisited:
                        if arr[x][y][z] == 1 and y < height - 1:   #if current only has neighbour to north
                            newer = (x - 1, y + 1, z) #1 down, 1 south from current
                            if newer in unvisited:
                                unvisited.remove(new)
                                unvisited.remove(newer)
                                visited.append(newer)
                                visited.remove(current)
                                arr[x][y][z] += 32
                                arr[x - 1][y][z] += 18
                                arr[x - 1][y + 1][z] += 1
                                break
                            else:
                                dirs.remove("D")
                        elif arr[x][y][z] == 2 and y > 0:   #if current only has neighbour to south
                            newer = (x - 1, y - 1, z) #1 up, 1 north from current
                            if newer in unvisited:
                                unvisited.remove(new)
                                unvisited.remove(newer)
                                visited.append(newer)
                                visited.remove(current)
                                arr[x][y][z] += 32
                                arr[x - 1][y][z] += 17
                                arr[x - 1][y - 1][z] += 2
                                break
                            else:
                                dirs.remove("D")
                        elif arr[x][y][z] == 4 and z > 0:   #if current only has neighbour to east
                            newer = (x - 1, y, z - 1) #1 up, 1 west from current
                            if newer in unvisited:
                                unvisited.remove(new)
                                unvisited.remove(newer)
                                visited.append(newer)
                                visited.remove(current)
                                arr[x][y][z] += 32
                                arr[x - 1][y][z] += 24
                                arr[x - 1][y][z - 1] += 4
                                break
                            else:
                                dirs.remove("D")
                        elif arr[x][y][z] == 8 and z < length - 1:   #if current only has neighbour to west
                            newer = (x - 1, y, z + 1) #1 up, 1 east from current
                            if newer in unvisited:
                                unvisited.remove(new)
                                unvisited.remove(newer)
                                visited.append(newer)
                                visited.remove(current)
                                arr[x][y][z] += 32
                                arr[x - 1][y][z] += 20
                                arr[x - 1][y][z + 1] += 8
                                break
                            else:
                                dirs.remove("D")
                        else:
                            dirs.remove("D")
                    else:
                        dirs.remove("D")
                else:
                    dirs.remove("D")
                    dirs.append("D")

        if len(dirs) == 0:
            visited.remove(current)
            break

print(np.array(arr))
print()

for f in range(0, floors):
    for l in range((5 * length) + 2):
        print("█", end="")
    print()
    for h in range(0, height):
        print("██", end="")
        for l in range(0, length):
            if arr[f][h][l] == -1 or arr[f][h][l] == 0:
                print("███", end="")
            elif arr[f][h][l] < 16:
                print("   ", end="")
            elif arr[f][h][l] >= 32:
                arr[f][h][l] -= 32
                print(" - ", end="")
            elif arr[f][h][l] >= 16:
                arr[f][h][l] -= 16
                print(" + ", end="")
            if arr[f][h][l] >= 8:
                arr[f][h][l] -= 8

            if arr[f][h][l] >= 4:
                arr[f][h][l] -= 4
                print(" ", end=" ")
            else:
                print("██", end="")
        print()
        print("██", end="")
        for l in range(0,length):
            if arr[f][h][l] >= 2:
                print("   ", end="██")
            else:
                print("███", end="██")
        print()
    print()
    print()   
