# Source : https://leetcode.com/problems/get-the-size-of-a-dataframe/
# Author : Md. Shohanur Islam Sobuj
#  Time : February 18, 2024 07:00 AM

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = list(players.shape)
    return df

if __name__=="__main__":
    getDataframeSize()
    