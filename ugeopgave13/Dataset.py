class Dataset:

    __data = {}

    def __init__(self):
        self.__data = {}

    def read_data_points(self, file_path):
        f = open(file_path, 'r')

        for i, line in enumerate(f):
            try:
                key, value = line.split(",")

                if len(key.split(" ")) > 1: raise ValueError("")
                if len(value.split(" ")) > 2: raise ValueError("")

                key = float(key.replace(" ", ""))
                value = value.replace(" ", "")
                value = float(value.replace("\n", ""))
                self.__data[key] = value
            except ValueError as e:
                print "Input can only be two comma-separated values on line " + str(i+1)

    def get(self, key):
        return self.__data[key]

    def put(self, key, value):
        self.__data[key] = value

    def set_data(self, data={}):
        self.__data = data

    def get_data(self):
        return self.__data

    def get_x_values(self):
        return self.__data.keys()

    def get_y_values(self):
        return self.__data.values()