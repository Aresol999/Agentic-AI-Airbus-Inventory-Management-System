from mcp.server.fastmcp import FastMCP
import pymysql as con
import pymysql.cursors
import datetime

def get_db():
    return con.connect(
        host="localhost",
        user="root",
        password="<YOUR_PASSWD>",
        cursorclass=pymysql.cursors.DictCursor
    )

def initialize_database():
    db = get_db()
    cur = db.cursor()
    
    cur.execute("CREATE DATABASE IF NOT EXISTS AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
    cur.execute("USE AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Inventory (
            Item_Serial_Number VARCHAR(300) PRIMARY KEY,
            Item_Name VARCHAR(300) NOT NULL,
            Manufacturing_Company VARCHAR(300) NOT NULL,
            Quantity INTEGER NOT NULL
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Finished_Products (
            Product_Serial_Number VARCHAR(300) PRIMARY KEY,
            Product_Type VARCHAR(300) NOT NULL,
            Date_Of_Building DATE,
            Quantity INTEGER NOT NULL,
            Status VARCHAR(300) NOT NULL
        )
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            Order_ID VARCHAR(300) PRIMARY KEY,
            Customer_Name VARCHAR(300),
            Product_Serial_Number VARCHAR(300),
            Quantity INTEGER NOT NULL,
            Status VARCHAR(300) NOT NULL,
            FOREIGN KEY (Product_Serial_Number) REFERENCES Finished_Products(Product_Serial_Number)
        )
    """)
    
    inventory_items = [
        ('ENG3201','Engine CFM 56','CFM International',2000), 
        ('ENG3202','Engine CFM LEAP','CFM International',4000),
        ('ENG33N1','Engine TRENT 7000','Rolls Royce',600), 
        ('ENG3501','Engine TRENT XWB','Rolls Royce',1500),
        ('ENG3801','Engine GP7000','Engine Alliance',300), 
        ('GEAR320','Landing Gear (A320)','HAECO',7000),
        ('GEAR33N','Landing Gear (A330neo)','Revima',650), 
        ('GEAR350','Landing Gear (A350)','Liebherr Aerospace',1650),
        ('GEAR380','Landing Gear (A380)','UTC Aerospace',350), 
        ('ALT1NN','Radio Altimeter','Collins Aerospace',10500),
        ('GYRO5NNN','Gyroscope','MEMS Manufacturers',20500), 
        ('BEACON1AA','Beacon lights','Airbus',2000)
    ]

    products = [
        ('F-GFK','Airbus A320','2007-03-14',40,'Delivered'), 
        ('F-AAA','Airbus A320','2018-11-12',400,'Available'),
        ('F-AVL','Airbus A320','2021-04-28',205,'Available'), 
        ('D-AIN','Airbus A320','2009-06-03',82,'On Order'),
        ('VT-EX','Airbus A320','2010-02-13',36,'Delivered'), 
        ('F-WTT','Airbus A330','2022-03-17',90,'Available'),
        ('CS-TU','Airbus A330','2018-12-11',20,'On Order'), 
        ('OO-AB','Airbus A330','2019-06-04',5,'Delivered'),
        ('N400DX','Airbus A330','2019-05-14',25,'On Order'),
        ('D-ANR','Airbus A330','2022-12-13',12,'On Order'),
        ('A7-AL','Airbus A350','2022-08-04',20,'Available'), 
        ('A7-AN','Airbus A350','2022-08-04',12,'Available'),
        ('D-AIX','Airbus A350','2017-03-12',52,'On Order'), 
        ('B-189','Airbus A350','2018-11-12',15,'Delivered'),
        ('OH-LW','Airbus A350','2020-05-16',26,'On Order'), 
        ('9V-SG','Airbus A350','2016-03-12',60,'On Order'),
        ('9M-MN','Airbus A380','2012-10-13',10,'Available'), 
        ('9V-SK','Airbus A380','2008-07-01',17,'Delivered'),
        ('A6-EV','Airbus A380','2008-08-03',119,'Delivered'), 
        ('HL761','Airbus A380','2011-03-12',9,'Delivered'),
        ('D-AIM','Airbus A380','2010-08-18',14,'Delivered')
    ]

    orders = [
        ('AFR189','Air France','F-GFK',40,'Delivered'), 
        ('DLH331','Lufthansa','D-AIN',82,'On Order'),
        ('AIC113','Air India','VT-EX',36,'Delivered'), 
        ('TAP221','Air Portugal','CS-TU',20,'On Order'),
        ('ABA123','Air Belgium','OO-AB',5,'Delivered'), 
        ('DAL002','Delta Air Lines','N400DX',25,'On Order'),
        ('CFG778','Condor','D-ANR',12,'On Order'),
        ('DLH009','Lufthansa','D-AIX',52,'On Order'),
        ('CAL334','Taiwan Air Lines','B-189',15,'Delivered'), 
        ('FIN358','Finnair','OH-LW',26,'On Order'),
        ('SIN489','Singapore Airlines','9V-SG',60,'On Order'), 
        ('SIN001','Singapore Airlines','9V-SK',17,'Delivered'),
        ('UAE001','Emirates','A6-EV',119,'Delivered'), 
        ('KAL001','Korean Air Lines','HL761',9,'Delivered'),
        ('DLH001','Lufthansa','D-AIM',14,'Delivered')
    ]

    cur.executemany("INSERT IGNORE INTO Inventory VALUES (%s,%s,%s,%s)", inventory_items)
    cur.executemany("INSERT IGNORE INTO Finished_Products VALUES (%s,%s,%s,%s,%s)", products)
    cur.executemany("INSERT IGNORE INTO Orders VALUES (%s,%s,%s,%s,%s)", orders)

    db.commit()
    db.close()

def format_result(data):
    if isinstance(data, (list, tuple)):
        for row in data:
            if isinstance(row, dict):
                for k, v in row.items():
                    if isinstance(v, (datetime.date, datetime.datetime)): row[k] = str(v)
    return data


mcp = FastMCP("Airbus Inventory Management System")
initialize_database()


@mcp.tool()
def list_all_orders():
    """Retrieve every order in the system (SELECT *)"""
    db=None

    try:
        db = get_db()

        db.select_db("AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
        cur = db.cursor()
        cur.execute("SELECT * FROM Orders")
        res = format_result(cur.fetchall())
        return res

    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if db:
            db.close()

@mcp.tool()
def list_all_inventory():
    """Retrieve the entire inventory list (SELECT *)"""
    db=None

    try:
        db = get_db()

        db.select_db("AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
        cur = db.cursor()
        cur.execute("SELECT * FROM Inventory")
        res = format_result(cur.fetchall())
        return res

    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if db:
            db.close()

@mcp.tool()
def list_all_products():
    """Retrieve all products (SELECT *)"""
    db=None

    try:
        db = get_db()    

        db.select_db("AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
        cur = db.cursor()
        cur.execute("SELECT * FROM Finished_Products")
        res = format_result(cur.fetchall())
        return res

    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if db:
            db.close()



@mcp.tool()
def search_orders(criteria: str, value: str):
    """Search orders by: Customer_Name, Product_Serial_Number, Quantity, Status, or Order_ID."""
    db=None

    try:
        db = get_db()

        db.select_db("AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
        cur = db.cursor()
        query = f"SELECT * FROM Orders WHERE {criteria} = %s"
        cur.execute(query, (value,))
        res = format_result(cur.fetchall())
        return res if res else "No matching records found."
    
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if db:
            db.close()

@mcp.tool()
def search_inventory(criteria: str, value: str):
    """Search inventory by: Item_Serial_Number, Item_Name, or Manufacturing_Company."""

    db=None

    try:
        db = get_db()

        db.select_db("AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
        cur = db.cursor()
        query = f"SELECT * FROM Inventory WHERE {criteria} = %s"
        cur.execute(query, (value,))
        res = format_result(cur.fetchall())
        return res if res else "No matching records found."

    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if db:
            db.close()

@mcp.tool()
def low_stock_search(threshold: int):
    """Find items with quantity less than threshold."""
    db=None

    try:
        db = get_db()

        db.select_db("AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
        cur = db.cursor()
        cur.execute("SELECT * FROM Inventory WHERE Quantity < %s", (threshold,))
        res = format_result(cur.fetchall())
        return res

    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if db:
            db.close()

@mcp.tool()
def delete_order(order_id: str):
    """Delete an order by its Order_ID."""
    db=None

    try:
        db = get_db()

        db.select_db("AIRBUS_INVENTORY_MANAGEMENT_SYSTEM")
        cur = db.cursor()
        cur.execute("DELETE FROM Orders WHERE Order_ID = %s", (order_id,))
        db.commit()
        return f"Order {order_id} deleted."
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    mcp.run()   