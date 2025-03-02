x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
# Lista por comprension:
coords = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]

# Otra manera de hacerlo:
# coords2 = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 coords2.append([i, j, k])

print(coords)