#ex
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
split_it = paragraph.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(10)  
print((most_occur))

#for Match
# syntac
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach


#search
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first

#searching all mathces using findall()
txt = ''' python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language']

# if we don't use flag then
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']


#Replacing a substring
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  

# ex_1 :
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
wordlist = paragraph.split()
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
print(str(list(zip(wordfreq, wordlist))))

#ex_3


import re
  

regex = '^[A-Za-z_][A-Za-z0-9_]*'
      

def check(string): 
  
   
    if(re.search(regex, string)): 
        print("True") 
          
    else: 
        print("False") 
      

if __name__ == '__main__' : 
      
    string = "first_name"
    check(string)
  
    string = "first-name"
    check(string)
  
    string = "1first_name"
    check(string)
    
    string = "firstname"
    check(string)


#ex_4    
original_string = "He said 'Hello' @to me"

new_string = original_string.replace("'", "","," )

print(new_string)
#not working


#Quantifier in regex
txt = 'This regular expression example was made on December 6,  2019.'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019']

txt = 'This regular expression example was made on December 6,  2019.'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019']







