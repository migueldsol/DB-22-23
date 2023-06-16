#!/usr/bin/python3

import psycopg2, cgi
from psycopg2 import errorcodes
import login

print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()

product_sku = form.getvalue("product_sku")

connection = None

# Perform any necessary processing with the received values

print("<!DOCTYPE html>")
print('<html lang="en">')
print("  <head>")
print("    <title>My Web Page</title>")
print(
    '    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous" />'
)
print('    <link rel="stylesheet" href="./styles2.css" />')
print("  </head>")
print("  <body>")
print('    <div class="sidebar">')
print('      <a href="Home.html">Home</a>')
print('      <a href="ManageProducts.html" class="white-link">Products</a>')
print('      <a href="ManageSuppliers.html">Suppliers</a>')
print('      <a href="ManageCustomers.html">Customers</a>')
print("    </div>")
print('    <div class="content">')
try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    query = "SELECT description FROM product WHERE product.sku = %s"
    cursor.execute(query, (product_sku,))
    result = cursor.fetchone()
except Exception as e:
    print("<h1>An error occurred.</h1>")
    print("<p>{}</p>".format(e))
finally:
    if connection is not None:
        connection.close()
print('      <div class="flex-container">')
print("        <h1>Alter Description</h1>")
print('        <a href="EditProduct.cgi" class="mb-5" style="margin-right: 25px">')
print(
    '          <img src="icons/back.png" alt="Back" style="width: 50px; height: 50px" />'
)
print("        </a>")
print("</div>")
print('<div class="mb-3">')
print('        <label for="product_sku" class="form-label">Old Description</label>')
print("  <textarea")
print("    readonly")
print('    class="form-control"')
print('    rows="3"')
print("  >{}</textarea>".format(result[0]))
print("</div>")
print('      <form action="AlterDescriptionCheck.cgi" method="post">')
print('<div class="mb-3">')
print(
    '          <label for="new_description" class="form-label">New Description</label>'
)
print("  <textarea")
print("    required")
print('    placeholder="Enter product\'s Description"')
print('    class="form-control"')
print('    id="new_escription"')
print('    name="new_description"')
print('    rows="3"')
print("  ></textarea>")
print("</div>")
print(
    '          <input required type="hidden" name="product_sku" value = {}>'.format(
        product_sku
    )
)
print('        <button type="submit" class="btn btn-primary mt-3">Submit</button>')
print("      </form>")
print("    </div>")
print("  </body>")
print("</html>")
