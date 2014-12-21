# coding=utf-8
import traceback


class Dataset(object):

    _data = {}

    def __init__(self):
        pass

    def read_data_points(self, file_path):
        """
        Reads the data into memory from given file_path
        Format must be 'x, y'
        :param file_path:
        :raise ValueError:
        """
        try:
            with open(file_path, 'r') as f:
                for i, line in enumerate(f):
                    key, value = line.split(",")

                    # raise errors if the input file is wrongly formatted
                    if len(key.split(" ")) > 1:
                        raise ValueError("Format should be 'x, y' on line " + str(i + 1))

                    if len(value.split(" ")) > 2:
                        raise ValueError("Format should be 'x, y' on line " + str(i + 1))

                    key = float(key.replace(" ", ""))
                    value = value.replace(" ", "")
                    value = float(value.replace("\n", ""))
                    self._data[key] = value

        except IOError as e:
            print "Opening file " + file_path + " failed:\n " + traceback.format_exc()

    def __getitem__(self, key):
        """
        Return value corresponding to key
        :param key:
        :return int:
        """
        return self._data[key]

    def __setitem__(self, key, value):
        """
        Update dictionary key
        :param key:
        :param value:
        """
        self._data[key] = value

    @property
    def data(self):
        """
        Return the entire dataset
        :return:
        """
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def get_x_values(self):
        """
        Return all the keys
        :return:
        """
        return self._data.keys()

    def get_y_values(self):
        """
        Return all the values
        :return:
        """
        return self._data.values()