from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

madewith = db.Table('madewith',
                    db.Column('menu_id', db.Integer, db.ForeignKey('menu.id')),
                    db.Column('storage_id', db.Integer, db.ForeignKey('storage.id')))

reservation = db.Table('reservation',
                       db.Column('reservation_id', db.Integer, db.ForeignKey('table.reservationid')),
                       db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
                       db.Column('date', db.DateTime))

orders = db.Table('orders',
                  db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                  db.Column('menu_id', db.Integer, db.ForeignKey('menu.id')),
                  db.Column('table_id', db.Integer, db.ForeignKey('table.id')))

ordersreceipt = db.Table('ordersreceipt',
                         db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                         db.Column('receipt_id', db.Integer, db.ForeignKey('receipt.id')))


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    items = db.Column(db.String(50), nullable=False, unique=True)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    ingr = db.relationship('Storage', secondary=madewith, backref=db.backref('menus'))


class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    unit_price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employeeid = db.Column(db.Integer, db.ForeignKey('employee.id'))
    reservationid = db.Column(db.Integer)
    menu_rel = db.relationship('Menu', secondary=orders, backref=db.backref('menu_rel'))
    cust_rel = db.relationship('Customer', secondary=reservation, backref=db.backref('cust_rel'))


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    address = db.Column(db.String(100))
    tables = db.relationship('Table', backref='tables')


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(20))


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payments = db.relationship('Payment', backref='receipt')


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer)
    type = db.Column(db.String(15))
    date = db.Column(db.DateTime)
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipt.id'))


db.create_all()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html', items=Menu.query.all())


@app.route('/storage')
def storage():
    return render_template('storage.html', storage=Storage.query.all())


@app.route('/customers')
def customer():
    return render_template('customer.html', customer=Customer.query.all())


@app.route('/employees')
def employee():
    return render_template('employee.html', employee=Employee.query.all())


@app.route('/payments')
def payment():
    return render_template('payment.html', payment=Payment.query.all())


# @app.route('/add_items', methods=['POST'])
# def add_items():
#    items = request.form['items']
#    category = request.form['category']
#    price = request.form['price']
#
#    db.session.add(Menu(items, category, price))
#    db.session.commit()
#    return redirect('/menu')


# @app.route('/add_storage', methods=['POST'])
# def add_storage():
#    name = request.form['name']
#    unitprice = request.form['unit_price']
#    quantity = request.form['quantity']

#    db.session.add(Storage(name, unitprice, quantity))
#    db.session.commit()
#    return redirect('/storage')


@app.route('/menu/<id>')
def item(id):
    item_query = Menu.query.filter_by(id=id).first_or_404()
    return render_template('item.html', items=item_query)


@app.route('/delete_items/<id>', methods=['POST'])
def delete_items(id):
    to_delete = Menu.query.filter_by(id=id).first()
    db.session.delete(to_delete)
    db.session.commit()
    return redirect('/menu')


@app.route('/edit_items/<id>', methods=['GET', 'POST'])
def edit_items(id):
    to_edit = Menu.query.filter_by(id=id).first()
    if request.method == 'POST':
        to_edit.items = request.form['items']
        to_edit.category = request.form['category']
        to_edit.price = request.form['price']
        db.session.commit()
        return redirect('/menu')
    else:
        return render_template('edit.html', edit=to_edit)


