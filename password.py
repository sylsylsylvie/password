password = '123'
x = 2
while True:
    attempt = input('please enter password:')
    if attempt == password:
        print('login successful!')
        break
    else:
        print('密碼錯誤！還有', x, '次機會')
        x = x - 1
        if x == -1:
            print('錯誤太多次')
            break
     