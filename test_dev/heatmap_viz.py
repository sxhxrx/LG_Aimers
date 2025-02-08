## train 데이터셋 원본 시각화 ##
## correlation matrix ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV 파일 리드
df = pd.read_csv('train.csv')
spec_df = pd.read_excel('데이터명세.xlsx')

categorical_columns = spec_df[spec_df["범주형 여부"] == 1]["컬럼명"].tolist()
numerical_columns = spec_df[spec_df["범주형 여부"] == 0]["컬럼명"].tolist()

# 상관관계 계산
correlation_matrix = df.corr()

# 히트맵 그리기
plt.figure(figsize=(10, 8))  # 히트맵 크기 설정
correlation_matrix = df[numerical_columns].corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()