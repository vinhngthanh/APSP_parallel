CSC 458 - Final Project
Professor: Andrew Read-McFarland

Name: Vinh Nguyen (vnguy23)

I, Explanation of the file system:
    1, apsp.cpp:
    The apsp.cpp file contains the basic implementation of the Floyd–Warshall algorithm.

    2, apsp_parallel.cpp:
    The apsp.cpp file contains the parallel implementation of the Floyd–Warshall algorithm.

    3, tests/generate.py:
    The generate.py file is used to generate tests and print them into the test text files.

    4, runner/run.py:
    The run.py file is used to execute the Floyd–Warshall algorithm on 6 tests and print the results to the output text files.

    5, runner/compare.py:
    The compare.py file is used to compare the results of the parallel version with the serial version.

    6, summary/summary.py:
    The summary.py file is used to read from all the output files and summarize the result into the summary.txt file.

    7, graph/avgGraph.ipynb:
    This file contains the graph of the average runtime of the Floyd–Warshall algorithm on the 6 tests.

    8, graph/speedupGraph.ipynb:
    This file contains the graph of the speedup of different amount of threads on the 6 tests.

II, Explanation of code:
    apsp.cpp:
        The code implements the Floyd-Warshall algorithm for finding the shortest paths between all pairs of vertices in a given weighted graph 
        with n vertices. The main function begins by timing the execution, reading the size n of the adjacency matrix from the input, and then 
        populating this matrix from user input. The apsp (All Pairs Shortest Path) function then modifies this matrix to reflect the shortest 
        paths between each pair of vertices by using a triple nested loop to update the path lengths iteratively. For each vertex k, the algorithm 
        checks if a direct path between any two vertices i and j is shorter than a path that goes through k. If so, it updates the matrix entry to 
        reflect this shorter path. By considering each vertex as an intermediate point in paths between all possible pairs of vertices, the 
        algorithm ensures that the resulting matrix contains the shortest path distances between all pairs of vertices. After the shortest paths 
        have been computed, the dynamically allocated memory for the graph is freed, and the total execution time (in milliseconds) of the program 
        (from the setup to memory deallocation) is printed. The function to print the matrix has been provided but commented out, you can 
        uncomment it to see the result graph.
    apsp_parallel.cpp:
        Everything here is the same as the serial version except for the apsp function where it takes in an additional number of threads. Inside
        this function, the algorithm is parallelized using OpenMP directives. The outer loop, iterating over each vertex k as an intermediate point, 
        is executed in sequence. The inner two loops, which iterate over all pairs of vertices i and j, are parallelized. The computation of the 
        shortest path that might include vertex k as an intermediate point is distributed among the available threads. This parallelization is 
        achieved using the #pragma omp parallel directive with nested #pragma omp for for distributing the iterations of the loop over i, and 
        dynamically scheduling chunks of iterations to different threads to balance the workload efficiently.
III, Raw data:
    You can find the raw output data in the ouput folder.
IV, How to run:
    1, apsp.cpp:
        Locate to the root folder.
        Example compile and run of apsp.cpp file with test1.txt as input.
        Compile: g++ apsp.cpp -o apsp
        Run: 
            Linux: cat ./tests/test1.txt | ./apsp
        Output location: Terminal

        You can uncomment print(graph, n); to print the result graph.

    2, apsp_parallel.cpp:
        Locate to the root folder.
        Example compile and run of apsp_parallel.cpp file with test1.txt as input with 8 threads.
        Compile: g++ apsp_parallel.cpp -o apsp_parallel -fopenmp
        Run: 
            Linux: cat ./tests/test1.txt | ./apsp_parallel 8
        Output location: Terminal

        You can uncomment print(graph, n); to print the result graph.

    3, runner/run.py:
        Locate to the root folder.
        Run: python ./runner/run.py
        Output location: output/output{1 - 6}.txt

    4, summary/summary.py:
        Locate to the summary folder.
        Run: python ./summary.py
        Output location: summary/summary.txt
    
    5, graph/avgGraph.ipynb:
        Go into the file.
        Run: Click on "Run All".
        Output location: In file.

    6, graph/speedupGraph.ipynb:
        Go into the file.
        Run: Click on "Run All".
        Output location: In file.