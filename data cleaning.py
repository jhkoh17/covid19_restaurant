# basic programing practice

# load library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# practice 1
i = 0
while i < 5:
    print('*' * i )
    i = i + 1

# practice 2
score = [ 70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0 # no. of variables
count = 0
for i in score:
    total+=i # "+=" add another values
    count+=1
print(total/count)

# practice 3
# print all sequence of Fibonachi below given value

def fibo(n):
    fibonumber = [0,1]
    if n == 1:
        print(0)
    elif n == 2:
        print(fibonumber)
    else:
        while fibonumber[-1]+fibonumber[-2] <n:
            fibonumber.append(fibonumber[-1]+fibonumber[-2])
        print(fibonumber)

n = 10
fibo(n)

# practice 4
# 1. create a text file with all scores into "sample.txt"
# 2. create a text file with the average of the scores at "result.txt"

score = [ 70, 60, 55, 75, 95, 90, 80, 85, 100]
textfile = open('./sample.txt', 'w') # w: write model
for i in score:
    textfile.write(str(i) + '\n')  # '\n':
textfile.close()

# read data s
newtextfile = open('./sample.txt', 'r')
total =0
number =0
for line in newtextfile:
    total+= int(line)
    number+=1
average = total/number
newtextfile.close()
resulttext = open('./results.txt', 'w')
resulttext.write(str(average))
resulttext.close()

# practice 5
# 1. create random number with n =50
# 2. create plot and histogram with data create in 1
list = np.random.rand(50) # create 50 random number between 0 and 1
data = pd.Series(list)
plt.plot(data)
plt.show()
plt.hist(data)

# practice 6
# 1. select the row where the number of attempts in the examination is less 2 and score greater 15
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan , 9, 20, 14.5, np.nan , 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

exam_data = pd.DataFrame(exam_data)

scorecondition = exam_data['score']>15
attempcondition = exam_data['attempts']<2
select = exam_data[scorecondition & attempcondition] # '&' -> and
select2 = exam_data[scorecondition | attempcondition] # '|' -> or

print(select)
print(select2)

# practice 7 (not working)

# import requests
# from bs4 import BeautifulSoup
# req=requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20180124')
# html=req.text
# soup=BeautifulSoup(html,'html.parser')
# columns=soup.select('div.table-responsive > table > thead > tr > th') # get contents in columns
#
# columnlist=[]
# for column in columns:
#     columnlist.append(column.text)
# df=pd.DataFrame(columns=columnlist)
#
# contents=soup.select('div.table-responsive > table > tbody > tr ') # get names of the contents collected
# dfcontent=[]
# alldfcontents=[]
#
# for content in contents:
#     tds=content.find_all("td")
#     for td in tds:
#         dfcontent.append(td.text)
#     alldfcontents.append(dfcontent)
#     dfcontent=[]
#
# df=pd.DataFrame(columns=columnlist, data=alldfcontents)
