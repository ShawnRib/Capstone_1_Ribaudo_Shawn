import os
from flask import Flask
from forms import  AddEmployersForm , AddProductForm , AddSalesQuantitiesForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import pandas as pd
import sqlalchemy as sq


app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
#OLD SQLite DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#NEW SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:SQL5Data@localhost/tractortek'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


############################################

        # SQL Model

##########################################
class Employers(db.Model):

    __tablename__ = 'employers'
    #id = db.Column(db.Integer,primary_key = True)
    emp_id = db.Column(db.Text, primary_key= True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    region =db.Column(db.Text)
    pay_grade = db.Column(db.Text)

    def __init__(self,emp_id, first_name, last_name, region, pay_grade):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.region = region
        self.pay_grade = pay_grade

    def __repr__(self):
        return f"Employer id: {self.emp_id}"




class Product_Codes(db.Model):

    __tablename__ = 'product_codes'
    #id = db.Column(db.Integer,primary_key = True)
    prod_code = db.Column(db.Text, primary_key = True)
    prod_name =db.Column(db.Text)
    URL = db.Column(db.Text)
    manufacturer = db.Column(db.Text)
    ext_service_plan = db.Column(db.Text)
    warranty_price = db.Column(db.Integer)

    def __init__(self,prod_code,prod_name, URL, manufacturer, ext_service_plan, warranty_price):
        self.prod_code = prod_code
        self.prod_name = prod_name
        self.URL = URL
        self.manufacturer = manufacturer
        self.ext_service_plan = ext_service_plan
        self.warranty_price = warranty_price

    def __repr__(self):
        return f"Product code: {self.prod_code}"

class Sale_Quantities(db.Model):

    __tablename__ = 'sales_quantities'
    #id = db.Column(db.Integer,primary_key = True)
    id = db.Column(db.Integer, primary_key = True)
    item_code =db.Column(db.Text)
    emp_id = db.Column(db.Text)
    years = db.Column(db.Integer)
    w0 = db.Column(db.Integer)
    w1 = db.Column(db.Integer)
    w2 = db.Column(db.Integer)
    w3 = db.Column(db.Integer)
    w4 = db.Column(db.Integer)
    w5 = db.Column(db.Integer)
    w6 = db.Column(db.Integer)
    w7 = db.Column(db.Integer)
    w8 = db.Column(db.Integer)
    w9 = db.Column(db.Integer)
    w10 = db.Column(db.Integer)
    w11 = db.Column(db.Integer)
    w12 = db.Column(db.Integer)
    w13 = db.Column(db.Integer)
    w14 = db.Column(db.Integer)
    w15 = db.Column(db.Integer)
    w16 = db.Column(db.Integer)
    w17 = db.Column(db.Integer)
    w18 = db.Column(db.Integer)
    w19 = db.Column(db.Integer)
    w20 = db.Column(db.Integer)
    w21 = db.Column(db.Integer)
    w22 = db.Column(db.Integer)
    w23 = db.Column(db.Integer)
    w24 = db.Column(db.Integer)
    w25 = db.Column(db.Integer)
    w26 = db.Column(db.Integer)
    w27 = db.Column(db.Integer)
    w28 = db.Column(db.Integer)
    w29 = db.Column(db.Integer)
    w30 = db.Column(db.Integer)
    w31 = db.Column(db.Integer)
    w32 = db.Column(db.Integer)
    w33 = db.Column(db.Integer)
    w34 = db.Column(db.Integer)
    w35 = db.Column(db.Integer)
    w36 = db.Column(db.Integer)
    w37 = db.Column(db.Integer)
    w38 = db.Column(db.Integer)
    w39 = db.Column(db.Integer)
    w40 = db.Column(db.Integer)
    w41 = db.Column(db.Integer)
    w42 = db.Column(db.Integer)
    w43 = db.Column(db.Integer)
    w44 = db.Column(db.Integer)
    w45 = db.Column(db.Integer)
    w46 = db.Column(db.Integer)
    w47 = db.Column(db.Integer)
    w48 = db.Column(db.Integer)
    w49 = db.Column(db.Integer)
    w50 = db.Column(db.Integer)
    w51 = db.Column(db.Integer)

    def __init__(self,item_code, emp_id, years, w0, w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,w27,w28,w29,w30,w31,w32,w33,w34,w35,w36,w37,w38,w39,w40,w41,w42,w43,w44,w45,w46,w47,w48,w49,w50,w51):
        self.item_code = item_code
        self.emp_id = emp_id
        self.years = years
        self.w0 = w0
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
        self.w5 = w5
        self.w6 = w6
        self.w7 = w7
        self.w8 = w8
        self.w9 = w9
        self.w10 = w10
        self.w11 = w11
        self.w12 = w12
        self.w13 = w13
        self.w14 = w14
        self.w15 = w15
        self.w16 = w16
        self.w17 = w17
        self.w18 = w18
        self.w19 = w19
        self.w20 = w20
        self.w21 = w21
        self.w22 = w22
        self.w23 = w23
        self.w24 = w24
        self.w25 = w25
        self.w26 = w26
        self.w27 = w27
        self.w28 = w28
        self.w29 = w29
        self.w30 = w30
        self.w31 = w31
        self.w32 = w32
        self.w33 = w33
        self.w34 = w34
        self.w35 = w35
        self.w36 = w36
        self.w37 = w37
        self.w38 = w38
        self.w39 = w39
        self.w40 = w40
        self.w41 = w41
        self.w42 = w42
        self.w43 = w43
        self.w44 = w44
        self.w45 = w45
        self.w46 = w46
        self.w47 = w47
        self.w48 = w48
        self.w49 = w49
        self.w50 = w50
        self.w51 = w51

    #def __repr__(self):
     #   return f"Quantities year: {self.years}"


############################################

        # VIEWS and FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_employers', methods=['GET', 'POST'])
def add_employers():

    form = AddEmployersForm()

    if form.validate_on_submit():
        emp_id = form.emp_id.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        region = form.region.data
        pay_grade = form.pay_grade.data
        try:
            # Add new employer to database
            new_employer = Employers(emp_id,first_name, last_name, region, pay_grade)
            print(new_employer)
            db.session.add(new_employer)
            db.session.commit()
            return redirect(url_for('employers_list'))
        except:
            return redirect(url_for('error_detail'))

    return render_template('add_employers.html',form=form)


@app.route('/add_products', methods=['GET', 'POST'])
def add_products():

    form = AddProductForm()

    if form.validate_on_submit():
        prod_code = form.prod_code.data
        prod_name = form.prod_name.data
        url = form.url.data
        manufacturer = form.manufacturer.data
        ext_service_plan = form.ext_service_plan.data
        warranty_price = form.warranty_price.data
        # Add new product to database
        try:
            new_product = Product_Codes(prod_code,prod_name, url, manufacturer, ext_service_plan, warranty_price)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('products_list'))
        except:
            return redirect(url_for('error_detail'))

    return render_template('add_products.html',form=form)

