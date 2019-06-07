import numpy, sys, time

#def matmultBlock1(a, b, c, n, blockSize):
#    for bi in range(0, n, blockSize):
#        for bj in range(0, n, blockSize):
#            for bk in range(0, n, blockSize):
#                for i in range(blockSize):
#                    for k in range(blockSize):
#                        for j in range(blockSize):
#                            c[bi+i][bj+j] += a[bi+i][bk+k]*b[bk+k][bj+j]
#    return c

def matmultBlock2(a, b, c, n, blockSize):
    for bi in range(0, n, blockSize):
        for bj in range(0, n, blockSize):
            for bk in range(0, n, blockSize):
                for i in range(blockSize):
                    for k in range(blockSize):
                        temp = a[bi+i][bk+k]
                        for j in range(blockSize):
                            #c[bi+i][bj+j] += a[bi+i][bk+k]*b[bk+k][bj+j]
                            c[bi+i][bj+j] += temp*b[bk+k][bj+j]
    return c

def matmult3(a, b, c, n):
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k]*b[k][j]
            c[i][j] = sum
    return c

def matmultBlock3(a, b, c, n, blockSize):
    for bj in range(0, n, blockSize):
        for bk in range(0, n, blockSize):
            for i in range(n):
                for j in range(bj, min(n, bj + blockSize), 1): 
                    sum = 0
                    for k in range(bk, min(bk + blockSize, n),1):
                            sum += a[i][k]*b[k][j]
                    c[i][j] += sum
    return c

def matmult2(a, b, c, n):
    for i in range(n):
        for k in range(n):
            temp = a[i][k]
            for j in range(n):
                c[i][j] += temp*b[k][j]
    return c



#def matmult1(a, b, c, n):
#    for i in range(n):
#        for k in range(n):
#            for j in range(n):
#                c[i][j] += a[i][k]*b[k][j]
#    return c





# Print C for debugging. Comment out the print before measuring the execution time.
#total = 0
#for i in range(n):
#    for j in range(n):
        # print c[i, j]
#        total += c[i, j]
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
#print("sum: %.6f" % total)


#if (len(sys.argv) != 2):
#    print("usage: python %s N" % sys.argv[0])
#    quit()

#n = int(sys.argv[1])





def main(n, blockSize):

    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    #c = numpy.matmul(a,b)

    #c = matmult1(a, b, c, n)
    #end1 = time.time()
    #print("mult1 time: %.6f sec" % (end1 - begin))

    end1 = begin
    
    c = matmult2(a, b, c, n)
    end2 = time.time()
    print("mult2 time: %.6f sec" % (end2 - end1))

    #c = matmultBlock1(a, b, c, n, blockSize)
    #end3 = time.time()
    #print("multBlock1 time: %.6f sec" % (end3 - end2))

    end3 = end2

    c = matmultBlock2(a, b, c, n, blockSize)
    end = time.time()
    print("multBlock2 time: %.6f sec" % (end - end3))

    c = matmult3(a, b, c, n)
    end4 = time.time()
    print("mult3 time: %.6f sec" % (end4 - end))


    c = matmultBlock3(a, b, c, n, blockSize)
    end5 = time.time()
    print("multBlock3 time: %.6f sec" % (end5 - end4))

    return numpy.array((end2 - end1,end - end3,end4 - end,end5 - end4))


def plot(N, r):

    import matplotlib.pyplot as plt

    plt.plot(list(r[0:N,0]))
    plt.plot(list(r[0:N,1]))
    plt.plot(list(r[0:N,2]))
    plt.plot(list(r[0:N,3]))
    plt.legend(['mult2', 'multBlock2', 'mult3', 'multBlock3'], loc='upper left')
    plt.xlabel('Size N: 100 + 25*x')
    plt.show()




    
n = 25
blockSize = 25

N = 20
r = numpy.zeros((N, 4))

for i in range(N):
    print('n = %d'%(n+i*blockSize) )
    r[i] = main(n+i*blockSize, blockSize)
    print('\n\n')

plot(N, r)
