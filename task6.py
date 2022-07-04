#task6
def zero(items, left, right):
    if items[0] == 2016:
        return left
    if items[0] == 2002:
        return right


def two(items, left, middle, right):
    if items[2] == 'C++':
        return left
    if items[2] == 'M4':
        return middle
    if items[2] == 'NGINX':
        return right


def one(items, left, middle, right):
    if items[1] == 'XC':
        return left
    if items[1] == 'PUG':
        return middle
    if items[1] == 'PONY':
        return right


def three(items, left, right):
    if items[3] == 1957:
        return left
    if items[3] == 2004:
        return right    


def main(items):
    return zero(
        items,
        two(
            items,
            one(items, 0, 1, 2),
            one(items, three(items, 3, 4), 5,
                three(items, 6, 7)),
            three(items, 8, one(items, 9, 10, 11))
        ),
        12
    )
