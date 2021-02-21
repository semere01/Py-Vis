import pygame
import random
import math
from algorithms import Algorithms
from helpers import *

from draw_information import DrawInformation
pygame.init()



def main():
	algos = Algorithms()

	run = True
	clock = pygame.time.Clock()

	n = 50
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = DrawInformation(1000, 600, lst, pygame)
	sorting = False
	ascending = True

	sorting_algorithm = algos.bubble_sort
	sorting_algo_name = "Bubble Sort"
	sorting_algorithm_generator = None

	while run:
		clock.tick(60)

		if sorting:
			try:
				next(sorting_algorithm_generator)
			except StopIteration:
				sorting = False
		else:
			draw(draw_info, sorting_algo_name, ascending)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
				sorting = False
			elif not sorting:
				if event.key == pygame.K_a:
					ascending = True
				elif event.key == pygame.K_SPACE:
					sorting = True
					sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
				elif event.key == pygame.K_d:
					ascending = False
				elif event.key == pygame.K_i:
					sorting_algorithm = algos.insertion_sort
					sorting_algo_name = "Insertion Sort"
				elif event.key == pygame.K_b:
					sorting_algorithm = algos.bubble_sort
					sorting_algo_name = "Bubble Sort"
	pygame.quit()


if __name__ == "__main__":
	main()