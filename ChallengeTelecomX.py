import pandas as pd
import ast
import plotly.express as px

URL = "https://raw.githubusercontent.com/alura-cursos/challenge2-data-science/main/TelecomX_Data.json"
df = pd.read_json(URL)
df.head()
customer_df = pd.json_normalize(df['customer'])
phone_df = pd.json_normalize(df['phone'])
internet_df = pd.json_normalize(df['internet'])
account_df = pd.json_normalize(df['account'])

df_final = pd.concat([df[['customerID', 'Churn']], customer_df, phone_df, internet_df, account_df], axis=1)
df_final['SeniorCitizen'] = df_final['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
df_final.head()

fig = px.histogram(df_final, x='Contract', color='Churn', barmode='group',
                   title='Distribuição de Churn por Tipo de Contrato')
fig.show()

fig2 = px.pie(df_final, names='SeniorCitizen', title='Distribuição de Idosos')
fig2.show()

fig3 = px.box(df_final, x='Churn', y='tenure', color='Churn',
             title='Distribuição de Tenure por Churn')
fig3.show()

fig4 = px.histogram(df_final, x='InternetService', color='Churn', barmode='group',
                   title='Churn por Tipo de Internet')
fig4.show()
