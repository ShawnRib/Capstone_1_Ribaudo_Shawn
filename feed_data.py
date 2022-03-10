import pandas as pd
import sqlalchemy as sq

#check connection
con = sq.create_engine('mysql+pymysql://root:SQL5Data@localhost/TractorTEK')
df_product_code = pd.read_sql('product_codes', con)
print(df_product_code)

#read csv and push date to SQL with panda
df_pd_product = pd.read_csv("csv/product_code_table.csv")
print(df_pd_product)
df_pd_product.to_sql('product_codes',con, if_exists="append", index=False)

df_pd_sale_team = pd.read_csv("csv/sale_team_table_comma.csv")
print(df_pd_sale_team)
df_pd_sale_team.to_sql('employers',con, if_exists="append", index=False)

df_pd_sales_quantities = pd.read_csv("csv/sales_quantities.csv")
print(df_pd_sales_quantities)
df_pd_sales_quantities.to_sql('sales_quantities',con, if_exists="append", index=False)

df_pd_dates = pd.read_csv("csv/date_list.csv")
print(df_pd_dates)
df_pd_dates.to_sql('dates',con, if_exists="append", index=False)
