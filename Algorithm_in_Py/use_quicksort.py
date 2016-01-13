import copy


def Partition(a, s, t):  # 划分算法
    i, j = s, t
    tmp = a[s]
    while (i != j):
        while (j > i and a[j] >= tmp):
            j -= 1
        a[i] = a[j]
        while (i < j and a[i] <= tmp):
            i += 1
        a[j] = a[i]
    a[i] = tmp
    return i


def QuickSort(a, s, t):  # 对a[s...t]元素序列进行递增排序
    if (s < t):
        i = Partition(a, s, t)
        QuickSort(a, s, i - 1)
        QuickSort(a, i + 1, t)


if __name__ == "__main__":
    a = [2, 5, 1, 7, 10, 6, 9, 4, 3, 8]
    b = copy.deepcopy(a)
    print(id(a))
    print(id(b))
    print("排序前：", a)
    QuickSort(a, 0, len(a) - 1)
    print("排序后：", a)
    print("排序前：", b)
    print(type(b))
    b.sort()
    print("排序后：", b)
