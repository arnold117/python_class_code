"""
实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输错误时显示剩余错误次数。
"""
if __name__ == '__main__':
    count = 3
    while count > 0:
        count = count - 1
        name = input("请输入用户名:")
        passwd = input("请输入密码:")
        if name == "admin" and passwd == "123":
            print("登陆成功")
            break
        else:
            message = "用户名输入错误，剩余{}次".format(count)
            print(message)
