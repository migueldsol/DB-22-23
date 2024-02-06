#!/usr/bin/python3

import psycopg2, cgi
from psycopg2 import errorcodes
import login

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
print("      <a href='ManageProducts.html'>Products</a>")
print("      <a href='ManageSuppliers.html' class='white-link'>Suppliers</a>")
print("      <a href='ManageCustomers.html'>Customers</a>")
print("    </div>")
print("    <div class='content'>")

form = cgi.FieldStorage()

tin = form.getvalue("TIN")
name = form.getvalue("Name")
address = form.getvalue("Address")
sku = form.getvalue("SKU")
date = form.getvalue("Date")

connection = None
try:
    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    add_supplier = (
        "INSERT INTO supplier "
        "(tin, name, address, sku, date) "
        "VALUES (%(tin)s, %(name)s, %(address)s, %(sku)s, %(date)s)"
    )

    data_supplier = {
        "tin": tin,
        "name": name,
        "address": address,
        "sku": sku,
        "date": date,
    }

    # Insert new Customer
    cursor.execute(add_supplier, data_supplier)

    # commit the changes
    connection.commit()

    cursor.close()
    print("<h1>Supplier Added!</h1>")
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
