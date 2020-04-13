CREATE TABLE Menu(
    id integer primary key autoincrement not null,
    items varchar(255),
    category varchar(255),
    price integer
);
CREATE TABLE Storage(
    id integer primary key autoincrement ,
    name varchar(255),
    unit integer,
    unitprice integer,
    quantity integer
);
CREATE table MadeWith(
    Itemsid integer,
    Ingridientsid integer,
    quantity integer,
    foreign key(Ingridientsid) references Storage(id),
    foreign key(Itemsid) references Menu(id)

    );
CREATE table Tables(
    id integer primary key autoincrement,
    Employeeid integer,
    Reservationid integer,
    foreign key(Employeeid) references Employee(id)
);
Create TABLE Orders(
    id integer primary key autoincrement,
    itemsid integer,
    tableid integer,
    foreign key(itemsid) references Menu(id),
    foreign key(tableid) references Tables(id)
);
CREATE table Employee(
    id integer primary key autoincrement,
    role varchar(255),
    first_name varchar(255),
    second_name varchar(255),
    email varchar(255),
    adress varchar(255)
);
CREATE table Customer(
    id integer primary key autoincrement,
    first_name varchar(255),
    second_name varchar(255),
    contact_number varchar(255)
);
CREATE table Reservation(
    Reservationid integer,
    Customerid integer,
    date datetime,
    foreign key(Reservationid) references Tables(Reservationid),
    foreign key(Customerid) references Customer(id)
);
CREATE table Receipt(
    id integer primary key autoincrement,
    paymentid integer
);
CREATE table OrdersReceipt(
    Receiptid integer,
    Orderid integer,
    quantity integer,
    foreign key(Receiptid) references Receipt(id),
    foreign key (Orderid) references Orders(id)
);
CREATE table Payment(
    id integer primary key autoincrement,
    date datetime,
    amount integer,
    paymentype varchar(255),
    foreign key(id) references Receipt(paymentid)
);