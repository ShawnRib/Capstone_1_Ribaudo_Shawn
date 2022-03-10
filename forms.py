from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import InputRequired, ValidationError, DataRequired, Length, number_range

#note datarequired give a warning message if the input is empty. Also, none of the number can go below negative.

#add employers form
class AddEmployersForm(FlaskForm):

    emp_id = StringField('What are the new employer id?', [DataRequired('Employer id is missing')])
    first_name = StringField('First name of the employer', [DataRequired('First name is missing')])
    last_name = StringField('Last name of the employer', [DataRequired('Last name is missing')])
    region = SelectField(u'Region', choices=[('NW', 'North West'), ('SW', 'South West')])
    pay_grade = StringField('Pay Grade', [DataRequired('Pay Grade is missing')])
    submit = SubmitField('Add a employer')

#add products form
class AddProductForm(FlaskForm):

    prod_code= StringField('What is the code of this new product?', [DataRequired('The product code is missing')])
    prod_name = StringField('Name of the product', [DataRequired('The product name is missing')])
    url = StringField('Paste the URL link about the product', [DataRequired('Please add a link in url')])
    manufacturer = StringField('What are the manufacturer of this product?', [DataRequired('The manufactureris missing')])
    ext_service_plan = StringField('Extended Service Plan code', [DataRequired('Please enter extended service plan code')])
    warranty_price = IntegerField('What are the warranty price', [DataRequired('Warranty Price is missing'), number_range(min=0, message='Warranty price can not be negative.')])
    submit = SubmitField('Add a product')

