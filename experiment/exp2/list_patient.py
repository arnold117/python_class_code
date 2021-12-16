"""
将7个病人随机分配到3个病房，每个病房最少一个病人
要求：
1、输出每个病房的病人名字。
2、结果以列表形式输出。
3、必须实现多次输出结果不同但能符合上述要求（提示：可以建一个以列表为元素的空列表patients，然后随机往patients列表中放入病人即可实现随机分配）
"""

import random


def assign_patient ():
    room = [[], [], []]
    patient = ["A", "B", "C", "D", "E", "F", "G"]

    for name in patient:
        index = random.randint(0, 2)
        room[index].append(name)

    return room


if __name__ == '__main__':
    flag = True

    while flag:
        room = assign_patient()

        for num in room:
            if not num:
                flag = True
                break
            else:
                flag = False

    print(room)