@app.route('/add_sales_quantities', methods=['GET', 'POST'])
def add_sales_quantities():

    form = AddSalesQuantitiesForm()

    if form.validate_on_submit():
        item_code = form.item_code.data
        emp_id = form.emp_id.data
        years = form.years.data
        w0 = form.w0.data
        w1 = form.w1.data
        w2 = form.w2.data
        w3 = form.w3.data
        w4 = form.w4.data
        w5 = form.w5.data
        w6 = form.w6.data
        w7 = form.w7.data
        w8 = form.w8.data
        w9 = form.w9.data
        w10 = form.w10.data
        w11 = form.w11.data
        w12 = form.w12.data
        w13 = form.w13.data
        w14 = form.w14.data
        w15 = form.w15.data
        w16 = form.w16.data
        w17 = form.w17.data
        w18 = form.w18.data
        w19 = form.w19.data
        w20 = form.w20.data
        w21 = form.w21.data
        w22 = form.w22.data
        w23 = form.w23.data
        w24 = form.w24.data
        w25 = form.w25.data
        w26 = form.w26.data
        w27 = form.w27.data
        w28 = form.w28.data
        w29 = form.w29.data
        w30 = form.w30.data
        w31 = form.w31.data
        w32 = form.w32.data
        w33 = form.w33.data
        w34 = form.w34.data
        w35 = form.w35.data
        w36 = form.w36.data
        w37 = form.w37.data
        w38 = form.w38.data
        w39 = form.w39.data
        w40 = form.w40.data
        w41 = form.w41.data
        w42 = form.w42.data
        w43 = form.w43.data
        w44 = form.w44.data
        w45 = form.w45.data
        w46 = form.w46.data
        w47 = form.w47.data
        w48 = form.w48.data
        w49 = form.w49.data
        w50 = form.w50.data
        w51 = form.w51.data
        # Add new product to database
        try:
            new_sales = Sale_Quantities(item_code, emp_id, years, w0, w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,w27,w28,w29,w30,w31,w32,w33,w34,w35,w36,w37,w38,w39,w40,w41,w42,w43,w44,w45,w46,w47,w48,w49,w50,w51)
            print(new_sales)
            db.session.add(new_sales)
            db.session.commit()
            return redirect(url_for('sales_list'))
        except:
            return redirect(url_for('error_detail'))

    return render_template('add_sales_quantities.html',form=form)


@app.route('/sales_list')
def sales_list():
    #connect the database and pull sales from the sales_quantities table
    con = sq.create_engine('mysql+pymysql://root:SQL5Data@localhost/TractorTEK')
    df_sales = pd.read_sql('sales_quantities', con)
    print(df_sales)
    df_size = len(df_sales)
    return render_template('sales_list.html', df_sales=df_sales, df_size=df_size)


@app.route('/employers_list')
def employers_list():
    #connect the database and pull sales from the sales_quantities table
    con = sq.create_engine('mysql+pymysql://root:SQL5Data@localhost/TractorTEK')
    df_employers= pd.read_sql('employers', con)
    print(df_employers)
    df_size = len(df_employers)
    return render_template('employers_list.html', df_employers=df_employers, df_size=df_size)

@app.route('/products_list')
def products_list():
    #connect the database and pull sales from the sales_quantities table
    con = sq.create_engine('mysql+pymysql://root:SQL5Data@localhost/TractorTEK')
    df_product = pd.read_sql('product_codes', con)
    print(df_product)
    df_size = len(df_product)
    return render_template('products_list.html', df_product=df_product, df_size=df_size)

#if the database got an error for various of reason, it will go to an error_detail page.
@app.route('/error_detail', methods=['GET', 'POST'])
def error_detail():
    return render_template('error_detail.html')

#404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

############################################

        # Run APP (MUST BE AT THE END OF THE CODE)

##########################################
if __name__ == '__main__':
    app.run(debug=True)