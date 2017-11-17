'''This class is a tool to represent vectors.'''
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('Coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an interable')

    '''Function that returns the default signature of the vector (Coordinates)'''
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    '''Rewrites how the function that compares if another vector is equal'''
    def __eq__(self, v):
        return self.coordinates == v.coordinates

if __name__ == '__main__':
    my_vector = Vector([1,2,3])
    my_vector_2 = Vector([1,2,3])
    my_vector_3 = Vector([-1,2,3])

    print(my_vector)
    print(my_vector == my_vector_2)
    print(my_vector == my_vector_3)