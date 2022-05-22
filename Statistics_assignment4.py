import scipy.stats as sts
from scipy.stats import norm
import math
import numpy as np
import pandas as pd

# Problem statement 1
print("# Problem statement 1")
f_list = [60,54,46,41]
m_list = [40,44,53,57]
s = [40,60]
b = [44,54]
m = [53,46]
p = [57,41]
marks = m_list + f_list
print(marks)
sex =  ['Male','Male','Male','Male','Female','Female','Female','Female']
edu = ['High School', 'Bachelors', 'Masters', 'Ph.d.','High School', 'Bachelors', 'Masters', 'Ph.d.']
df_edu = pd.DataFrame({"Sex":sex,"Edu":edu,"Marks":marks})
print(df_edu)
cross_tab = pd.crosstab([df_edu.Sex,df_edu.Marks],df_edu.Edu,margins=True)

df2 = pd.crosstab(df_edu.Sex, df_edu.Edu,df_edu.Marks, aggfunc="sum",margins=True)
df2.columns = ["Bachelors","High School","Masters","Ph.d.","row_totals"]
df2.index = ["Female","Male","col_totals"]

observed = df2.iloc[0:2,0:4]   # Get table without totals for later use
expected =  np.outer(df2["row_totals"][0:2],
                     df2.loc["col_totals"][0:4]) / 395.0
expected = pd.DataFrame(expected)
expected.columns = ["Bachelors","High School","Masters","Ph.d."]
expected.index = ["Female","Male"]
chi_squared_stat = (((observed-expected)**2)/expected).sum().sum()
print(chi_squared_stat)

crit = sts.chi2.ppf(q=0.95,  # Find the critical value for 95% confidence*
                    df=3)  # *

print("Critical value")
print(crit)
p_value = 1 - sts.chi2.cdf(x=chi_squared_stat, df=3)  # Find the p-value
print("P value")
print(p_value)

print(sts.chi2_contingency(observed= observed))

print("The output shows the chi-square statistic = 8, the p-value as 0.045 and the degrees of freedom as 3 followed by the expected counts. The critical value with 3 degree of freedom is 7.815. Since 8.006 > 7.815, therefore we reject the null hypothesis and conclude that the education level depends on gender at a 5% level of significance")


#problem statement 2
print("#Problem statement 2")
Group1 = [51, 45, 33, 45, 67]
Group2 = [23, 43, 23, 43, 45]
Group3 = [56, 76, 74, 87, 56]

# Perform the ANOVA
statistic, pvalue = sts.f_oneway(Group1,Group2,Group3)
print("F Statistic value {} , p-value {}".format(statistic,pvalue))
if pvalue < 0.05:
    print('True')
else:
    print('False')
# Problem statement 3

print("#Problem statement 3")

print(sts.f_oneway([10, 20, 30, 40, 50],[5,10,15, 20, 25]))

Group1 = [10, 20, 30, 40, 50]
Group2 = [5,10,15, 20, 25]

mean_1 = np.mean(Group1)
mean_2 = np.mean(Group2)

grp1_sub_mean1 = []
grp2_sub_mean2 = []
add1 = 0
add2 = 0
for items in Group1:
    add1 += (items - mean_1)**2
for items in Group2:
    add2 += (items - mean_2)**2
var1 = add1/(len(Group1)-1)
var2 = add2/(len(Group2)-1)

F_Test = var1/var2
print("F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25 is : ",F_Test)