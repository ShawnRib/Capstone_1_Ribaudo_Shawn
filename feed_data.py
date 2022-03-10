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

'''
# read only
#df_puppies = pd.read_sql('puppies', con, columns=['name', 'owner'])
df_puppies = pd.read_sql('puppies', con)
print(df_puppies)


df_fur_group = df_puppies.groupby('color_fur')
print('---Group by color---')
print(df_fur_group.count())
total_row_puppies = df_puppies.shape[0]
total_row_owner = df_owner.shape[0]
print('Total count for puppies table: ' + str(total_row_puppies))
print('Total count for owners table: ' + str(total_row_owner))
print('Total number of column in puppies table: ' + str(df_puppies.shape[1]))
print('Total number of column in owners table: ' + str(df_owner.shape[1]))

# select name FROM puppies where name='asdf';

df = pd.read_sql('select name FROM puppies where name="Fire"', con)
print(df)
'''
'''
# write to sql for puppies
puppies_list=pd.DataFrame({
        "name": ['Fish', "Fire", "Wind", "Earth", "Water", "Neo", "Rock", "Joker", "Ginger", "Ziggy"],
        "color_fur": ['brown','white','black','brown','white','black','white','white','white','black'],
        "owner": [1,2,3,4,5,6,7,8,9,10]})

#write to sql for owners
oweners_list=pd.DataFrame({
        "name": ['Shawn', "Tyler", "Catherine", "Robin", "David", "Andrew", "Sophia", "Carl", "Caleb", "Todd"],
        "puppy_id": [1,2,3,4,5,6,7,8,9,10]})

puppies_list.to_sql('puppies',con, if_exists="append", index=False)
oweners_list.to_sql('owners',con, if_exists="append", index=False)
'''