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

    '''Checks the two vectors are compatible with the operation requested'''
    def check_vector(self, v):
        try:
            if self.dimension != v.dimension:
                raise AttributeError
            elif v.__class__.__name__ != 'Vector':
                raise AttributeError

        except AttributeError:
            raise AttributeError('Dimension of the vectors are not compatible')

        except TypeError:
            raise TypeError('The class used in the sum is not compatible with the Vector class')

    '''Function that returns the default signature of the vector (Coordinates)'''
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    '''Rewrites how the function that compares if another vector is equal'''
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    '''Define how the sum function works for two vectors'''
    def __add__(self, v):
           self.check_vector(v)
           coordinates = list(((self.coordinates[i] + v.coordinates[i]) for i in range(self.dimension)))
           print(coordinates)
           return Vector(coordinates)


    '''Define how the sub function works for two vectors'''
    def __sub__(self, v):
        self.check_vector(v)
        coordinates = list(map(lambda i: (self.coordinates[i] - v.coordinates[i]), range(self.dimension)))
        return Vector(coordinates)

    '''Define how the multiplication works (Scalar Multiplication)'''
    def __mul__(self, s):
        try:
            if not str(s).isdigit():
                raise ValueError
            else:
                return Vector(list(map(lambda i: (self.coordinates[i] * s), range(self.dimension))))

        except ValueError:
            raise ValueError('Invalid type to perform Scalar Multiplication, please define a number')



    # TODO: Make graphical example of vectors operations
if __name__ == '__main__':
    my_vector = Vector([1,2,3])
    my_vector_2 = Vector([1,2,3])
    my_vector_3 = Vector([-1,2,3])

    print(my_vector)
    print(my_vector == my_vector_2)
    print(my_vector == my_vector_3)

    print(my_vector + my_vector_2)
    print(my_vector - my_vector_2)
    print(my_vector * 2)