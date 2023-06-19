#!/usr/bin/python3
import psycopg2, cgi
import login
import html

form = cgi.FieldStorage()

cust_no = form.getvalue("customer")

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html lang='en'>")
print("  <head>")
print("    <title>My Web Page</title>")
print(
    "    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM' crossorigin='anonymous' />"
)
print("    <link rel='stylesheet' href='styles2.css' />")
print("  </head>")
print("  <body>")
print("    <div class='sidebar'>")
print("      <a href='Home.html'>Home</a>")
print("      <a href='Orders.cgi' class='white-link'>Orders</a>")
print("    </div>")
print("    <div class='content'>")
print("      <div class='flex-container'>")
print("        <h1>Orders</h1>")
print("        <a href='Orders.cgi' class='mb-5' style='margin-right: 25px'>")
print(
    "          <img src='icons/back.png' alt='Back' style='width: 50px; height: 50px' />"
)
print("        </a>")
print("      </div>")
print('      <form action="RemoveOrder.cgi" method="POST">')
print('      <div class="mb-3">')
print('         <label for="product_sku" class="form-label">SKU</label>')
print('         <select class="form-control select2" id="mySelect2">')

connection = None

try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    query = """SELECT o.order_no 
                FROM customer c 
                JOIN order o
                WHERE c.customer_id = %s;"""

    cursor.execute(query, (cust_no,))

    for row in cursor.fetchall():
        cust_no = row[0]
        print(f'<option value="{cust_no}">{cust_no}</option>')

except Exception as e:
    print(f"<p>Error: {e}</p>")

finally:
    if connection is not None:
        connection.close()

print("          </select>")
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
print("    </div>")
print("  </body>")
print("</html>")
