import pandas as pd
import os

os.chdir('~/proj/mlops24/scripts/data-processing')
os.makedirs('../../data/stage1', exist_ok=True)

df = pd.read_csv('../../data/raw/train.csv')
df[['Survived', 'Pclass', 'Sex', 'Age']].to_csv('../../data/stage1/train.csv', index=False)