#add sales form
class AddSalesQuantitiesForm(FlaskForm):
    item_code = StringField('Product Code', [DataRequired('Product code is missing')])
    emp_id = StringField('Who made those sales? Type thier emp_id', [DataRequired('Please enter the employment id.')])
    years = IntegerField('Which year?', [InputRequired('Year is missing'), number_range(min=2019, message='Year can not be below 2019')])

    #week 0 - 51
    #note: Default is 0.
    w0 = IntegerField('Week 0', [InputRequired('Week 0 can not be blank'),
                                 number_range(min=0, message='Week 0 can not have a value below 0')], default=0)
    w1 = IntegerField('Week 1', [InputRequired('Week 1 can not be blank'),
                                 number_range(min=0, message='Week 1 can not have a value below 0')], default=0)
    w2 = IntegerField('Week 2', [InputRequired('Week 2 can not be blank'),
                                 number_range(min=0, message='Week 2 can not have a value below 0')], default=0)
    w3 = IntegerField('Week 3', [InputRequired('Week 3 can not be blank'),
                                 number_range(min=0, message='Week 3 can not have a value below 0')], default=0)
    w4 = IntegerField('Week 4', [InputRequired('Week 4 can not be blank'),
                                 number_range(min=0, message='Week 4 can not have a value below 0')], default=0)
    w5 = IntegerField('Week 5', [InputRequired('Week 5 can not be blank'),
                                 number_range(min=0, message='Week 5 can not have a value below 0')], default=0)
    w6 = IntegerField('Week 6', [InputRequired('Week 6 can not be blank'),
                                 number_range(min=0, message='Week 6 can not have a value below 0')], default=0)
    w7 = IntegerField('Week 7', [InputRequired('Week 7 can not be blank'),
                                 number_range(min=0, message='Week 7 can not have a value below 0')], default=0)
    w8 = IntegerField('Week 8', [InputRequired('Week 8 can not be blank'),
                                 number_range(min=0, message='Week 8 can not have a value below 0')], default=0)
    w9 = IntegerField('Week 9', [InputRequired('Week 9 can not be blank'),
                                 number_range(min=0, message='Week 9 can not have a value below 0')], default=0)
    w10 = IntegerField('Week 10', [InputRequired('Week 10 can not be blank'),
                                   number_range(min=0, message='Week 10 can not have a value below 0')], default=0)
    w11 = IntegerField('Week 11', [InputRequired('Week 11 can not be blank'),
                                   number_range(min=0, message='Week 11 can not have a value below 0')], default=0)
    w12 = IntegerField('Week 12', [InputRequired('Week 12 can not be blank'),
                                   number_range(min=0, message='Week 12 can not have a value below 0')], default=0)
    w13 = IntegerField('Week 13', [InputRequired('Week 13 can not be blank'),
                                   number_range(min=0, message='Week 13 can not have a value below 0')], default=0)
    w14 = IntegerField('Week 14', [InputRequired('Week 14 can not be blank'),
                                   number_range(min=0, message='Week 14 can not have a value below 0')], default=0)
    w15 = IntegerField('Week 15', [InputRequired('Week 15 can not be blank'),
                                   number_range(min=0, message='Week 15 can not have a value below 0')], default=0)
    w16 = IntegerField('Week 16', [InputRequired('Week 16 can not be blank'),
                                   number_range(min=0, message='Week 16 can not have a value below 0')], default=0)
    w17 = IntegerField('Week 17', [InputRequired('Week 17 can not be blank'),
                                   number_range(min=0, message='Week 17 can not have a value below 0')], default=0)
    w18 = IntegerField('Week 18', [InputRequired('Week 18 can not be blank'),
                                   number_range(min=0, message='Week 18 can not have a value below 0')], default=0)
    w19 = IntegerField('Week 19', [InputRequired('Week 19 can not be blank'),
                                   number_range(min=0, message='Week 19 can not have a value below 0')], default=0)
    w20 = IntegerField('Week 20', [InputRequired('Week 20 can not be blank'),
                                   number_range(min=0, message='Week 20 can not have a value below 0')], default=0)
    w21 = IntegerField('Week 21', [InputRequired('Week 21 can not be blank'),
                                   number_range(min=0, message='Week 21 can not have a value below 0')], default=0)
    w22 = IntegerField('Week 22', [InputRequired('Week 22 can not be blank'),
                                   number_range(min=0, message='Week 22 can not have a value below 0')], default=0)
    w23 = IntegerField('Week 23', [InputRequired('Week 23 can not be blank'),
                                   number_range(min=0, message='Week 23 can not have a value below 0')], default=0)
    w24 = IntegerField('Week 24', [InputRequired('Week 24 can not be blank'),
                                   number_range(min=0, message='Week 24 can not have a value below 0')], default=0)
    w25 = IntegerField('Week 25', [InputRequired('Week 25 can not be blank'),
                                   number_range(min=0, message='Week 25 can not have a value below 0')], default=0)
    w26 = IntegerField('Week 26', [InputRequired('Week 26 can not be blank'),
                                   number_range(min=0, message='Week 26 can not have a value below 0')], default=0)
    w27 = IntegerField('Week 27', [InputRequired('Week 27 can not be blank'),
                                   number_range(min=0, message='Week 27 can not have a value below 0')], default=0)
    w28 = IntegerField('Week 28', [InputRequired('Week 28 can not be blank'),
                                   number_range(min=0, message='Week 28 can not have a value below 0')], default=0)
    w29 = IntegerField('Week 29', [InputRequired('Week 29 can not be blank'),
                                   number_range(min=0, message='Week 29 can not have a value below 0')], default=0)
    w30 = IntegerField('Week 30', [InputRequired('Week 30 can not be blank'),
                                   number_range(min=0, message='Week 30 can not have a value below 0')], default=0)
    w31 = IntegerField('Week 31', [InputRequired('Week 31 can not be blank'),
                                   number_range(min=0, message='Week 31 can not have a value below 0')], default=0)
    w32 = IntegerField('Week 32', [InputRequired('Week 32 can not be blank'),
                                   number_range(min=0, message='Week 32 can not have a value below 0')], default=0)
    w33 = IntegerField('Week 33', [InputRequired('Week 33 can not be blank'),
                                   number_range(min=0, message='Week 33 can not have a value below 0')], default=0)
    w34 = IntegerField('Week 34', [InputRequired('Week 34 can not be blank'),
                                   number_range(min=0, message='Week 34 can not have a value below 0')], default=0)
    w35 = IntegerField('Week 35', [InputRequired('Week 35 can not be blank'),
                                   number_range(min=0, message='Week 35 can not have a value below 0')], default=0)
    w36 = IntegerField('Week 36', [InputRequired('Week 36 can not be blank'),
                                   number_range(min=0, message='Week 36 can not have a value below 0')], default=0)
    w37 = IntegerField('Week 37', [InputRequired('Week 37 can not be blank'),
                                   number_range(min=0, message='Week 37 can not have a value below 0')], default=0)
    w38 = IntegerField('Week 38', [InputRequired('Week 38 can not be blank'),
                                   number_range(min=0, message='Week 38 can not have a value below 0')], default=0)
    w39 = IntegerField('Week 39', [InputRequired('Week 39 can not be blank'),
                                   number_range(min=0, message='Week 39 can not have a value below 0')], default=0)
    w40 = IntegerField('Week 40', [InputRequired('Week 40 can not be blank'),
                                   number_range(min=0, message='Week 40 can not have a value below 0')], default=0)
    w41 = IntegerField('Week 41', [InputRequired('Week 41 can not be blank'),
                                   number_range(min=0, message='Week 41 can not have a value below 0')], default=0)
    w42 = IntegerField('Week 42', [InputRequired('Week 42 can not be blank'),
                                   number_range(min=0, message='Week 42 can not have a value below 0')], default=0)
    w43 = IntegerField('Week 43', [InputRequired('Week 43 can not be blank'),
                                   number_range(min=0, message='Week 43 can not have a value below 0')], default=0)
    w44 = IntegerField('Week 44', [InputRequired('Week 44 can not be blank'),
                                   number_range(min=0, message='Week 44 can not have a value below 0')], default=0)
    w45 = IntegerField('Week 45', [InputRequired('Week 45 can not be blank'),
                                   number_range(min=0, message='Week 45 can not have a value below 0')], default=0)
    w46 = IntegerField('Week 46', [InputRequired('Week 46 can not be blank'),
                                   number_range(min=0, message='Week 46 can not have a value below 0')], default=0)
    w47 = IntegerField('Week 47', [InputRequired('Week 47 can not be blank'),
                                   number_range(min=0, message='Week 47 can not have a value below 0')], default=0)
    w48 = IntegerField('Week 48', [InputRequired('Week 48 can not be blank'),
                                   number_range(min=0, message='Week 48 can not have a value below 0')], default=0)
    w49 = IntegerField('Week 49', [InputRequired('Week 49 can not be blank'),
                                   number_range(min=0, message='Week 49 can not have a value below 0')], default=0)
    w50 = IntegerField('Week 50', [InputRequired('Week 50 can not be blank'),
                                   number_range(min=0, message='Week 50 can not have a value below 0')], default=0)
    w51 = IntegerField('Week 51', [InputRequired('Week 51 can not be blank'),
                                   number_range(min=0, message='Week 51 can not have a value below 0')], default=0)

    submit = SubmitField('Add sales quantities')

