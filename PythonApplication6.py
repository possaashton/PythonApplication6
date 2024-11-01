
# Python program to convert .tsv file to .csv file
# importing pandas library
import pandas as pd
#import numpy as np

DIR = r"D:\DublinBusinessSchool\Semister_3_Dissertation\Applied_Research_Project\DataSet"
DATASET = pd.read_csv(DIR + r"\raw_test.csv")

print(DATASET.head)
#testing
