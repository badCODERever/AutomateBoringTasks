mycoll={'fero':'M','buvi':'F','mahi':'M'}
while True:
    print('Enter the name to check')
    name=input()
    if name=='':
        break
    if name in mycoll:
        print('Gender is '+mycoll[name])
    else:
        print('I dont\'t have ur Gender Enter the gender')
        gender=input()
        mycoll[name]=gender
        print('updated')
    
