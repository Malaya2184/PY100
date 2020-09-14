import os
import random

for i in range(1,200):
	n= random.randint(60,500)
	if n>60:
		d = str(n) + 'days ago'
		with open('fun.txt', 'a') as file:
			file.write(d+'\n')
		os.system('git add fun.txt')
		os.system('git commit --date="'+d+'" -m "fun to do"')

	os.system('git push -u origin master')