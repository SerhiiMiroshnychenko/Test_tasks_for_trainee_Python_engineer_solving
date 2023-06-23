# Task 1
"""
You will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and
circles ( radius - just a number ).
Your task is to return a new sequence of dimensions, sorted ascending by area.
For example,
const array = [ [4.23, 6.43], 1.23, 3.444, [1.342, 3.212] ]; // [ rectangle, circle, circle, rectangle ]
sortByArea(array) => [ [ 1.342, 3.212 ], 1.23, [ 4.23, 6.43 ], 3.444 ]
"""
from math import pi


def sortByArea(sequence: list) -> list:
    """
    Function that sorts rectangles and circles in the list by their area

    :param sequence: list of lists or numbers(float and int):
                     series of the dimensions of rectangles and circles
    :return: the list is sorted by area
    """
    return  sorted(sequence, key=lambda x: x[0]*x[1] if isinstance(x, list) else pi*x**2)


if __name__ == "__main__":

    array = [[4.23, 6.43], 1.23, 3.444, [1.342, 3.212]]
    array1 = [[1, 2.3], [3, 4], [5.12, 6.25], [2, 3], [5.5, 1]]
    array2 = [2, 3, 4.44, 1,23, 2.22, 5, 6.7, 1.111]
    array3 = array + array1 + array2
    assert sortByArea(array) == [[1.342, 3.212], 1.23, [4.23, 6.43], 3.444]

    for arr in (array, array1, array2, array3):
        print(sortByArea(arr))
