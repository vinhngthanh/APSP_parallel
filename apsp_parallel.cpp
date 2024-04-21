#include <iostream>
#include <stdlib.h>
#include <chrono>
#include <omp.h>

using namespace std;

int INF = 2147483647;

void apsp(int **graph, int n, int numThread)
{
    omp_set_num_threads(numThread);
    #pragma omp parallel for
    for (int k = 0; k < n; k++)
    {
        // #pragma omp parallel for
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if(graph[i][j] > graph[i][k] + graph[k][j]){
                    graph[i][j] = graph[i][k] + graph[k][j];
                }          
            }
        }
    }
}

void print(int **graph, int n)
{   
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << graph[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}

int main()
{
    using chrono::high_resolution_clock;
	using chrono::duration;
	
	auto start = high_resolution_clock::now();

    int n;
    cin >> n;

    int **graph = new int *[n];

    for (int i = 0; i < n; i++)
    {
        graph[i] = new int[n];
        for (int j = 0; j < n; j++)
        {
            cin >> graph[i][j];
        }
    }

    int numThread;
    cin >> numThread;
    apsp(graph, n, numThread);
    print(graph, n);

    for (int i = 0; i < n; i++)
    {
        delete[] graph[i];
    }
    delete[] graph;
    
    auto end = high_resolution_clock::now();
	duration<double, milli> time = end - start;
	
	// cout << "Duration: " << time.count() << " miliseconds." << endl;
}
