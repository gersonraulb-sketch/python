def cal_subtotal(precios):
    return sum(precios)

def cal_cantidad(productos):
    return len(productos)

def cal_iva(subtotal, iva=0.19):
    return subtotal * iva

def cal_total(subtotal, iva_total):
    return subtotal + iva_total

def iva_producto(precios, iva=0.19):
    return [precio * iva for precio in precios]
print ("-----Factura-----")