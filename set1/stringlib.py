import base64
import unittest


def decode_hex(bstring):
    if isinstance(bstring, str):
        bstring = bytes(bstring, encoding='ascii')
    return base64.b16decode(bstring, casefold=True)


def encode_hex(bstring):
    if isinstance(bstring, str):
        bstring = bytes(bstring, encoding='ascii')
    return base64.b16encode(bstring)


def decode_base64(string):
    return base64.standard_b64decode(string, validate=True)


def encode_base64(string):
    return base64.standard_b64encode(string)


def xor_hexes(hex1, hex2):
    dec1 = decode_hex(hex1)
    dec2 = decode_hex(hex2)
    xored = (a^b for a, b in zip(dec1, dec2))
    return encode_hex(bytearray(xored)).lower()