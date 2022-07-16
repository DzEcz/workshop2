year = int(input('Enter a 4-digit year : '))
year_len = len(str(year))

if year_len != 4:
    print('Please enter 4-digit year!')
else:
    if year % 100 == 0 and year % 400 == 0:
        print(True)
    elif year % 100 == 0 and year % 400 != 0:
        print(False)
    elif year % 4 == 0:
        print(True)
    else:
        print(False)