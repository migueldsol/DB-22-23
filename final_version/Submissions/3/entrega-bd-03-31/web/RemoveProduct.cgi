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
print('      <a href="ManageProducts.html" class="white-link">Products</a>')
print('      <a href="ManageSuppliers.html">Suppliers</a>')
print('      <a href="ManageCustomers.html">Customers</a>')
print("    </div>")
print("    <div class='content'>")

form = cgi.FieldStorage()

sku = form.getvalue("product_sku")

connection = None
try:
    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    delete_product = """DELETE FROM product WHERE sku = %s"""

    delete_contains_order_no = """DELETE FROM contains WHERE order_no = %s"""

    delete_contains_order_no_and_sku = (
        """DELETE FROM contains WHERE order_no = %s AND sku = %s"""
    )

    delete_order = """DELETE FROM "order" WHERE order_no = %s"""

    delete_supplier = """DELETE FROM supplier WHERE sku = %s"""

    select_supplier_with_sku = """SELECT tin FROM supplier WHERE sku = %s"""

    start_transaction = """START TRANSACTION; SET CONSTRAINTS ALL DEFERRED;"""

    delete_delivery = """DELETE FROM delivery WHERE tin = %s"""

    delete_pay = """DELETE FROM pay WHERE order_no = %s"""

    select_order_with_sku = (
        """SELECT order_no FROM "order" NATURAL JOIN contains WHERE sku = %s"""
    )

    count_contains_from_order = """SELECT COUNT(*) FROM contains WHERE order_no = %s"""

    cursor.execute(select_supplier_with_sku, (sku,))  # gets the suppliers

    supplier_tins = cursor.fetchall()

    for i in supplier_tins:
        cursor.execute(delete_delivery, (i,))  # deletes the deliverys

    cursor.execute(delete_supplier, (sku,))  # deletes the suppliers

    cursor.execute(select_order_with_sku, (sku,))

    orders_with_sku = cursor.fetchall()

    for order_no in orders_with_sku:  # goes to each order with sku
        cursor.execute(count_contains_from_order, (order_no,))

        contains_in_order = cursor.fetchall()

        if contains_in_order[0][0] == 1:                #if last contains gotta delete order
            cursor.execute("""DELETE FROM pay WHERE order_no = %s""", (order_no[0],))  #delete pay

            cursor.execute("""DELETE FROM process where order_no = %s""", (order_no[0],))  #delete process

            cursor.execute(start_transaction)  # starts transaction

            cursor.execute(delete_contains_order_no, (order_no[0],))  # deletes contains

            cursor.execute(delete_order, (order_no[0],))  # deletes the order

            cursor.execute("COMMIT;")
        else:
            cursor.execute(delete_contains_order_no_and_sku, (order_no[0], sku))   #just deletes contain with sku X

    cursor.execute(delete_product, (sku,))
    connection.commit()

    cursor.close()
    print("<h1>Product Removed!</h1>".format(sku))

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
