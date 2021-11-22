import pandas as pd

holiday = pd.read_csv("Holidays.csv")
   #1.How many rows and columns are there in your file?
number_rows = len(holiday)
#print(len(holiday))
#print()
number_columns = len(holiday.columns)
#print(number_columns)
  # 2.Print row 3-8 ( using iloc loc )
#print(holiday.iloc[3:9])
 # 3. Find the mean number of all inclusive hotels across all destinations.
mean = holiday["number_all_inclusive_hotels"].mean()
#print(mean)

# 4.Find the lowest scoring destination.
lowest_score = holiday["Feedback_score"].min()
index_lowest = holiday["Feedback_score"].idxmin()

#print(holiday.iloc[(index_lowest)])

#5.Find the highest scoring destination.
highest_score = holiday["Feedback_score"].max()
index_highest = holiday["Feedback_score"].idxmax()

#print(holiday.iloc[(index_highest)])

# Find all the destinations where there are more than 9 all inclusive hotels.
more_than_nine_h = holiday[(holiday.number_all_inclusive_hotels > 9)]
#print(more_than_nine_h)

#Filter the data by score above 8
score_above_height = holiday[(holiday.Feedback_score > 8)]
#print(score_above_height)

#Filter the data score below 2 ( I need to know if these destinations should be removed or there is a problem)
score_below_two = holiday[(holiday.Feedback_score <2 )]
if score_below_two.empty :
  print("There is no destinations whose score is below 2")
else :
        print(score_below_two)

#Extension
#1.Is there a correlation between number of all inclusive hotels and score?

#2.Create a data visualisation diagram to show destination and highest scores?
from sklearn.datasets import load_iris
