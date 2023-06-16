#!/usr/bin/python3

import psycopg2, cgi
from psycopg2 import errorcodes
import login

form = cgi.FieldStorage()

cust_no = form.getvalue("customer")

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html>")
print("  <head>")
print("    <title>Consult Orders</title>")
print(
    "    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM' crossorigin='anonymous' />"
)
print("    <link rel='stylesheet' href='styles2.css' />")
print(
    "    <link rel='stylesheet' type='text/css' href='https://cdn.datatables.net/1.11.4/css/jquery.dataTables.css'>"
)
print("  </head>")
print("  <body>")
print("    <div class='sidebar'>")
print("      <a href='Home.html'>Home</a>")
print("      <form action='Orders.cgi' method='POST'>")
print("        <input type='hidden' name='customer' value='{}'>".format(cust_no))
print("        <button type='submit' class='btn-a white-link'>Orders</button>")
print("      </form>")
print("    </div>")
print("    <div class='content'>")
print("      <div class='flex-container'>")
print("        <h1>Consult Orders</h1>")
print("        <form action='Orders.cgi' method='POST'>")
print("          <input type='hidden' name='customer' value='{}'>".format(cust_no))
print("          <button type='submit' class='btn'>")
print(
    "            <img src='icons/back.png' alt='Back' style='width: 50px; height: 50px'>"
)
print("          </button>")
print("        </form>")
print("                </div>")
print("      <div class='table-responsive'>")
print("        <table id='myTable' class='table table-striped table-bordered'>")
print("          <thead>")
print("            <tr>")
print("              <th class='text-center'>order_no</th>")
print("              <th class='text-center'>date</th>")
print("              <th class='text-center'>Status</th>")
print("            </tr>")
print("          </thead>")
print("          <tbody>")

connection = None

try:
    connection = psycopg2.connect(login.credentials)
    sql = """SELECT o.order_no,o.date,
            CASE WHEN p.cust_no IS NOT NULL THEN 'Yes' ELSE 'No' END as paid
            FROM customer c
            LEFT JOIN "order" o ON c.cust_no = o.cust_no
            LEFT JOIN pay p ON c.cust_no = p.cust_no AND o.order_no = p.order_no
            WHERE c.cust_no = %(cust_no)s;
          """
    cursor = connection.cursor()
    cursor.execute(sql, {"cust_no": cust_no})
    result = cursor.fetchall()

    for row in result:
        print("<tr>")
        for i in range(2):
            # The string has the {}, the variables inside format() will replace the {}
            print('<td class="text-center">{}</td>'.format(row[i]))
        if row[2] == "No":
            print("              <td class='text-center'>")
            print("                <form action='PayProduct.cgi' method='POST'>")
            print(" <input type='hidden' name='order_no' value='{}' />".format(row[0]))
            print(" <input type='hidden' name='cust_no' value='{}' />".format(cust_no))
            print("                  <button")
            print("                    type='submit'")
            print("                    class='btn btn-link p-0 border-0 ")
            print("                  >")
            print("                    <p class='text-primary p-0 border-0'>Pay</p>")
            print("                  </button>")
            print("                </form>")
            print("              </td>")
        else:
            print('<td class="text-center">Payed</td>')
except psycopg2.InvalidName as e:
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
    print("<h1>An error occurred.</h1>")
    print("<p>{}</p>".format(e))
finally:
    if connection is not None:
        connection.close()
print("          </tbody>")
print("        </table>")
print("      </div>")
print("    </div>")
print("    <script")
print("      type='text/javascript'")
print("      charset='utf8'")
print("      src='https://code.jquery.com/jquery-3.5.1.js'")
print("    ></script>")
print("    <script")
print("      type='text/javascript'")
print("      charset='utf8'")
print("      src='https://cdn.datatables.net/1.11.4/js/jquery.dataTables.js'")
print("    ></script>")
print("    <script>")
print("      // Apply DataTable to our table")
print("      $(document).ready(function () {")
print("        $('#myTable').DataTable({")
print("          pageLength: 14,")
print("          lengthChange: false,")
print("        });")
print("      });")
print("    </script>")
print("  </body>")
print("</html>")
