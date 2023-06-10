#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Manager</title>')
print('<link rel="stylesheet" href="output.css">')  # Move the <link> tag here
print('<style>')
print("body {")
print("    background-color: #D4DFDC")
print("}")
print('</style>')
print('</head>')
print('<body>')

connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    print('<h1> HOME PAGE\n <h1>')
    print('<button> \nclick here <button>' )
    # Closing connection
    cursor.close()
except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close()
print('</body>')
print('</html>')