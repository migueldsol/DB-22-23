#!/usr/bin/python3

import psycopg2, cgi
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
print("      <a href='ManageClients.html' class='white-link'>Clients</a>")
print("    </div>")
print("    <div class='content'>")

form = cgi.FieldStorage()

connection = None
try:
    cust_no = form.getvalue("Cust_no")
    name = form.getvalue("Name")
    email = form.getvalue("Email")
    phone = form.getvalue("Phone")
    address = form.getvalue("Address")

    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    add_client = (
        "INSERT INTO Project.customer "
        "(cust_no, name, email, phone, address) "
        "VALUES (%s, %s, %s, %s, %s)"
    )

    data_client = (cust_no, name, email, phone, address)

    # Insert new client
    cursor.execute(add_client, data_client)

    # commit the changes
    connection.commit()

    cursor.close()
    print("<h1>Client Added!</h1>")
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
