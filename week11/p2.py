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
        s_list = list()

        for i in self.data:
            p_list[i-index_c] = False
        for i in p_list:
            if i is not False:
                s_list.append(i)
        c = 0
        for i in s_list:
            if c is 0:
                print('{}:{}'.format(start_point,s_list[0]-1))
                c += 1
            if c>0 and c< len(s_list):
                if s_list[c-1]+1-s_list[c]-1>0:
                    print('{}:{}'.format(s_list[c-1]+1,s_list[c]-1))
                c += 1
            if c is len(s_list):
                print('{}:{}'.format(s_list[c - 1] + 1, end_point))
                return













if __name__ == '__main__':
    data = input().split(' ')
    ss = qsort()
    for i in data:
        k1,k2 = i.split(":")
        ss.add(k1,k2)
    ss.out_put()


