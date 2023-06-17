#!/usr/bin/python3

import psycopg2, cgi
from psycopg2 import errorcodes
import login

print("Content-Type: text/html\n\n")

print("<!DOCTYPE html>")
print("<html lang='en'>")
print("  <head>")
print("    <title>My Web Page</title>")
print(
    "     <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM' crossorigin='anonymous' />"
)
print("   <link rel='stylesheet' href='./styles2.css' />")
print("  </head>")
print("  <body>")
print('    <div class="sidebar">')
print('      <a href="Home.html">Home</a>')
print('      <a href="ManageProducts.html">Products</a>')
print('      <a href="ManageSuppliers.html">Suppliers</a>')
print('      <a href="ManageCustomers.html" class="white-link">Customers</a>')
print("    </div>")
print("    <div class='content'>")

form = cgi.FieldStorage()

cust_no = form.getvalue("cust_no")

connection = None
try:
    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    delete_supplier_tin = """DELETE FROM supplier WHERE tin = %s"""

    delete_product = """DELETE FROM product WHERE sku = %s"""

    delete_contains_order_no = """DELETE FROM contains WHERE order_no = %s"""

    delete_order = """DELETE FROM "order" WHERE order_no = %s"""

    delete_supplier_sku = """DELETE FROM supplier WHERE sku = %s"""

    select_supplier_with_sku = """SELECT tin FROM supplier WHERE sku = %s"""

    start_transaction = """START TRANSACTION; SET CONSTRAINTS ALL DEFERRED;"""

    delete_delivery = """DELETE FROM delivery WHERE tin = %s"""

    delete_pay = """DELETE FROM pay WHERE order_no = %s"""

    select_order_with_sku = (
        """SELECT order_no FROM "order" NATURAL JOIN contains WHERE sku = %s"""
    )

    count_contains_from_order = """SELECT COUNT(*) FROM contains WHERE order_no = %s"""

    # elim order
    cursor.execute(
        """SELECT order_no FROM "order" NATURAL JOIN customer WHERE cust_no = %s""",
        (cust_no,),
    )
    orders_of_customer = cursor.fetchall()          #selects the orders of the customer

    for order in orders_of_customer:                #deletes the pay and process of the orders
        cursor.execute("""DELETE FROM pay WHERE order_no = %s""", (order[0],))
        cursor.execute("""DELETE FROM process WHERE order_no = %s""", (order[0],))

        cursor.execute(count_contains_from_order, (order[0],))

        contains_in_order = cursor.fetchall()

        cursor.execute(start_transaction)  # starts transaction

        cursor.execute(delete_contains_order_no, (order[0],))  # deletes contains

        cursor.execute(delete_order, (order[0],))  # deletes the order

        cursor.execute("COMMIT;")

    cursor.execute("""DELETE FROM customer WHERE cust_no = %s""", (cust_no,))
    connection.commit()
    cursor.close()
    print("<h1>Customer Removed!</h1>")


except psycopg2.InternalError as e:
    error_code = e.pgcode
    if error_code == errorcodes.RAISE_EXCEPTION:
        print("<h1>An error occurred.</h1>")
        print("<p>{},{}</p>".format(e, e.pgcode))
        # Handle unique violation error with the specific attribute
    else:
        print("IntegrityError occurred:", str(e))
except Exception as e:
    # Print errors on the webpage if they occur
    print("<h1>An error occurred.</h1>")
    print("<p>{}</p>".format(e))
finally:
    if connection is not None:
        connection.close()
print("<div>")
print("  </body>")
print("</html>")
