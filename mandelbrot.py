#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.


import numpy as np
import curses

import colors

MAX_ITERS = 100
ITERATIONS = 0
COLOR_COUNT = 101
MONOCHROME = False
ZOOM_LEVEL = 0
X_SCALE = 1.75
Y_SCALE = 1
X_MID = -0.75
Y_MID = 0


def get_points(cols, rows):
	x_min = X_MID - X_SCALE * (1 / (2 ** ZOOM_LEVEL))
	x_max = X_MID + X_SCALE * (1 / (2 ** ZOOM_LEVEL))
	y_min = Y_MID - Y_SCALE * (1 / (2 ** ZOOM_LEVEL))
	y_max = Y_MID + Y_SCALE * (1 / (2 ** ZOOM_LEVEL))
	x = np.linspace(x_min, x_max, cols)
	y = np.linspace(y_min, y_max, rows)
	return x, y


def calculate_point(x, y):
	global ITERATIONS
	z = 0
	for i in range(MAX_ITERS):
		ITERATIONS += 1
		z = z ** 2 + complex(x, y)
		if abs(z) >= 2:
			return i

	return -1


def calculate_set(cols, rows):
	global ITERATIONS
	ITERATIONS = 0
	x, y = get_points(cols, rows)
	matrix = np.zeros([rows, cols])
	for i in range(rows):
		for j in range(cols):
			matrix[i, j] = calculate_point(x[j], y[i])

	return matrix


def print_set(screen, cols, rows, matrix, char):
	screen.clear()
	for i in range(rows):
		for j in range(cols):
			iteration = matrix[i, j]
			if iteration == -1:
				screen.addstr(i, j, ' ', curses.color_pair(1))
			else:
				color_index = (int(iteration) + 2) % COLOR_COUNT
				color_index = 2 if color_index < 2 else color_index
				screen.addstr(i, j, ' ', curses.color_pair(color_index))

	screen.addstr(rows, 0, f'Max Iterations: {MAX_ITERS}, Zoom: {ZOOM_LEVEL}, Iterations: {ITERATIONS}, Char: {char}', curses.color_pair(COLOR_COUNT))
	screen.refresh()


def handle_keyboard(char):
	global X_MID
	global Y_MID
	global ZOOM_LEVEL
	global MAX_ITERS
	global MONOCHROME
	global COLOR_COUNT

	if char == 113:
		return True
	elif char == 258:  # Down
		Y_MID += Y_SCALE * (1 / (2 ** (ZOOM_LEVEL + 1)))
		return False
	elif char == 259:  # Up
		Y_MID -= Y_SCALE * (1 / (2 ** (ZOOM_LEVEL + 1)))
		return False
	elif char == 260:  # Left
		X_MID -= X_SCALE * (1 / (2 ** (ZOOM_LEVEL + 1)))
		return False
	elif char == 261:  # Right
		X_MID += X_SCALE * (1 / (2 ** (ZOOM_LEVEL + 1)))
		return False
	elif char == 40:  # Zoom out
		if ZOOM_LEVEL > 0:
			ZOOM_LEVEL -= 1
		return False
	elif char == 41:  # Zoom in
		ZOOM_LEVEL += 1
		return False
	elif char == 61:  # Zoom reset
		ZOOM_LEVEL = 0
		return False
	elif char == 43:  # Iterations up
		MAX_ITERS += 1
		return False
	elif char == 45:  # Iterations down
		MAX_ITERS = 1 if MAX_ITERS == 1 else MAX_ITERS - 1
		return False
	elif char == 99:  # Toggle colors
		if MONOCHROME:
			COLOR_COUNT = colors.init_101_colors()
			MONOCHROME = False
		else:
			COLOR_COUNT = colors.init_101_monochrome()
			MONOCHROME = True

		return False


def main(screen):
	global COLOR_COUNT
	rows, cols = screen.getmaxyx()
	rows -= 1
	COLOR_COUNT = colors.init_101_colors()
	char = 0
	while True:
		matrix = calculate_set(cols, rows)
		print_set(screen, cols, rows, matrix, char)
		char = screen.getch()
		if handle_keyboard(char):
			break


if __name__ == '__main__':
	curses.wrapper(main)

