class qsort(object):
    def __init__(self, other_lst):
        self.data = other_lst

    def mysort(self, start_index, end_index):
        if start_index >= end_index:
            return
        store_index = start_index + 1
        for i in range(start_index + 1, end_index):
            if self.data[i] < self.data[start_index]:
                self.data[i], self.data[store_index] = self.data[store_index], self.data[i]
                store_index += 1
        self.data[start_index], self.data[store_index - 1] = self.data[store_index - 1], self.data[start_index]
        self.mysort(start_index, store_index - 1)
        self.mysort(store_index, end_index)

    def __repr__(self):
        return self.data

class score(object):
    def __init__(self):



if __name__ == '__main__':
    a = [3, 2, 1, 5, 4, 8, 7, 10, 9]
    b = qsort(a)
    b.mysort(0, 9)
    print(b.data)
