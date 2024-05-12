class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maximum = []
        for rows in range(len(grid) - 2):
            row = []
            for cols in range(len(grid[0]) - 2):
                submatrix = [
                    [grid[rows][cols], grid[rows][cols+1], grid[rows][cols+2]],
                    [grid[rows+1][cols], grid[rows+1][cols+1], grid[rows+1][cols+2]],
                    [grid[rows+2][cols], grid[rows+2][cols+1], grid[rows+2][cols+2]]
                ]
                max_val = max(max(row) for row in submatrix)
                row.append(max_val)
            maximum.append(row)
        return maximum
