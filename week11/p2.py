class qsort(object):
    def __init__(self):
        self.data = list()

    def add(self,k1,k2):
        k1 = int(k1)
        k2 = int(k2)
        self.data.extend(list(range(k1,k2+1)))

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

    def out_put(self):
        self.mysort(0,len(self.data))

        start_point = self.data[0]

        end_point = self.data[-1]
        index_c = (start_point-0)
        p_list = list(range(start_point,end_point+1))
        for i in self.data:
            p_list[i-index_c] = False
        for i in p_list:








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
        d[index] = '{} {} {}'.format(str(k1),int(k2),int(k3))
    ss = qsort(s)
    ss.mysort(0,m)
    for i in ss.data:
        print(d[i])


