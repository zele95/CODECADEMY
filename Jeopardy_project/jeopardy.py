import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')

## strip additional spaces of the column names
for col in jeopardy.columns:
  jeopardy.rename(columns = {col: col.strip()},inplace = True)

# print(jeopardy.columns)
# print(jeopardy)

## filter question columns for desired keywords
def get_keywords(df,words):
  contains_keywords = lambda x: all(word.lower() in x.lower() for word in words)   
  # contains_keywords = lambda x: all((' ' + word + ' ').lower() in x.lower() for word in lst)   
  # new_df = df.loc[df.Question.apply(contains_keywords)]
  new_df = df[df.Question.apply(contains_keywords) == True]
  return new_df

# test function
filtered_data = get_keywords(jeopardy,['King','England'])
# print(filtered_data.Question)

## add a new column with floats of values
print(jeopardy.Value)
conv_to_float = lambda x: 0 if x == 'None' else float(x.strip('$').replace(',',''))
jeopardy['Value_float'] = jeopardy.Value.apply(conv_to_float)
print(jeopardy.Value_float)

## compute average value of the questions containing a certain word
def get_keyword_average(df,words):
  return get_keywords(df,words).Value_float.mean()

# test function
print(get_keyword_average(jeopardy,['King']))

## count unique values of answers for a certain keyword
def get_nunique_answ(df,words):
  answer = get_keywords(df,words).Answer.value_counts()
  # answer = get_keywords(df,words).groupby('Answer')['Show Number'].count().reset_index(
  # name='Count').sort_values(['Count'], ascending=False)
  return answer

# test function
print(get_nunique_answ(jeopardy,['King']))


## compare keywoard appearance in question in different years

def check_years_question(y1,y2,word):
  # filter data for a wordd
  filtered_data2 = get_keywords(jeopardy,[word])
  # extract the years in correct format
  time_format = lambda x: int(x[:4])
  filtered_data2['Air Year'] = filtered_data2['Air Date'].apply(time_format)
  # select only data from these years 
  selected_years = filtered_data2[(filtered_data2['Air Year'] == y1) | (filtered_data2['Air Year'] == y2)]
  # count years
  print(selected_years['Air Year'].value_counts())

# test function
print(check_years_question(1990,2000,'Computer'))


## check connection between round and category
# count 'Literature' in single and in double jeopardy...
def check_category(df,cat):
  contains = lambda x: cat.lower() in x.lower()  
  # contains_keywords = lambda x: all((' ' + word + ' ').lower() in x.lower() for word in lst)   
  # new_df = df.loc[df.Question.apply(contains_keywords)]
  new_df = jeopardy[jeopardy.Category.apply(contains)]
  return new_df.Round.value_counts()

# test function
print(check_category(jeopardy,'Literature'))


## ask random question  and check if right
def random_question():

  # choose question
  q = np.random.randint(0,len(jeopardy)+1)
  print(jeopardy.Question[q]+'?')

  # enter answer
  a = input('Enter your answer:')
  print(a)
  
  # check if correct
  if a == jeopardy.Answer[q]:
    print('Correct!')
  else:
    print('Sorry, not correct..')

# test function
# random_question()






