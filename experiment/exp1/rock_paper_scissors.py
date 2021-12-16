"""
实现和电脑猜拳（石头剪刀布）的小游戏。
要求：
（1）含有如下提示信息：
    请输入您的猜拳：0、石头，1、剪刀，2、布:
（2）在玩家输入猜拳数后与计算机随机生成的猜拳（提示：import random）进行比较，给出结果。
（3）对于输入不正常的结果，尽可能考虑全面，使得程序能够流畅运行(比如输入错误)。
"""
import random


def judgement(plat):  # 判断游戏结果
    if plat.count(plat[0]) > 1:  # 平局
        return 2
    return plat.index(max(plat)) if sum(plat) in (1, 3) else plat.index(min(plat))


def play():
    base = ('剪刀', '石头', '布')
    print('轮到你出了！\n')
    for i, n in enumerate(base):  # 打印选项
        print(f'[{i}] {n}')
    player = int(input('输入序号选择：'))  # 玩家出
    computer = random.randint(0, 2)  # 电脑出
    print(f'\n- 你出了[{base[player]}]！\n- 电脑出了[{base[computer]}]！')
    winner = judgement([player, computer])
    print('\n本局是' + ('你赢了！', '电脑赢了！', '平局~')[winner])  # 结果


if __name__ == '__main__':
    play()  # 开始玩
