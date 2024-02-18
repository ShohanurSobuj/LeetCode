# Source : https://leetcode.com/problems/create-a-dataframe-from-list
# Author : Md. Shohanur Islam Sobuj
#  Time : February 18, 2024 06:53 AM

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    df = pd.DataFrame(student_data, columns=['student_id', 'age'])

    return df

if __name__=="__main__":
    createDataframe()