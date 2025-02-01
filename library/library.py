def append_column(mlist: list[list], amount = 1, right = True, placeHolder = None) -> None:
    if len(mlist) > 0:
        for i in range(amount):
            if right:
                mlist[0].append(placeHolder);
            else:
                mlist[0].insert(0, placeHolder);

def append_row(mlist: list[list], amount = 1, bottom = True, length = None, placeHolder = None) -> None:
    if length is None:
        if (len(mlist) < 1):
            raise IndexError
        length = len(mlist[0])
    emptyList = []
    for i in range(length):
        emptyList.append(placeHolder)

    for i in range(amount):
        if bottom:
            mlist.append(emptyList)
        else:
            mlist.insert(0, emptyList)

def list_of_dimension(size = (1, 1), placeHolder = None) -> list[list]:
    graph: list[list] = []
    append_row(graph, amount=size[1], length=size[0],placeHolder=placeHolder)
    return graph

print(list_of_dimension((4, 4)))