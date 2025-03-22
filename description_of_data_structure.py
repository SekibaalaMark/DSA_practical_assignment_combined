
#Graph represention using an adjacency list
adjacency_list = {
    1: {2: 12, 3: 10, 7: 12},
    2: {1: 12, 3: 8, 4: 12},
    3: {1: 10, 2: 8, 4: 11, 5: 3, 7: 9},
    4: {2: 12, 3: 11, 5: 11, 6: 10},
    5: {3: 3, 4: 11, 6: 6, 7: 7},
    6: {4: 10, 5: 6, 7: 9},
    7: {1: 12, 3: 9, 5: 7, 6: 9}
}

'''
The main keys are representing the city node
the inner keys are representing the cities the that the city on the main can access and the values to these keys are the distances
between the city on the main key and the city on the inner key 
'''


'''
city one can access city 2 and the distance between city 2 and 1 12
city 1 can access city 3 through a distance of 10
city 1 can access city 7 through a distance of 12

same procedure for all other cities
'''
