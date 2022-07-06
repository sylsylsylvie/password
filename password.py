password = '123'
x = 3
while x > 0:
    attempt = input('please enter password:')
    if attempt == password:
        print('login successful!')
        break
    else:
        x = x - 1
        print('密碼錯誤！還有', x, '次機會')

