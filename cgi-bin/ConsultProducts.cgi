#!/usr/bin/python3

import psycopg2, cgi
import login

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html>")
print("  <head>")
print("    <title>My Web Page</title>")
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
print("      <a href='ManageProducts.html' class='white-link'>Products</a>")
print("      <a href='ManageSuppliers.html'>Suppliers</a>")
print("      <a href='ManageCustomers.html'>Customers</a>")
print("    </div>")
print("    <div class='content'>")
print("      <h1>Products</h1>")
print("      <div class='table-responsive'>")
print("        <table id='myTable' class='table table-striped table-bordered'>")
print("          <thead>")
print("            <tr>")
print("              <th class='text-center'>sku</th>")
print("              <th class='text-center'>name</th>")
print("              <th class='text-center'>description</th>")
print("              <th class='text-center'>price</th>")
print("              <th class='text-center'>ean</th>")
print("              <th class='text-center'>edit</th>")
print("              <th class='text-center'>delete</th>")
print("            </tr>")
print("          </thead>")
print("          <tbody>")
connection = None

try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM product;")
    result = cursor.fetchall()

    for row in result:
        print("<tr>")
        for value in row:
            # The string has the {}, the variables inside format() will replace the {}
            print('<td class="text-center">{}</td>'.format(value))
        print("              <td class='text-center'>")
        print("                <form action='EditProduct.html' method='POST'>")
        print(
            "                  <input type='hidden' name='cust_no' value='{}' />".format(
                row[0]
            )
        )
        print("                  <button")
        print("                    type='submit'")
        print("                    class='btn btn-link p-0 border-0 float-right'")
        print("                  >")
        print("                    <img")
        print("                      src='icons/editWhite.png'")
        print("                      alt='Submit'")
        print("                      class='img-fluid'")
        print("                      style='width: 30px; height: 30px'")
        print("                    />")
        print("                  </button>")
        print("                </form>")
        print("              </td>")

        print("              <td class='text-center'>")
        print("                <form action='RemoveProduct.cgi' method='POST'>")
        print(
            "                  <input type='hidden' name='delete' value='{}' />".format(
                row[0]
            )
        )
        print("                  <button")
        print("                    type='submit'")
        print("                    class='btn btn-link p-0 border-0 float-right'")
        print("                  >")
        print("                    <img")
        print("                      src='icons/garbageBlack.png'")
        print("                      alt='Submit'")
        print("                      class='img-fluid'")
        print("                      style='width: 30px; height: 30px'")
        print("                    />")
        print("                  </button>")
        print("                </form>")
        print("              </td>")
        print("</tr>")
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
