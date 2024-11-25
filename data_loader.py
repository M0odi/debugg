def load_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [x for x in data]