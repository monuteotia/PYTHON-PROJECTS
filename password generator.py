def help():
    import string
    import secrets
    alfa = string.ascii_letters + string.hexdigits + string.punctuation
    pas = ''.join(secrets.choice(alfa) for i in range(8))
    return pas

print("Can I help you to make your password")
v = input(("   y/n    =>    "))
if v=="y":
    print("Your password is :",help())
else:
    print("ok bye")