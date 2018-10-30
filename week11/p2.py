class qsort(object):
    def __init__(self):
        self.data = list()

    def add(self, k1, k2):
        k1 = int(k1)
        k2 = int(k2)
        self.data.extend(list(range(k1, k2 + 1)))

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
        self.mysort(0, len(self.data))

        start_point = self.data[0]

        end_point = self.data[-1]
        s_list = list()
        p_list = list(range(start_point,end_point+1))
        c = 0
        for i in p_list:
            if i in self.data:
                s_list.append(i)
        for i in s_list:
            if i is s_list[-1]:
                myprint(start_point,i)
                return
            elif s_list[c+1] > i+1:
                myprint(start_point,i)
                start_point = s_list[c+1]
                c += 1

def myprint(s,e):
    print('{}:{}'.format(s,e))


if __name__ == '__main__':
    # data = input().split(' ')
    data = ['0:6', '1:10', '15:20', '23:23']
    ss = qsort()
    for i in data:
        k1, k2 = i.split(":")
        ss.add(k1, k2)
    ss.out_put()
