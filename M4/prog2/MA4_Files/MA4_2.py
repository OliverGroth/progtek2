#!/usr/bin/env python3.9

from person import Person
import time

def main():
	x = list(range(35,46))
	times_cpp = []
	for n in x:

		f = Person(n)
	print(f.get())
	f.set(7)
	print(f.get())
	print(fib_py(f.get()))
	print(f.fib())


def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

if __name__ == '__main__':
	main()