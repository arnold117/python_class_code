def get_num(*args):
    ave = sum(args) / len(args)
    arg2 = [ave]

    for arg in args:
        if arg > ave:
            arg2.append(arg)
    arg2 = tuple(arg2)

    return arg2


if __name__ == '__main__':
    print(get_num(1, 20, 300, 100))