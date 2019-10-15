#!C:\Users\ACER\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi, cgitb 
import wave

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

first_name = form.getvalue('fname')

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Encryptor</title>')
print('</head>')
print('<body>')

print('<h1> encrypting %s</h1>' %(first_name))

f = open('ans.txt','w+')
f.write(first_name)

k = open('decryptor.txt','w+')
k.write('Encryption code for a is 97\n')
k.write('Encryption code for b is 98\n')
k.write('Encryption code for c is 99\n')
k.write('Encryption code for d is 100\n')
k.write('Encryption code for e is 101\n')
k.write('Encryption code for f is 102\n')
k.write('Encryption code for g is 103\n')
k.write('Encryption code for h is 104\n')
k.write('Encryption code for i is 105\n')
k.write('Encryption code for j is 106\n')
k.write('Encryption code for k is 107\n')
k.write('Encryption code for l is 108\n')
k.write('Encryption code for m is 109\n')
k.write('Encryption code for n is 110\n')
k.write('Encryption code for o is 111\n')
k.write('Encryption code for p is 112\n')
k.write('Encryption code for q is 113\n')
k.write('Encryption code for r is 114\n')
k.write('Encryption code for s is 115\n')
k.write('Encryption code for t is 116\n')
k.write('Encryption code for u is 117\n')
k.write('Encryption code for v is 118\n')
k.write('Encryption code for w is 119\n')
k.write('Encryption code for x is 120\n')
k.write('Encryption code for y is 121\n')
k.write('Encryption code for z is 122\n')
k.write('The encryption string is '+first_name)


infiles = ["music/1.wav", "music/2.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav","music/3.wav"]
outfile = "sounds.wav"
tempfiles = []

for i in first_name:
    print('<p> encrypting %s</p>'%(i))
    if i is 'a':
        tempfiles.append(infiles[0])
    elif i is 'b':
        tempfiles.append(infiles[1])
    elif i is 'c':
        tempfiles.append(infiles[1])
    elif i is 'd':
        tempfiles.append(infiles[1])
    elif i is 'e':
        tempfiles.append(infiles[1])
    elif i is 'f':
        tempfiles.append(infiles[1])
    elif i is 'g':
        tempfiles.append(infiles[1])
    elif i is 'h':
        tempfiles.append(infiles[1])
    elif i is 'i':
        tempfiles.append(infiles[1])
    elif i is 'j':
        tempfiles.append(infiles[1])
    elif i is 'k':
        tempfiles.append(infiles[2])
    elif i is 'l':
        tempfiles.append(infiles[2])
    elif i is 'm':
        tempfiles.append(infiles[2])
    elif i is 'n':
        tempfiles.append(infiles[2])
    elif i is 'o':
        tempfiles.append(infiles[2])
    elif i is 'p':
        tempfiles.append(infiles[2])
    elif i is 'q':
        tempfiles.append(infiles[2])
    elif i is 'r':
        tempfiles.append(infiles[2])
    elif i is 's':
        tempfiles.append(infiles[2])
    elif i is 't':
        tempfiles.append(infiles[2])
    elif i is 'u':
        tempfiles.append(infiles[2])
    elif i is 'x':
        tempfiles.append(infiles[2])  
    elif i is 'y':
        tempfiles.append(infiles[2])  
    elif i is 'z':
        tempfiles.append(infiles[2]) 
        
    
data= []
print("<p>files %s<p>"%(tempfiles))

for j in tempfiles:
    w = wave.open(j, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])

j=0
for i in range(len(tempfiles)):
    output.writeframes(data[j][1])
    j = j+1

output.close()

print('<a href="sounds.wav" download >Download</a>')
print('</body>')
print('</html>')