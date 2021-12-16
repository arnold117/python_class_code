"""
编写一个接受句子并计算字母(XX.isalpha()函数)和数字（XX.isdigit（））的程序。假设为程序提供了以下输入：
Hello world! 123456
然后，输出应该是：
字母10
数字6
"""

if __name__ == '__main__':
    str_input = input("请输入句子：")
    count_digit = 0
    count_alpha = 0

    for i in str_input:
        if i.isdigit():
            count_digit += 1
        if i.isalpha():
            count_alpha += 1

    print("Digit:", count_digit)
    print("Alpha:", count_alpha)
