from itertools import permutations

COINS = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0]

# too slow
possible_chains = list()
def add_link(chain, value):
	if sum(chain) == value:
		possible_chains.append(chain)
		return

	for coin in COINS:
		if sum(chain) + coin <= value:
			add_link(chain + [coin], value) 

def possible_permutations(value):
	for coin in COINS:
		if coin <= value:
			add_link([coin], value)

	possible_unique_chains = set([",".join([str(coin) for coin in sorted(chain)]) for chain in possible_chains])
	return possible_unique_chains

"""this is somehow even worse...
def change_chain(chain):
	new_chains = list()
	done_chains = list()
	for coin in COINS[1:]:
		num_pennies = int(coin / 0.01)
		
		if num_pennies <= chain[0.01]:
			new_chain = {**chain}
			new_chain[0.01] -= num_pennies
			if coin in chain:
				new_chain[coin] += 1

			else:
				new_chain[coin] = 1

			if new_chain[0.01] <= 1:
				done_chains.append(new_chain)
			else:
				new_chains.append(new_chain)

	return new_chains, done_chains
"""

COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def num_combinations(target):
	combinations = [0] * (target+1)

	combinations[0] = 1
	for coin in COINS:
		for idx in range(coin, target+1):
			combinations[idx] += combinations[idx - coin]

	return combinations[target]

	print(combinations)

def main():
	print(200, num_combinations(200))

if __name__ == '__main__':
	main()