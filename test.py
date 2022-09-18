# data = []
# lenght = 2

# for i in range(5):
#     data.append([i, i])
#     if len(data) > lenght:
#         data.pop(0)
#     print(data)





# import random

# size = 64

# positionsX = []
# positionsY = []

# for x in range(1920):
#     if x%size == 0:
#         positionsX.append(x)
# for y in range(1080):
#     if y%size == 0:
#         positionsY.append(y)


# print(positionsX)
# print(positionsY)

# print(random.choice(positionsX), random.choice(positionsY))








import pygame

data = [pygame.Rect(0, 1, 2, 3), pygame.Rect(4, 5, 6, 7), pygame.Rect(8, 9, 10, 11)]

good = False
x = 1

while not good:
    s = True
    for i in data:
        if i[0] == x:
            s = False
            break
    
    if s == True:
        good = True

    # x += 1

print(data[:-1])

pygame.quit()











# counter = 4-1
# while counter != -1:
#     print(counter)
#     counter -= 1