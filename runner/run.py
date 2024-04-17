import subprocess

num_tests = 6
iterations_per_test = 10
num_threads = [1, 2, 4, 8, 10, 16, 20, 24, 32, 40, 64]

for i in range(1, num_tests + 1):
    destination = './output/output' + str(i) + '.txt'
    with open(destination, 'w') as output_file:
        for j in num_threads:
            if j == 1:
                for iteration in range(1, iterations_per_test + 1):
                    output_file.write(f'Running test {i} iteration {iteration} with 1 thread:\n')

                    command = f'cat ./tests/test{i}.txt | ./apsp'
                    try:
                        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                        output_file.write(result.stdout)
                    except subprocess.CalledProcessError as e:
                        output_file.write('Failed to execute command: ' + str(e) + '\n')

                    if iteration == iterations_per_test:
                        output_file.write('\n')
            else:
                for iteration in range(1, iterations_per_test + 1):
                    output_file.write(f'Running test {i} iteration {iteration} with {j} thread:\n')

                    command = f'cat ./tests/test{i}.txt | ./apsp_parallel {j}'
                    try:
                        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                        output_file.write(result.stdout)
                    except subprocess.CalledProcessError as e:
                        output_file.write('Failed to execute command: ' + str(e) + '\n')

                    if iteration == iterations_per_test:
                        output_file.write('\n')