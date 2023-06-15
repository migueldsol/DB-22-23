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
print("      <a href='ManageSuppliers.html'>Suppliers</a>")
print("      <a href='ManageCustomers.html' class='white-link'>Customers</a>")
print("    </div>")
print("    <div class='content'>")

form = cgi.FieldStorage()

cust_no = form.getvalue("Cust_no")
name = form.getvalue("Name")
email = form.getvalue("Email")
phone = form.getvalue("Phone")
address = form.getvalue("Address")

connection = None
try:
    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    add_client = (
        "INSERT INTO customer "
        "(cust_no, name, email, phone, address) "
        "VALUES (%(cust_no)s, %(name)s, %(email)s, %(phone)s, %(address)s)"
    )

    data_client = {
        "cust_no": cust_no,
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
    }

    # Insert new client
    cursor.execute(add_client, data_client)

    # commit the changes
    connection.commit()

    cursor.close()
    print("<h1>Customer Added!</h1>")
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
    print("<p>Unknown Error</p>")
finally:
    if connection is not None:
        connection.close()

print("<div>")
print("  </body>")
print("</html>")
