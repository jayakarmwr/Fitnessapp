def pwd():
    print("\nRules of the password:\ni) Minimum length is 6 characters and maximum length is 15 characters.\nii) It should have a minimum of one Capital Letter, One Small Letter, One digit and one special symbol\niii) Special symbols allowed are only (*, @, #)")
    s = input('Enter a password: ')
    flag = 0
    while True:
        if len(s) < 6 or len(s) > 15:
            flag = -1
            break
        elif not re.search('[a-z]', s):
            flag = -1
            break
        elif not re.search('[A-Z]', s):
            flag = -1
            break
        elif not re.search('[0-9]', s):
            flag = -1
            break
        elif not re.search('[*@#]', s):
            flag = -1
            break
        else:
            flag = 0
            break

    if flag == -1:
        print('Not a valid password')
        print('Please try a different password')
        return pwd()
    elif flag == 0:
        return s
