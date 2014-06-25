#ifndef _INTERFACE_CCORE_H_
#define _INTERFACE_CCORE_H_

typedef struct cluster_representation {
	unsigned int size;
	unsigned int * objects;
} cluster_representation;

typedef struct clustering_result {
	unsigned int size;
	cluster_representation * clusters;
} clustering_result;

typedef struct data_representation {
	unsigned int size;
	unsigned int dimension;
	double ** objects;
};

extern "C" __declspec(dllexport) void free_clustering_result(clustering_result * pointer);

/* extern "C" __declspec(dllexport) clustering_result * dbscan_algorithm(const char * const path_file, const double radius, const unsigned int minumum_neighbors); */
extern "C" __declspec(dllexport) clustering_result * dbscan_algorithm(const data_representation * const path_file, const double radius, const unsigned int minumum_neighbors);

#endif