//The implementation can be done using dynamic programming:

def matrix_chain_order(arr):
    # Number of matrices in input array
    n = len(arr)
    
    # Create a table m to store the results of subproblems
    # m[i][j] is the minimum number of scalar multiplications 
    # needed to compute the matrix A[i]A[i+1]...A[j]
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    # length is the chain length. We evaluate the matrix chain multiplication
    # for chain lengths from 2 to n-1 (both inclusive).
    for length in range(2, n): 
        for i in range(1, n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    
    # Return the minimum cost for multiplying matrices from 1 to n-1
    return m[1][n-1]

arr = [40, 20, 30, 10, 30]  # Example array
print(matrix_chain_order(arr))  # Outputs 26000 which is the minimum number of operations
