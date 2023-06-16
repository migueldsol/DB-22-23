#!/usr/bin/python3
import psycopg2, login
import cgi

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html lang='en'>")
print("  <head>")
print("    <title>My Web Page</title>")
print(
    "    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM' crossorigin='anonymous' />"
)
print(
    "    <link href='https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/css/select2.min.css' rel='stylesheet' />"
)
print("    <link rel='stylesheet' href='./home.css' />")
print("  </head>")
print("  <body>")
print("    <div class='mb-3 header'>")
print("      <h2>Email:</h2>")
print("    </div>")
print("    <div class='content mb-5'>")
print(" <form action='Orders.cgi' method='post'>")
print("      <select class='form-control select2' id='mySelect2' name = 'customer'>")

connection = None

try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    cursor.execute("SELECT cust_no, email FROM customer;")

    for row in cursor.fetchall():
        cust_no, email = row
        print(f'<option value="{cust_no}">{email}</option>')

except Exception as e:
    print(f"<p>Error: {e}</p>")

finally:
    if connection is not None:
        connection.close()
print("      </select>")
print("    </div>")
print("    <button type='submit' class='btn btn-primary'>Submit</button>")
print("  </form>")
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
