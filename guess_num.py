import random
print("there is a random number please guess it")
print("1")
print("2")
print("3")
print("please write any number from options")
n = int(input())
r = random.randint(1,3)
if n == r:
	print("good")
else:
	print("sorry you can retry")
