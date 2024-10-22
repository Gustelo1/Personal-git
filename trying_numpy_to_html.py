import numpy as np
import matplotlib.pyplot as plt
import time

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

def check_if_edge(new_m):
    mask = np.logical_or(
        np.isin(element=m[:, m.shape[0] - 2], test_elements=1),
        np.isin(element=m[m.shape[0] - 2, :], test_elements=1)
    )

    mask2 = np.logical_or(
        np.isin(element=m[:,1],test_elements=1),
        np.isin(element=m[1, :], test_elements=1)
    )

    if mask.any():
        new_m = np.pad(m, pad_width=((0, 1), (0, 1)), mode='constant', constant_values=0)

    if mask2.any():
        new_m = np.pad(m, pad_width=((1, 0), (1, 0)), mode='constant', constant_values=0)

    return new_m

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
    new_m = check_if_edge(new_m)
    return new_m
def get_table():
    m = np.zeros((20,20))

    m[15,2] = 1
    m[16,3] = 1
    m[17,3] = 1
    m[17,2] = 1
    m[17,1] = 1

    m[5, 7] = 1
    m[4, 8] = 1
    m[4, 9] = 1
    m[5, 9] = 1
    m[6, 9] = 1

    html = "<table border='1' id='game-table'>"
    for i, row in enumerate(m):
        html += "<tr>"
        for j, value in enumerate(row):
            cell_value = 'white-cell' if value == 1 else 'black-cell'
            html += f"<td class='{cell_value}' data-row='{i}' data-col='{j}' onclick='toggleCell(this)'></td>"
        html += "</tr>"
    html += "</table>"
    return html