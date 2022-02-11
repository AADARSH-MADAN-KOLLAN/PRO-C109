import statistics
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")

score_list = df["reading score"].to_list()
mean = statistics.mean(score_list)
median = statistics.median(score_list)
mode = statistics.mode(score_list)
standard_deviation = statistics.stdev(score_list)
print(f"\nThe mean of the scores is : {mean}\nThe median of the scores is : {median}\nThe mode of the scores is : {mode}\nThe standard deviation of the scores is : {standard_deviation}")

score_1stdev_start, score_1stdev_end = mean-(standard_deviation), mean+(standard_deviation)
score_2stdev_start, score_2stdev_end = mean-(2*standard_deviation), mean+(2*standard_deviation)
score_3stdev_start, score_3stdev_end = mean-(3*standard_deviation), mean+(3*standard_deviation)

data_between_1stdev = [result for result in score_list if result > score_1stdev_start and result < score_1stdev_end]
data_between_2stdev = [result for result in score_list if result > score_2stdev_start and result < score_2stdev_end]
data_between_3stdev = [result for result in score_list if result > score_3stdev_start and result < score_3stdev_end]

print("The percentage of data that lies between the first standard deviation is : {}".format((len(data_between_1stdev)*100.0)/len(score_list)))
print("The percentage of data that lies between the second standard deviation is : {}".format((len(data_between_2stdev)*100.0)/len(score_list)))
print("The percentage of data that lies between the third standard deviation is : {}".format((len(data_between_3stdev)*100.0)/len(score_list)))