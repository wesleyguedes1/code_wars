def converter(r, g, b):
    r = int(r)
    g = int(g)
    b = int(b)
    rgb = [r, g, b]
    hex = ''
    value = 0 
    for i in range(3):
        value = rgb[i] // 16
        hex+= str(value)
        value = rgb[i] / 16 - value
        value*=16
        value = int(value)
        hex+=str(value)
    print(hex)

converter(220, 20, 60)