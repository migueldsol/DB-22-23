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
print('      <a href="ManageSuppliers.html" class="white-link">Suppliers</a>')
print('      <a href="ManageCustomers.html">Customers</a>')
print("    </div>")
print("    <div class='content'>")

form = cgi.FieldStorage()

tin = form.getvalue("tin")

connection = None
try:
    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    delete_supplier_tin = """DELETE FROM supplier WHERE tin = %s"""

    delete_product = """DELETE FROM product WHERE sku = %s"""

    delete_contains_order_no = """DELETE FROM contains WHERE order_no = %s"""

    delete_contains_order_no_and_sku = (
        """DELETE FROM contains WHERE order_no = %s AND sku = %s"""
    )

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

    cursor.execute(
        """SELECT sku FROM supplier WHERE tin = %s""", (tin,)
    )  # get the skus with supplier tin X
    supplier_skus = cursor.fetchall()
    print("<p>supplier_skus {}</p>".format(supplier_skus))

    for j in supplier_skus:  # run through the skus
        print("<p>j {}</p>".format(j))
        cursor.execute(
            """SELECT COUNT(*) FROM supplier WHERE sku = %s""", j[0]
        )  # count the supplier
        number_of_suppliers = cursor.fetchall()
        print("<p>number_of_supplier {}</p>".format(number_of_suppliers))

        if (
            number_of_suppliers[0][0] == 1
        ):  # if only one supplier need to remove product
            cursor.execute(select_order_with_sku, (j[0],))

            orders_with_sku = cursor.fetchall()
            print("<p>orders_with_sku {}</p>".format(orders_with_sku))

            for i in orders_with_sku:  # goes to each order with sku
                print("<p>i {}</p>".format(i))

                cursor.execute(count_contains_from_order, (i,))

                contains_in_order = cursor.fetchall()
                print("<p>contains_in_Order{}</p>".format(contains_in_order))

                if (
                    contains_in_order[0][0] == 1
                ):  # if only 1 contains need to remove order
                    print("<p>deletes_order</p>")
                    cursor.execute(start_transaction)  # starts transaction

                    cursor.execute(
                        delete_contains_order_no, (i[0],)
                    )  # deletes contains

                    cursor.execute(delete_pay, (i[0],))

                    cursor.execute(delete_order, (i[0],))  # deletes the order

                    cursor.execute("COMMIT;")
                else:
                    cursor.execute(delete_contains_order_no_and_sku, (i[0], j[0]))
            cursor.execute("""DELETE FROM delivery WHERE tin = %s""", (tin,))
            cursor.execute(delete_supplier_tin, (tin,))
            cursor.execute(delete_product, (j[0],))
        else:
            cursor.execute("""DELETE FROM delivery WHERE tin = %s""", (tin,))
            cursor.execute(delete_supplier_tin, (tin,))

    connection.commit()

    cursor.close()
    print("<h1>Supplier Removed!</h1>")
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
