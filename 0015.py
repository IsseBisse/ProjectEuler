def move(x, y, limit):
	"""Too slow for limit > 15"""
	# limit = 3

	if x == limit or y == limit:
		return 1

	elif x < limit and y < limit:
		return move(x+1, y, limit) + move(x, y+1, limit)

def grid_paths(limit):
	grid_size = limit+1
	grid = [[-1 for _ in range(grid_size)] for _ in range(grid_size)]

	# Fill first row and column
	for i in range(grid_size):
		grid[i][0] = 1
		grid[0][i] = 1

	for start in range(1, grid_size):
		# Fill one row and one column at the time
		for offset in range(0, grid_size-start):
			grid[start+offset][start] = grid[start+offset-1][start] + grid[start+offset][start-1]
			grid[start][start+offset] = grid[start-1][start+offset] + grid[start][start+offset-1]

	print_grid(grid)

def print_grid(grid):
	for row in grid:
		for num in row:
			print(f"{num: 3d} ", end="")
		print("")

def main():
	limit = 20
	grid_paths(limit)

if __name__ == '__main__':
	main()