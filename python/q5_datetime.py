# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

# coding: utf-8

# In[2]:

# Computing Days
import datetime as dt

str_date_start = '01-02-2013'
str_date_stop = '07-28-2015'
str_format = '%m-%d-%Y'

date_start= dt.datetime.strptime(str_date_start, str_format)
date_stop = dt.datetime.strptime(str_date_stop, str_format)

number_of_days = date_stop - date_start

print (number_of_days.days)

# Answer: 937

# In[3]:

str_date_start2 = '12312013'  
str_date_stop2 = '05282015'  
str_format2 = '%m%d%Y'

date_start= dt.datetime.strptime(str_date_start2, str_format2)
date_stop = dt.datetime.strptime(str_date_stop2, str_format2)

number_of_days = date_stop - date_start

print (number_of_days.days)

# Answer: 513

# In[4]:

str_date_start3 = '15-Jan-1994'
str_date_stop3 =  '14-Jul-2015'    
str_format3 = '%d-%b-%Y'

date_start= dt.datetime.strptime(str_date_start3, str_format3)
date_stop = dt.datetime.strptime(str_date_stop3, str_format3)

number_of_days = date_stop - date_start

print (number_of_days.days)

# Answer: 7850
