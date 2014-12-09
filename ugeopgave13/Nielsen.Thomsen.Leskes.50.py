class Dataset:
    def __init__(self):
        self.data = {}

    def set_data_point(self, x, y):
        self.data[x] = y

    def get_data_point(self, x):
        return self.data[x]

    def read_data_points(self, file_path):
        f = open(file_path, 'r')
        print f

    def __str__(self):
        ans = []
        for i in self.data:
            ans += [i]
        return str(ans)

data1 = Dataset()
data1.set_data_point(3, 6)
data1.set_data_point(5, 11)
print data1