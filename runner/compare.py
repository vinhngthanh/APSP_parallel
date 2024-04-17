def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1:
            file1_content = file1.read()

        with open(file2_path, 'r') as file2:
            file2_content = file2.read()

        if file1_content == file2_content:
            print("Files have identical content.")
        else:
            print("Files have different content.")

    except FileNotFoundError:
        print("One or both files not found.")


file1_path = './output/graph.txt'
file2_path = './output/graph_parallel.txt'
compare_files(file1_path, file2_path)
