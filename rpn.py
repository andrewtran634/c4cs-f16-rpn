#!/usr/bin/env python3

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	# '^': operator.pow
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			func = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = func(arg1, arg2)
			stack.append(result)	
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many params")
	return stack.pop()
def main():
	while True:
		result = calculate(input("rpn calc> "))
		print(result)

if __name__ == '__main__':
	main()
