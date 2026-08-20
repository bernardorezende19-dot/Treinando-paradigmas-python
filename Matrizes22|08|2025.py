mat=[[1,2,3],[4,5,6],[7,8,9]]
def remover (L,C):
    for i in range(len(mat)):
        mat [L] [i] = 0
        mat [i] [C] = 0
remover(0,1)
print (mat [0])
print (mat [1])
print (mat [2])
