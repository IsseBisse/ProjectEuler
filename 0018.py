def read_tree():
	with open("0018.txt") as file:
		text = file.read()

	tree = [[int(num) for num in row.split(" ")] for row in text.split("\n")]
	return tree

def fill_cumsum_tree(tree):
	cumsum_tree = [[-1 for _ in range(len(row))] for row in tree]
	cumsum_tree = [[-1 for _ in range(len(row))] for row in tree]

	cumsum_tree[-1] = tree[-1]

	for row_idx in reversed(range(1, len(tree))):
		for col_idx in range(len(cumsum_tree[row_idx-1])):
			cumsum_tree[row_idx-1][col_idx] = tree[row_idx-1][col_idx] + max(cumsum_tree[row_idx][col_idx], cumsum_tree[row_idx][col_idx+1])
		
	return cumsum_tree

def main():
	tree = read_tree()
	cumsum_tree = fill_cumsum_tree(tree)
	print(cumsum_tree[0][0])

if __name__ == '__main__':
	main()