#!/usr/bin/python3

import psycopg2
import login
import cgi

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html lang='en'>")
print("  <head>")
print("    <title>My Web Page</title>")
print("    <link")
print(
    '      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"'
)
print('      rel="stylesheet"')
print(
    '      integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"'
)
print('      crossorigin="anonymous"')
print("    />")
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
print('      <div class="flex-container">')
print("        <h1>Remove Product</h1>")
print('        <a href="ManageProducts.html" class="mb-5" style="margin-right: 25px">')
print("          <img")
print('            src="icons/back.png"')
print('            alt="Back"')
print('            style="width: 50px; height: 50px"')
print("          />")
print("        </a>")
print("      </div>")
print('      <form action="RemoveProduct.cgi" method="POST">')
print('      <div class="mb-3">')
print('         <label for="product_sku" class="form-label">SKU</label>')
print(
    '         <select class="form-control select2" id="product_sku" name = "product_sku">'
)

connection = None

try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    cursor.execute("SELECT sku FROM product;")

    for row in cursor.fetchall():
        sku = row[0]
        print(f'<option value="{sku}">{sku}</option>')

except Exception as e:
    print(f"<p>Error: {e}</p>")

finally:
    if connection is not None:
        connection.close()

print("          </select>")
print('          <div id="text" class="form-text">')
print("            The SKU number must be at max 25 digits long.")
print("          </div>")
print("        </div>")
print('        <button type="submit" class="btn btn-primary mt-3">Submit</button>')
print("      </form>")
print("    </div>")
print(
    "    <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>"
)
print(
    "    <script src='https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js'></script>"
)
print("    <script>")
print("      $(document).ready(function () {")
print("        $('#mySelect2').select2();")
print("      });")
print("    </script>")
print("  </body>")
print("</html>")
