#!/usr/bin/python3

"""
Check if the given data set represents 
valid UTF-8 encoding.
"""

def validUTF8(data):

    """
    Check if the given data set represents 
    valid UTF-8 encoding.
    """
    bytes_expected = 0

    for byte in data:
        # Check the leading bits to determine the byte length
        if bytes_expected == 0:
            if (byte & 0x80) == 0:  # 1-byte character (0xxxxxxx)
                continue  # No additional bytes expected
            elif (byte & 0xE0) == 0xC0:  # 2-byte character (110xxxxx)
                bytes_expected = 1  # Expect 1 additional byte
            elif (byte & 0xF0) == 0xE0:  # 3-byte character (1110xxxx)
                bytes_expected = 2  # Expect 2 additional bytes
            elif (byte & 0xF8) == 0xF0:  # 4-byte character (11110xxx)
                bytes_expected = 3  # Expect 3 additional bytes
            else:
                return False  # Invalid leading byte
        else:
            # Check for continuation bytes (10xxxxxx)
            if (byte & 0xC0) != 0x80:  # Not a continuation byte
                return False  # Invalid byte sequence
            bytes_expected -= 1  # Decrement the count of expected bytes

    return bytes_expected == 0  # Return True if no bytes are expected left
