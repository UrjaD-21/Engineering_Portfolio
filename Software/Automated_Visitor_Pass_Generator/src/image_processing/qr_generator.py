import qrcode

def generate_qr(data, size):
    qr = qrcode.make(data)
    qr = qr.resize((size, size))
    return qr
