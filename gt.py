import seaborn as sns
import matplotlib.pyplot as plt
 
# read a titanic.csv file
# from seaborn library
df = sns.load_dataset('titanic')
 
# class v / s fare barplot 
sns.barplot(x = 'class', y = 'fare', data = df)
 
# Show the plot
plt.show()