#!/usr/bin/python3

import psycopg2, cgi
import login

print("Content-Type: text/html\n\n")

print("<!DOCTYPE html>")
print("<html lang='en'>")
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
print("      <a href='ManageProducts.html' class='white-link>Products</a>")
print("      <a href='ManageSuppliers.html'>Suppliers</a>")
print("      <a href='ManageClients.html'>Clients</a>")
print("    </div>")
print("    <div class='content'>")

form = cgi.FieldStorage()

sku = form.getvalue("product_sku")
name = form.getvalue("Name")
price = form.getvalue("Price")
ean = form.getvalue("EAN")
description = form.getvalue("Description")


connection = None
try:
    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    delete_product = (
        "DELETE FROM product "
        "WHERE sku = %s"
    )

    cursor.execute(delete_product, (sku,))

    connection.commit()

    cursor.close()
    print("<h1>Product Removed!</h1>")
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