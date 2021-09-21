def maze_solver(maze, x, y, n, goal, visited=[]):

    if x >= n or y >= n:
        return False
    cell_value = maze[x][y]
    if cell_value == goal:
        visited.append([x,y])
        return True
    if cell_value != 1:
        return False
    if check(cell_value, x, y, n) is True and [x,y] not in visited:
        visited.append([x,y])
        maze_solver(maze, x-1, y, n, 2, visited)
        maze_solver(maze, x, y+1, n, 2, visited)
        maze_solver(maze, x+1, y, n, 2, visited)
        maze_solver(maze, x, y-1, n, 2, visited)
    return visited
    
def check(cell_value, x, y, n):
    if x >= 0 and x < n and y >= 0 and y < n and cell_value == 1:
        return True
    return False

maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 2],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 0, 0]
]

order_of_visit = maze_solver(maze, 0, 0, 5, 2)
goal_state = [2,4]
order_of_visit.append(goal_state)
# for element in order_of_visit:
#     for num in element:
#         print(num, end=" ")
#     print()
print(order_of_visit)