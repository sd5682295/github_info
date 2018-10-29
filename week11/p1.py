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
    s = (k1*(26**11))
    c = 10
    for i in k2:
        s += (ord(i)*(26**c))
        c -= 1
    return s


if __name__ == '__main__':
    m = int(input())
    s =[]
    d = dict()
    for _ in range(m):
        k1,k2,k3 = input().split(' ')
        k3 = int(k3)
        k1 = str(k1)
        index = (str_to_int(k3,k1))
        s.append(index)
        d[index] = '{} {} {}'.format(str(k1),str(k2),str(k3))
    ss = qsort(s)
    ss.mysort(0,m)
    for i in ss.data:
        print(d[i])


