def umrechnung_zeit(zeit, einheit):
    if einheit == "s":
        min = zeit / 60
        h = min / 60
        d = h / 24
        w = d / 7
        m = d / 30.44
        j = m / 12
        return {
            'min': min,
            'h': h,
            'd': d, 
            'w': w,
            'm': m,
            'j': j
        }
    elif einheit == "min":
        s = zeit * 60
        h = zeit / 60
        d = h / 24
        w = d / 7
        m = d / 30.44
        j = m / 12
        return {
            's': s,
            'h': h,
            'd': d,
            'w': w,
            'm': m,
            'j': j
        }
    elif einheit == "h":
        s = zeit * 3600
        min = zeit * 60
        d = zeit / 24
        w = d / 7
        m = d / 30.44
        j = m / 12
        return {
            's': s,
            'min': min,
            'd': d,
            'w': w,
            'm': m,
            'j': j
        }
    elif einheit == "d":
        s = zeit * 86400
        min = zeit * 1440
        h = zeit * 24
        w = zeit / 7
        m = zeit / 30.44
        j = m / 12
        return {
            's': s,
            'min': min,
            'h': h,
            'w': w,
            'm': m,
            'j': j
        }
    elif einheit == "w":
        s = zeit * 604800
        min = zeit * 10080
        h = zeit * 168
        d = zeit * 7
        m = zeit * 30.44 / 12
        j = zeit * 30.44 / 12 / 12
        return {
            's': s,
            'min': min,
            'h': h,
            'd': d,
            'm': m,
            'j': j
        }
    elif einheit == "m":
        s = zeit * 2628002.88
        min = zeit * 43800.048
        h = zeit * 730.001
        d = zeit * 30.44
        w = zeit * 12 / 52
        j = zeit / 12
        return {
            's': s,
            'min': min,
            'h': h,
            'd': d,
            'w': w,
            'j': j
        }
    elif einheit == "j":
        s = zeit * 31536000
        min = zeit * 525600
        h = zeit * 8760
        d = zeit * 365
        w = zeit * 52
        m = zeit * 12
        return {
            's': s,
            'min': min,
            'h': h,
            'd': d,
            'w': w,
            'm': m
        }
    else:
        return "Ungültige Einheit!"


zeit = float(input("Geben Sie den Zeitwert ein: "))
einheit = input("Geben Sie die Einheit der Zeit ein (s/min/h/d/w/m/j): ")

ergebnis = umrechnung_zeit(zeit, einheit)

for einheit, wert in ergebnis.items():
    print(f'{wert:.2f} {einheit}')