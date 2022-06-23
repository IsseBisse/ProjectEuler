def get_names():
	with open("0022.txt") as file:
		text = file.read()

	names = [name.replace("\"", "").lower() for name in text.split(",")]
	return sorted(names)

def get_score(name, idx):
	print(name, idx)
	return idx * sum([ord(c)-96 for c in name])

def main():
	names = get_names()
	idx = range(1, len(names)+1)

	print(sum(map(get_score, names, idx)))

if __name__ == '__main__':
	main()