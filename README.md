# Intro to Data Science in Python
## University of Michigan, Coursera online course
### 11/2016


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

df.drop("Store 1") 
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