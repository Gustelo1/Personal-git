import numpy as np
import matplotlib.pyplot as plt
import time
# np.random.seed(200)
# m = np.zeros((20,20))
# random_ones = np.random.choice(m.size, 200, replace=False)
# m.ravel()[random_ones] = 1

def get_all_neighbor_index(m,location):
    rows, cols = m.shape
    array = []
    if location[0] <= 0 or location[0] >= rows - 1 or location[1] <= 0 or location[1] >= cols - 1:
        return None

    for row in range(-1,2):
        for col in range(-1,2):
            array.append((location[0]+row,location[1]+col))
    array.remove(location)
    return array

def get_neighbor_values(m,array):
    values = []
    for neigbor in array:
        values.append(m[neigbor])

    return sum(values)

def get_new_generation(m):
    new_m = m.copy()
    for index, value in np.ndenumerate(m):
        status = m[(index)]
        array = get_all_neighbor_index(m,index)
        if array:
            values = get_neighbor_values(m,array)

            if values < 2 and status == 1:
                new_m[(index)] = 0
            if values > 3 and status == 1:
                new_m[(index)] = 0
            if values == 3 and status ==0:
                new_m[(index)] = 1
    return new_m

m = np.zeros((20,20))

m[3,2] = 1
m[4,3] = 1
m[5,3] = 1
m[5,2] = 1
m[5,1] = 1
for i in range(100):
    plt.imshow(m,cmap='gray_r')
    plt.show()
    time.sleep(0.12)
    m = get_new_generation(m)
