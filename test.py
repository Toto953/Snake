data = []
lenght = 2

for i in range(5):
    data.append([i, i])
    if len(data) > lenght:
        data.pop(0)
    print(data)

