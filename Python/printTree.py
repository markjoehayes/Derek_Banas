#!/usr/bin/python3

# Promt user for the height and print a tree (triangle with a single # base) of #s

def print_triangle(height):
    for i in range(height):
        print(' ' * (height - i) + '#' * (2 * i - 1))

def main():
	height = int(input("Enter the height you want your tree: "))
	print_triangle(height)
	print(' ' * (height -1) + '#')

main()


