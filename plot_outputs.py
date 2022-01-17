import matplotlib.pyplot as plt
import pandas as pd

def plot_cpu_time(df):
	df.plot.line('size', ['basic_time', 'efficient_time'])
	# plt.title('CPU Time vs Problem Size')
	# plt.xlabel('Problem Size')
	# plt.ylabel('Time(in seconds)')
	plt.show()
	# plt.savefig('CPUPlot.png', format='png')

def plot_memory(df):
	df.plot.line('size', ['basic_space', 'efficient_space'])
	# plt.title('Memory space vs Problem Size')
	# plt.xlabel('Problem Size')
	# plt.ylabel('Memory(in kilobytes)')
	plt.show()
	# plt.savefig('MemoryPlot.png', format='png')

def plot(csv_file):
	df = pd.read_csv(csv_file)

	plot_cpu_time(df)
	plot_memory(df)

if __name__ == "__main__":
	csv_filename = 'plot_output.csv'

	plot(csv_filename)
	