#!/usr/bin/python3
import psycopg2, cgi
from psycopg2 import errorcodes
import login

form = cgi.FieldStorage()

cust_no = form.getvalue("customer")
date = form.getvalue("date")

print("Content-Type: text/html\n\n")

print("<html>")
print("<head>")
print("<title>My Web Page</title>")
print(
    "<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM' crossorigin='anonymous' />"
)
print("<link rel='stylesheet' href='./styles2.css' />")
print("</head>")
print("<body>")
print("<div class='sidebar'>")
print("      <a href='Home.html'>Home</a>")
print("      <form action='Orders.cgi' method='POST'>")
print("        <input type='hidden' name='customer' value='{}'>".format(cust_no))
print("        <button type='submit' class='btn-a white-link'>Orders</button>")
print("      </form>")
print("    </div>")
print("    <div class='content'>")


connection = None
try:
    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    cursor.execute("""SELECT MAX(order_no) FROM "order" """)
    max_order_no = cursor.fetchone()[0]

    flag = False

    for sku in form.keys():
        if sku == "qty" or sku == "date" or sku == "customer":
            continue

        product_qty = form.getvalue(sku)

        date_add = {
            "cust_no" : cust_no,
            "order_no" : max_order_no + 1,
            "date" : date,
            "sku" : sku,
            "product_qty" : product_qty
        }

        if not flag:
            cursor.execute(
                """START TRANSACTION;
            SET CONSTRAINTS ALL DEFERRED;"""
            )

            cursor.execute(
                """INSERT INTO "order" (cust_no, order_no, date) VALUES (%(cust_no)s, %(order_no)s, %(date)s)""",
                date_add
            )

            cursor.execute(
                """INSERT INTO contains (order_no, sku, qty) VALUES (%(order_no)s, %(sku)s ,%(product_qty)s)""",
                date_add
            )
            cursor.execute("COMMIT;")
            flag = True
        else:
            cursor.execute(
                """INSERT INTO contains (order_no, sku, qty) VALUES (%(order_no)s, %(sku)s, %(product_qty)s)""",
                date_add
            )

    # commit the changes
    connection.commit()

    cursor.close()
    print("<h1>Order added!</h1>")
except psycopg2.IntegrityError as e:
    error_code = e.pgcode
    if error_code == errorcodes.UNIQUE_VIOLATION:
        error_message = e.diag.message_detail
        attribute_start = error_message.index("(") + 1
        attribute_end = error_message.index(")")

        attribute = error_message[attribute_start:attribute_end]
        print("<h1>An error occurred.</h1>")
        print("<p>{} already exists </p>".format(attribute))
    # Handle unique violation error with the specific attribute
    else:
        print("IntegrityError occurred:", str(e))
except psycopg2.InternalError as e:
    error_code = e.pgcode
    if error_code == errorcodes.RAISE_EXCEPTION:
        error_message = e.diag.message_detail
        print("<h1>An error occurred.</h1>")
        print("<p>Raise Exception raised {}</p>".format(error_message))
except Exception as e:
    # Print errors on the webpage if they occur
    print("<h1>An error occurred.</h1>")
    print("<p>Unknown Error{}</p>".format(e))
finally:
    if connection is not None:
        connection.close()

print("<div>")
print("  </body>")
print("</html>")
