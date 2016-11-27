# Intro to Data Science in Python
## University of Michigan, Coursera online course
### 11/2016

Summary:
Despite the course name, this is an intermediate-level data science course with Python. Familiarity with Numpy and Pandas libraries is not required, but is highly recommended, as the course does get pretty intense really quickly (i.e. Week 2)

Feedback:

![My feeling while taking this course...](https://imgs.xkcd.com/comics/python.png)

> My feeling while taking this course...

This is an intermediate Data Analysis course with Python. The course is difficult not only because the level of materials taught, but because the structure of the course is made in such a way that familiarity with methods is required before they are even taught in the videos. For examples, I struggled a lot with Week 2's assginment because sort_values() and groupby() were only introduced in Week 3. 


In one word, this is a solid course for someone who has a background with Panda and numpy libraries. There is a big knowledge gap between the videos and the assignments, so it's challenging for beginners. 

## Week 4 Statistical Analysis in Python and Project
Binomial Distribution in numpy for coin flipping

```
np.random.binomial(1,0.5)
```
First term (1) is the number of times you want it to run, and second term (0.5) is the chance we get a zero

```
np.random.binomial(1000, 0.5)/1000
```
Flip coins 1000 times, and divide the result by 1000

Run 1000 simulations of flipping coins 20 times and getting a number >= 15. 

```
x = np.random.binomial(20, .5, 10000)
print((x>=15).mean())
```
Output:
```
0.0219
```

Get the number of events given no. of simulation. 
"How many tornados will take place based on 100,000 simulations, given that the chance of a tornado is 0.01%?"

```
chance_of_tornado = 0.01/100
np.random.binomial(100000,chance of tornado)
```
Output:
```
8
```

"Assume the chance of tornado is 1%. How many tornados will take place (what is the chance of tornados taking place) two days in a row based on 1000000 simulations?"

```
chance_of_tornado = 0.01

tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
    
two_days_in_a_row = 0
for j in range(1,len(tornado_events)-1):
    if tornado_events[j]==1 and tornado_events[j-1]==1:
        two_days_in_a_row+=1

print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000/365))
```
Output:
```
103 tornadoes back to back in 2739.72602739726 years
```
tornado_events[j]== 1 means the day when tornado took place.

#### Standard deviation

Draw 1000 samples of a normal distriubtion, with expected value of 0.75 and a standard deviation of 1. Result is ~ 68% of area.
```
distribution = np.random.normal(0.75,size=1000)

np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))
```
The above code is equivalent to the np.std() function:
```
np.std(distribution)
```

#### Kirtosis (shape of tails) with stats module

Positive value = more chubby than a normal distribution
Negative value = more flat than a normal distribution

```
import scipy.stats as stats
stats.kurtosis(distribution)

```
Output:
```
-0.21162400583818153
```

#### Skew with stats module
If skew = 0.5, then there's no skew (i.e. the distribution is symmetric)

```
stats.skew(distribution)
```
Output:
```
0.051147428570855365
```


#### Chi squared distribution (left-skewed)
As the degree of freedom increases, the plot moves from left to center

Degree of freedom = 2:
```
chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)
```
Output:
```
1.9589902136938178
```

Degree of freemdom = 5:
```
chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df5)
```
Output:
```
1.3010399138921354
```

---

## Week 3 Advanced Python Pandas

![Finished Week 3's assignment](http://cdn.someecards.com/someecards/usercards/MjAxMi1mNWM4MDQ3MTJkODYzMzhi.png)

> Finally finished Week 3's assignment.

11/27/2016 Update
Finally finished this week's assignment! The first one took a long time. I had to relearn regular expression because of it. Learned a lot about dataframes through the practices, so I'm happy about the progress eventually, but Jesus,that was a lot of work...

Merging dataframes based on the same index. "NaN" is assigned when there's a missing value.

#### iloc() and loc()
iloc()for query based on location
loc() for query based on label

#### Outer vs inner join

Outer Join
```
pd.merge(df1,df2,how='outer',left_index=True,right_index=True)
```
Inner Join
```
pd.merge(df1,df2,how='inner,left_index=True,right_index=True)
```
Left Join: keep all information from df1
```
pd.merge(df1,df2,how='left',left_index=True,right_index=True)
```
Right Join: keep all information from df2
```
pd.merge(df1,df2,how='right',left_index=True,right_index=True)
```
Join by Column names
```
pd.merge(df1,df2,how='left',left_on='Name',right_on='Name')
```

Chain indexing - not recommended
```
df.loc['Washtenaw']['Total Population']
```

Method chaining 
```
(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))
```
Drop rows where 'Quantity' is 0, and rename the column 'Weight' to 'Weight(oz.)'
```
df = df[df.Quantity !=0].rename({'Weight':'Weight(oz.)'})
```
Alternatively:
```
print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))
```

#### Apply() function which applies a function to all rows in a dataframe

To apply to all rows, use axis= 1

```
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

df.apply(min_max, axis=1)
```
Adding the applied function to the existing dataframe (instead of creating a new one)
```
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row
df.apply(min_max, axis=1)
```
Use apply() with lambda function:
create a function with the max of each row
```
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)
```

#### Groupby()
you can use a function to be the criteria for group_by()
```
df = df.set_index('STNAME')

def fun(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

```
Calculate the average/sum of a certain group with groupby() and agg()
```
df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
```
```
print(df.groupby('Category').agg('sum'))
```

#### Use apply() with groupby()
```
def totalweight(df, w, q):
        return sum(df[w] * df[q])
        
print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))
```

#### Scales
Use astype() to change the type of scales from one to another

create a list and use astype() to indicate the order with ordered = True. This enables > or < to be used on strings. 

```
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)

grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
grades.head()
```
output is:
```
excellent    A+
excellent     A
excellent    A-
good         B+
good          B
Name: Grades, dtype: category
Categories (11, object): [D < D+ < C- < C ... B+ < A- < A < A+]

```
Use > or < functions on types, output:
```
excellent     True
excellent     True
excellent     True
good          True
good          True
good          True
ok            True
ok           False
ok           False
poor         False
poor         False
Name: Grades, dtype: bool
```

Change this series to categorical with ordering Low < Medium < High

```
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)
```

Use get_dummies() to convert boolean values into 0s and 1s

#### cut(): to cut data into bins (i.e. to divide them equally into 10 buckets)

```
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
pd.cut(df['avg'],10)
```
Cut a series into 3 equal-sized bins
```
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])


pd.cut(s, 3)

# You can also add labels for the sizes [Small < Medium < Large].
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])
```

#### Use pivot_table() to create Pivot Tables 

```
df = pd.read_csv('cars.csv')
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
```

Create a pivot table that shows mean price and mean ratings for every "Manufacturer"/"Bike Type" combination
```
print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))

import numpy as np
print(Bikes.pivot_table(values ='Price',index = 'Manufacturer',columns = 'Bike Type',aggfunc=np.average))
```

#### Date Functionality in Panda
1. Timestamp
2. DatetimeIndex (the index of 1)
3. Period
4. PeriodIndex (the index of 3)

1. Timestamp, exchangeable to Python's datetime
⋅⋅⋅```
⋅⋅⋅pd.Timestamp('9/1/2016 10:05AM')
⋅⋅⋅```

2. Period
```
pd.Period('1/2016')
```

3. DatetimeIndex and PeriodIndex
DatetimeIndex
```
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])

type(t1.index)

```
Output:
```
pandas.tseries.index.DatetimeIndex
```
PeriodIndex
```
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
type(t2.index)
```
Output:
```
pandas.tseries.period.PeriodIndex
```

Coverts datetimes to the same format with to_datetime()

```
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
ts3.index = pd.to_datetime(ts3.index)
```

use dayfirst = True to change the datetime into European format
```
pd.to_datetime('4.7.12', dayfirst=True)
```
#### Timedelta: show difference in times

```
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')
```
Output:
```
Timedelta('2 days 00:00:00')
```

Calculate datetime with timedelta
```
pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')
```
Output:
```
Timestamp('2016-09-14 11:10:00')
```

#### Date_range()
Create a range of dates for bi-weekly on Sundays, starting with a specific date

```
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
```

#### weekday_name(): check what day of the week it is
```
df.index.weekday_name
```

#### diff(): find difference between each day's value
```
df.diff()
```

#### resample(): frequency conversion. example: find mean count for each month, will show the data as of month end. 'M' stands for month
```
df.resample('M').mean()
```

Find values from a specific year, month or a range of dates

```
df['2017']
df['2016-12']
df['2016-12':]
<!-- from 12/2016 onwards -->
```
#### asfreq(): change frequency from bi-weekly to weekly, and fill NaN value with last week's data point
```
df.asfreq('W', method='ffill')
```
#### matplotlib: visualising a timeseries

```
import matplotlib.pyplot as plt
%matplotlib inline

df.plot()
```
---
## Week 2 Basic Data Processing with Pandas

Dataframe

```
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()
```

df.T.loc --> T transforms data

iloc vs loc: iloc searches by index, loc searches by value

Avoid chaining as it generally create a copy of the data, instead of simply viewing it.

Deleting data with df.drop(). It creates a copy of the dataframe with the given rows removed.

```
df.drop("Store 1") 
```

Deleting data with del() function

```
del copy_df['Name']
```

apply 20% discount to cost

```
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])


df['Cost'] *= 0.8
print(df)
```

Panda's read_csv() function, making first column the index

```
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
```

Change column names with rename() method

```
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()
```

Boolean masking: applying a boolean (True or False) filter/mask to a dataframe/array with where() function

```
only_gold = df.where(df['Gold']>0)
only_gold.head()
```

Drop lines when there is no data with na() function

```
only_gold = only_gold.dropna()
```

Chaining boolean maskes

```
<!-- either  -->
len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])
<!-- and -->
df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]

```

Return all of names of people who spend more than $3.00
```
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df['Name'][df['Cost']>3]
```

Set_index() function

Reindex the purchase records Dataframe to be index hierarchically, first by store, then by person. Name these indexes "Location" and "Name". Then add a new entry to it with the value of:

Name: "Kevyn", Item Purchased: "Kitty Food", Cost: 3.00 Location:"Store 2".

```
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])


df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
```
---


## Week 1

####List Indexing and Slicing

Example 1

```
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

titleName = []
def split_title_and_name():
  for person in people:
    last = person.split(" ")[-1]
    title = person.split(" ")[0]
    titleName.append(title + " "+last)
  print(titleName)

split_title_and_name()
```


Example 2

```
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split(" ")[0] + " " + person.split(" ")[-1]

list(map(split_title_and_name,people))
```

Example 3 (official answer)

```
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))
```


Lambda functions (for writing quick one-liner functions)

```
my_function = lambda a,b: a+b
my_function(1,2)
```

list comprehension (list all even numbers in range 0 - 1000)

```
my_list = [number for number in range(0,1000) if number % 2==0]
```



```
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [j*i for i in range(10) for j in range(10)]
```

```
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids
```