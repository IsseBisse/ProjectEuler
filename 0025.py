fn_1 = 1
fn_2 = 1

idx = 2
while len(str(fn_2)) < 1000:
	temp = fn_2
	fn_2 = fn_1 + fn_2
	fn_1 = temp
	idx += 1

print(idx)