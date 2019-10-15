#!C:\Users\ACER\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

first_name = form.getvalue('fname')
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello Word - First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! This is my first CGI program</h2>')
print(' <form>')
print('Text:<br>')
print('<input type="text" name="firstname"><br>')

print('</form> ')
print('</body>')
print('</html>')
