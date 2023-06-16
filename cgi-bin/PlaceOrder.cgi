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
print("    <title>Place Order</title>")
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
print("        <h1>Place Order</h1>")
print("        <form action='Orders.cgi' method='POST'>")
print("          <input type='hidden' name='customer' value='{}'>".format(cust_no))
print("          <button type='submit' class='btn'>")
print(
    "            <img src='icons/back.png' alt='Back' style='width: 50px; height: 50px'>"
)
print("          </button>")
print("        </form>")
print("                </div>")
print("      <form action='VerifyOrder.cgi' method='POST'>")
print("      <div class='table-responsive'>")
print("        <table id='myTable' class='table table-striped table-bordered'>")
print("          <thead>")
print("            <tr>")
print("              <th class='text-center'>checkbox</th>")
print("              <th class='text-center'>sku</th>")
print("              <th class='text-center'>name</th>")
print("              <th class='text-center'>description</th>")
print("              <th class='text-center'>price</th>")
print("              <th class='text-center'>qty</th>")
print("            </tr>")
print("          </thead>")
print("          <tbody>")

connection = None

try:
    connection = psycopg2.connect(login.credentials)
    qry_produtcs = """Select sku,name,description,price FROM product"""
    cursor = connection.cursor()
    cursor.execute(
        qry_produtcs,
    )
    result = cursor.fetchall()

    for row in result:
        print("<tr>")
        print('<td class="text-center">')
        print(
            '  <input type="checkbox" class="checkboxInput" name="{}" value="">'.format(
                row[0]
            )
        )
        print("</td>")
        for i in range(4):
            print('<td class="text-center">{}</td>'.format(row[i]))
        print('<td class="text-center">')
        print('  <input type="number" class="numberInput" name="qty">')
        print("</td>")
        print("</tr>")

    print('<div class="mb-3">')
    print('  <label for="date" class="form-label">Date</label>')
    print("  <input")
    print("    required")
    print('    type="date"')
    print('    class="form-control"')
    print('    id="date"')
    print('    name="date"')
    print('    placeholder="Enter Supplier\'s SKU"')
    print("  />")
    print("</div>")

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
print("        <input type='hidden' name='customer' value='{}'>".format(cust_no))
print("        <input type='submit' value='Place Order' class='btn btn-primary'>")
print("      </form>")
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
print("          pageLength: 12,")
print("          lengthChange: false,")
print("        });")
print("      });")
print("    </script>")
print("<script>")
print("var numberInputs = document.getElementsByClassName('numberInput');")
print("var checkboxInputs = document.getElementsByClassName('checkboxInput');")
print("for (var i = 0; i < numberInputs.length; i++) {")
print("  numberInputs[i].addEventListener('change', function() {")
print(
    "    checkboxInputs[Array.prototype.indexOf.call(numberInputs, this)].value = this.value;"
)
print("  });")
print("}")
print("</script>")


print("  </body>")
print("</html>")
