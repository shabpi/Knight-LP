from pyscipopt import Model


import matplotlib.pyplot as plt
import numpy as np



model = Model ("Knight")

moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]

# Define variables

a = (0,0)
b = (2,2)

X = dict()

for i in range(8):
    for j in range(8):
        X[i,j] = model.addVar(f"x{i}{j}", vtype="B")

model.addCons(X[a] == 1 )
model.addCons(X[b] == 1 )

for i in range(8):
    for j in range(8):
        if ((i,j) == a or (i,j) == b):
            continue
        model.addCons( sum( 0.5 * X[(i + k[0],j + k[1])] for k in moves if (i + k[0] < 8 and i + k[0] > -1 and j + k[1] < 8 and j + k[1] > -1)) >= X[i,j]  )

model.addCons(sum(X[(a[0] + k[0],a[1] + k[1])] for k in moves if (a[0] + k[0] < 8 and a[0] + k[0] > -1 and a[1] + k[1] < 8 and a[1] + k[1] > -1)) == 1)
model.addCons(sum(X[(b[0] + k[0],b[1] + k[1])] for k in moves if (b[0] + k[0] < 8 and b[0] + k[0] > -1 and b[1] + k[1] < 8 and b[1] + k[1] > -1)) == 1)



model.setObjective(sum(X.values()), 'minimize')

model.optimize()
# sol describes the best solution found
sol = model.getBestSol()

# Create chessboard background
board = np.array([[(i + j) % 2 for j in range(8)] for i in range(8)], dtype=float)

# Overlay solution (mark placed pieces differently)
for i in range(8):
    for j in range(8):
        if model.getSolVal(sol, X[i, j]) > 0.5:
            board[i][j] = 2  # third color for pieces

path = list()
knight = a

while knight != b:
    path.append(knight)
    for k in moves:
        try:
            if (board[knight[0] + k[0]][knight[1] + k[1]] == 2):
                knight = (knight[0]  + k[0], knight[1] + k[1])
                board[knight[0]][knight[1]] = 3
        except:
            continue
            

# Custom colormap: white, gray, black
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['white', "#0D070F", 'red', "#250E8B"])

plt.figure(figsize=(6, 6))
plt.imshow(board, cmap=cmap, vmin=0, vmax=2)
plt.xticks(range(8))
plt.yticks(range(8))
plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.show()


print(f"Objective function value : { model.getObjVal () } ")
print(sol)