iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    iris[id_n] = {}
    my_dict = dict(species=species, petal_length=petal_length, petal_width=petal_width)
    for key, value in kwargs.items():
        my_dict[key] = value
    iris[id_n].update(my_dict)
