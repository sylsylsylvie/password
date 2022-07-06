password = '123'
x = 3
while x > 0:
    x = x - 1
    attempt = input('please enter password:')
    if attempt == password:
        print('login successful!')
        break
    else:
        print('密碼錯誤！')
        if x > 0:
            print('還有', x, '次機會')
        else:
            print('錯誤太多次')