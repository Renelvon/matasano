def pad_pkcs7(msg, length):
    pad_len = length - len(msg) % length
    return msg + pad_len * chr(pad_len)


class InvalidPadding(Exception):
    pass


def strip_pad(plaintext):
    pad_cnt = ord(plaintext[-1])
    for i in range(1, pad_cnt):
        if ord(plaintext[-(i + 1)]) != pad_cnt:
            raise InvalidPadding
    return plaintext[:-pad_cnt]
