
def question(n, arr):
    i = 0
    j = 0
    while (i < n):
        i += 1
        while ((j < n) and (arr[i] < arr[j])):
            j += 1
            print("comparacion")


def test_for(n):
    i = 0
    while i < n:
        i += 1
        print("A")

    i = 0
    while i < n:
        i += 2
        print("B")

    i = 1
    while i < n:
        i *= 2
        print("C")

    i = n
    while i > 0:
        i -= 1
        print("D")


listNode = {'data': None, 'next': None}


def method(head):
    if head is None:
        return head

    print(str(head['data']) + ' ')

    if (head['next'] is not None):
        method(head['next']['next'])

    print(str(head['data']) + ' ')
    return head


def complejidad(n, arr):
    i = 0
    j = 0
    while (i < n):
        i += 1
        while ((j < n) and (arr[i] < arr[j])):
            j += 1
            print('op')


def complejidad2(n):
    i = 0
    j = 0
    while (i < n):
        i += 1
        while ((j < n)):
            j += 1
            print('op2')


def main():
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    question(9, arr)
    test_for(10)
    head = None
    var1 = {'data': 1, 'next': None}
    var2 = {'data': 2, 'next': None}
    var3 = {'data': 3, 'next': None}
    var4 = {'data': 4, 'next': None} 
    var5 = {'data': 5, 'next': None} 
    var6 = {'data': 6, 'next': None} 

    var1['next'] = var2
    var2['next'] = var3
    var3['next'] = var4
    var4['next'] = var5
    var5['next'] = var6
    head = var1
    method(head)

    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    complejidad(9, arr)
    complejidad2(9)


if __name__ == "__main__":
    main()
