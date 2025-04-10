n = 7
m = 3
variables = ["Alaska", "Maldives", "Central City", "Mystic Falls", "New Orleans", "Small Ville", "London"]

g = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

colors = ["Red", "Green", "Blue"]
def isSafe(curr, color, c):
    for i in range(n):
        if g[curr][i] == 1 and color[i] == c:
            return False
    return True

def graphColor(curr, n, color):
    if curr == n:
        return True
    for i in range(1, m + 1):
        if isSafe(curr, color, i):
            color[curr] = i
            if graphColor(curr + 1, n, color):
                return True
            color[curr] = 0
    return False

color = [0] * n

if graphColor(0, n, color):
    for i in range(n):
        print(variables[i] + ": " + colors[color[i] - 1])
else:
    print("No possibility to color")