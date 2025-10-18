from collections import deque

def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])
    q = deque()
    dist = [[float('inf')] * cols for _ in range(rows)]
    
    # Step 1: Initialize queue with all 0s
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                q.append((r, c))
    
    # Step 2: BFS from all zeros
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
    return dist

# Example
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat))



# Input:
# mat = [[0,0,0],
#        [0,1,0],
#        [1,1,1]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
