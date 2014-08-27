def pad_pkcs7(msg, length):
    pad_len = length - len(msg) % length
    return msg + pad_len * chr(pad_len)
