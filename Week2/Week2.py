Week 2 Assignment

Question 1
Which country has won the most gold medals in summer games?
This function should return a single string value.

```
def answer_one():
    return df['Gold'].idxmax()

answer_one()
```

Question 2¶
Which country had the biggest difference between their summer and winter gold medal counts?
This function should return a single string value.
```
def answer_two():
    max_diff=max(df['Gold']-df['Gold.1'])
    answer = df[(df['Gold']-df['Gold.1'])==max_diff].index.tolist()
    return answer[0]

answer_two()
```

Question 3

Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
(Summer Gold−Winter Gold)/Total Gold
 
Only include countries that have won at least 1 gold in both summer and winter.
This function should return a single string value.
```
def answer_three():
    df_nozero = df[(df['Gold']>0) & (df['Gold.1']>0)]
    percentage = max(abs((df_nozero['Gold']-df_nozero['Gold.1'])/df_nozero['Gold.2']))
    return df[((df['Gold']-df['Gold.1'])/df['Gold.2'])==percentage].index.tolist()[0]

answer_three()
```


Question 4¶
Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created.
This function should return a Series named Points of length 146

```
def answer_four():
    df['Points']= (df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2'])
    return df['Points']

answer_four()
```

Question 5
Question 5¶
Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
This function should return a single string value.
```

def answer_five():
    new_df = census_df[census_df['SUMLEV'] == 50]
    return new_df.groupby('STNAME').count()['SUMLEV'].idxmax()

answer_five()
```

