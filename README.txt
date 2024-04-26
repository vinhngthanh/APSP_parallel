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
        This lock only has two functions and one atomic variable. The atomic variable called locked is a boolean which is true when the lock is
        locked and false otherwise. The lock function has a while loop which will try to replace locked with true. If locked is already true, it
        will spin until locked is false. The unlock function simply sets locked to false.
    apsp_parallel.cpp:
        In this read write lock implementation, I use an atomic int called readers to keep track of number of readers. When a reader want to get
        a lock, if readers = 0 meaning the lock is there to take, it will try to aquire the lock. But if readers > 0, meaning a reader already had
        the lock, it can continue to take the lock too because many readers can take the lock at the same time. For the readUnlock function, since
        we have a lot of readers having the lock at the same time, calling unlock early can lead to wrong answer so we decrement the reader by 1
        each time the function is called. Only when reader is 0 we will release the lock for contest. writeLock and writeUnlock just try to take the
        lock and release the lock in this case. During testing, I realized that the variables can somehow be affected even when I use atomic so I
        has to created another mutex called rmtx to lock the readLock and readUnlock function.
III, Raw data:
    You can find the raw output data in the ouput folder.
IV, How to run:
    1, test{i}.cpp (i is the program you want to run):
        Locate to the a2 folder.
        Example compile and run of test1.cpp file with test1.txt as input.
        Compile: g++ test1.cpp -o test1
        Run: 
            Linux: cat ./tests/test1.txt | ./test1
        Output location: Terminal

    2, runner.py:
        Run: python runner.py
        Output location: output{1-4}.txt

    3, summary.py:
        Run: python summary.py
        Output location: summary.txt