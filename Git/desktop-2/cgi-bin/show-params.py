import cgi

# ヘッダの表示
print("Content-Type: text/html; charset=utf-8")
print("")

print("<pre>")
# URLパラメータの取得
form = cgi.FieldStorage()

# 特定パラメータを取得して表示
mode = form.getvalue("mode", default="")
print("mode=", mode)

# すべてのパラメータを取得して表示
print("--- all params ---")
for k in form.keys():
    print(k, "=", form.getvalue(k))