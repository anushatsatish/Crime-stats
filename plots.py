from data import *
import matplotlib.pyplot as plt 
 
s = df[['primary_type']] #  get a series from data frame
crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
data=crime_count.iloc[-10:-5] # retrieving select rows by loc method

print(data[::-1])

data.plot(kind='barh')
  
plt.subplots_adjust(left=0.33, right=0.89) 

# Show graphic
plt.show()
 

 