# Intro to Data Science in Python
## University of Michigan, Coursera online course
### 11/2016

## Week 3 Advanced Python Pandas
Merging dataframes based on the same index. "NaN" is assigned when there's a missing value.
Outer vs inner join

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