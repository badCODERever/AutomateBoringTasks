mycoll={'fero':'M','mahi':'M','buvi':'F'}
while True:
	print('Enter the name to find the gender or leave blank to exit')
	name=input()
	if name=='':
		break
	elif name in mycoll:
		print('gender is '+mycoll[name]+' for '+name)
	else:
		print('I dont have ur data please enter u r gender')
		gender=input()
		mycoll[name]=gender
		print('updated')
