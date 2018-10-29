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

def str_to_int(k1,k2):
    k1 = int(k1)
    k2 = str(k2)
    s = ((100-k1)*(26**11))
    c = 10
    for i in k2:
        s += (ord(i)*(26**c))
        c -= 1
    return s


if __name__ == '__main__':
    # a = [3, 2, 1, 5, 4, 8, 7, 10, 9]
    # b = qsort(a)
    # b.mysort(0, 9)
    # print(b.data)
    data = [(50,'sun'),(50,'zhang'),(80,'sun'),(90,'zhang'),(90,'sun')]
    s = []

    for k1,k2 in data:
        a = str_to_int(k1,k2)
        s.append(a)
    ss = qsort(s)
    ss.mysort(0,5)
    print(ss.data)


