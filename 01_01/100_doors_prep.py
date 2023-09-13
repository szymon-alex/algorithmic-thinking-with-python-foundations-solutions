doors = [False] * 101

print(doors)

for step in range(1,101):
    for i in range(step,101,step):
        doors[i] = not doors[i]

for i in range(1,101):
    if doors[i]:
        print(f"opened doors: {i}")

