import psutil, os

def read_input_file(input_filepath = 'input.txt'):
    '''
    Reads the input file

    Arg(s):
        input_filepath(str, path): Path of the input file
    Output(s):
        X(str): String 1 to align 
        Y(str): String 2 to align
    '''
    with open(input_filepath,'r') as f:
        contents = f.readlines()
    n = len(contents)

    X = contents[0][:-1]

    i = 1
    while contents[i][0] not in ['A', 'C', 'T', 'G']:
        index = int(contents[i][:-1])
        X = X[:index+1] + X + X[index+1:]
        i+=1

    Y = contents[i][:-1]
    i+=1

    while i < n-1:
        index = int(contents[i][:-1])
        Y = Y[:index + 1] + Y + Y[index + 1:]
        i+=1

    index = int(contents[i])
    Y = Y[:index + 1] + Y + Y[index + 1:]

    return (X,Y)

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def write_output_file(
    aligned_x, 
    aligned_y, 
    cost, 
    time, 
    memory, 
    output_filepath = 'output.txt'
):
    lines = []
    lines.append(aligned_x[:50] + " " + aligned_x[-50:] + "\n")
    lines.append(aligned_y[:50] + " " + aligned_y[-50:] + '\n')
    lines.append("{0:0.1f}".format(cost) + '\n')
    lines.append("{}".format(time) + '\n')
    lines.append("{0:0.1f}".format(memory) + '\n')

    with open(output_filepath, 'w+') as f:
        f.writelines(lines)

    