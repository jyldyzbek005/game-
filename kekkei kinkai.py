list = [('video', 9), 
    ('audio', 7), 
    ('orange', 3), 
    ('frog', 2), 
    ('baz', 6), 
    ('foo', 1), 
    ('apple', 5), 
    ('bar', 1), 
    ('banana', 4), 
    ('toad', 1)
]
def sort(list):
    if list != None:
        for i in range(len(list)):
            min = i
            x = i
            while x + 1 < len(list):
                x += 1
                j = x
                if list[min] > list[j]:
                    min = j
            if min != i:
                list[min], list[i] = list[i], list[min]

    return list





