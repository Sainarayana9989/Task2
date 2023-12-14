def palin(s):
    str = s.replace(' ','')
    str=str[ ::-1]
    return s==str

print(palin('aia'))

