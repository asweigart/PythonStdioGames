WIDTH = 6
LENGTH = 4

lines = []
lines.append(' \\_/ ___ \\ \\')
lines.append('\\___/ _ \\ \\ ')
lines.append('_____/ \\ \\ \\')
lines.append(' ___ \\_/ / /')
lines.append('/ _ \\___/ / ')
lines.append(' / \\_____/ /')


for i in range(LENGTH):
    for line in lines:
        print(line * WIDTH)
