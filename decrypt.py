#!C:\Users\ACER\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi, cgitb 
import wave

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello Word - First CGI Program</title>')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">')
print('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>')
print('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>')
print('<script src="decrypt.js"></script> ')
print('</head>')
print('<body>')
print('<div class="jumbotron">')
print('<h1>Check your encrypted music </h1>')
print('</div>')
f = open('ans.txt')
a = f.readlines()
name = a[0]
print('<p>Upload your encrypted audio file.</p>')
print('<input type="file" id="myfile" ')
print('<div>')
print('<button type="button" onclick="change()" class="btn btn-success">Decrypt</button>')
print('</div>')
print('<p> The decrypted msg is : <h1 style="display:none;" id="name" > %s</h1> </p>'%(name))
print()

print('<a href="decryptor.txt" download >Download</a>')
print('</body>')
print('</html>')