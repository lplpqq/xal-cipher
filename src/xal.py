BYTES_SCHEME = b"\x030\xc3\xa9\x087\xc2\xb0\xc2\x94\x0e-\xc2\xb3x\xc2\x9d\xc3\xbb\xc3\x8bf\xc3\xae\xc3\xa2\xc3\x80\x0eZ\xc3\xa2\xc2\xa9\x04\xc2\x9cS\xc3\x91\xc3\xa4`\xc2\x88\xc2\x9c\xc3\x81'".decode()


def decode_xal(xal: str) -> str:
    decoded_data = ''
    for i, j in enumerate(range(0, len(xal), 2)):
        hex_value = xal[j:j + 2]
        decoded_int = int(hex_value, 16)
        xor_value = ord(BYTES_SCHEME[i % len(BYTES_SCHEME)]) ^ decoded_int
        decoded_data += chr(xor_value)
    return decoded_data


def encode_data(data: str) -> str:
    encrypted_xal = ''
    for i, char in enumerate(data):
        xor_value = ord(char) ^ ord(BYTES_SCHEME[i % len(BYTES_SCHEME)])
        hex_value = "{:02x}".format(xor_value)
        encrypted_xal += hex_value
    return encrypted_xal
