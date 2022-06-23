fn_1 = 1
fn_2 = 1

idx = 2
while fn_2 < 1e400:
	temp = fn_2
	fn_2 = fn_1 + fn_2
	fn_1 = temp
	idx += 1

print(idx)