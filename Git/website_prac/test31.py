import random
import sys,io
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer,
    encoding='utf-8'
)

ran_int = random.randint(1, 100)

print("Content-Type: text/html; charset=utf-8\n")
print("<html>")
print("<head>")
print("<meta charset='utf-8'>")
print("</head>")
print("<body>")

print("<h1>{num}</h1>".format(num=ran_int))
form = cgi.FieldStorage()

for key in form.keys():
    print(key, " = ", form.getvalue(key))

mode = form.getvalue("mode")
print("<p>mode = ", mode, "</p>")

print("</body>")

print("<ul>")
for i in range(5):
    print("<li>Test Python</li>")
print("</ul>")
print(random.randint(1, 100))
print("</body></html>")

