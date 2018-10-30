def qsort(start_index, end_index):
    if start_index >= end_index:
        return
    global a
    store_index = start_index + 1
    for i in range(start_index + 1, end_index):
        if a[i] < a[start_index]:
            a[i], a[store_index] = a[store_index], a[i]
            store_index += 1
    a[start_index], a[store_index - 1] = a[store_index - 1], a[start_index]
    qsort(start_index, store_index - 1)
    qsort(store_index, end_index)


def myprint(s, e):
    print(int(s),':',int(e))


if __name__ == '__main__':
    # data = input().split(' ')
    data = ['2:6', '3:10', '15:20', '23:23', '0:0']
    p_list = list()
    # ss = qsort()
    for i in data:
        k1, k2 = i.split(":")
        k1 = int(k1)
        k2 = int(k2)
        p_list.extend(list(range(k1, k2 + 1)))
    a = p_list
    qsort(0, len(a))
    p_list = set(a)
    # print(p_list)
    p_list = list(p_list)
    c = 0
    start_point = p_list[0]
    for i in p_list:
        if i is p_list[-1]:
            myprint(start_point, i)
            break
        elif p_list[c + 1] > i + 1:
            myprint(start_point, i)
            start_point = p_list[c + 1]
        c += 1
