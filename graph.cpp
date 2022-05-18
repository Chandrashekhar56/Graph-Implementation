#include <bits/stdc++.h>
using namespace std;
void Add_New_Edge(vector<int> adjency_list[], int source_vertex, int destination_vertex)
{
	adjency_list[source_vertex].push_back(destination_vertex);
	adjency_list[destination_vertex].push_back(source_vertex);
}
void display(vector<int> adjency_list[], int total_vertices)
{
	for (int i = 0; i < total_vertices; ++i) {
		cout << "Adjency list : \n" <<"source vetrex: "<<i<<"\n";
		for (auto m : adjency_list[i])
			cout <<"destination vertex:  -> " << m<<"\n";
		printf("\n");
	}
}
int main()
{
	int total_vertices = 5;
	vector<int> adjency_list[total_vertices];
	Add_New_Edge(adjency_list, 0, 1);
	Add_New_Edge(adjency_list, 0, 4);
	Add_New_Edge(adjency_list, 1, 2);
	Add_New_Edge(adjency_list, 1, 3);
	Add_New_Edge(adjency_list, 3, 2);
	Add_New_Edge(adjency_list, 4, 1);
    Add_New_Edge(adjency_list, 3, 4);
	display(adjency_list, total_vertices);
	return 0;
}
