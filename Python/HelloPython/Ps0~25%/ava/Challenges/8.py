text = "No system is safe"
print(len(text))

text1 = "BackdoorAccess"
print(text1[0])
print(text1[3])
print(text[-1])

text2 = "FirewallBypass"
print(text2[0:7])
print(text2[8:])

text3 = "ThIs Is A tEsT"
print(text3.lower())
print(text3.upper())
print(text3.capitalize())

text4 = "proxy_enabled"
print(text4.replace("proxy","vpn"))

text5 = "Suspiciout file detected"
print("file" in text5)

text6 = "os:linux,arch:x86_64,user:root"
print(text6.split(','))

text7 = "   backtrace   "
print(text7.strip())