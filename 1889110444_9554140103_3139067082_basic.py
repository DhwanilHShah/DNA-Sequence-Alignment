import time
import psutil, os
import argparse

from utils import read_input_file, process_memory, write_output_file
# from divide_and_conquer import divide_conquer
from alignment import alignment

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-filepath", type = str, 
	help = "Input filepath", default='input.txt'
	)
parser.add_argument("-o", "--output-filepath", type = str, 
	help = "Input filepath", default='output.txt'
	)

def main():
	args = parser.parse_args()

	# Read input file
	input_filepath = args.input_filepath
	output_filepath = args.output_filepath
	x, y = read_input_file(input_filepath)

	# Hard coding cost values
	gap_cost = 30
	mismatch_cost = {'AA': 0, 'AC': 110, 'AG': 48, 'AT': 94, 'CA': 110, 
						'CC': 0, 'CG': 118, 'CT': 48, 'GA': 48, 'GC': 118, 
						'GG': 0, 'GT': 110, 'TA': 94, 'TC': 48, 'TG': 110, 
						'TT': 0
						}

	mem_before = process_memory()
	start_time = time.time()

	aligned_x, aligned_y, cost = alignment(
		x, y, len(x), len(y), mismatch_cost, gap_cost
		)

	end_time = time.time() - start_time
	mem_after = process_memory() - mem_before

	write_output_file(
		aligned_x, 
		aligned_y, 
		cost, 
		end_time, 
		mem_after, 
		output_filepath
		)

if __name__ == "__main__":
	main()