def prime(n):
	not_prime = False
	list_primes = [1]
	for i in range(2, n):
		for j in range(2, i):
			not_prime = False
			if i % j == 0:
				not_prime = True
				break
		if not not_prime:
			list_primes.append(i)
	return list_primes

def prime2(n):
	list_primes = [1]
	for i in range(2, n):
		l1 = [True for x in range(2, i) if i % x == 0]
		if len(l1) == 0:
			list_primes.append(i)
	return list_primes


def func(n):
	list_even = []
	for i in range(0, n):
		if i % 2 == 0:
			list_even.append(i)
	return list_even

def func2(n):
	return [x for x in range(n) if x % 2 == 0]

print(func(20) == func2(20))