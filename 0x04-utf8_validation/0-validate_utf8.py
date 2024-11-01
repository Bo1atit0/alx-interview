#!/usr/bin/python3

# Write a method that determines if a given data set represents a valid UTF-8 encoding.

def validUTF8(data):
    # Step 1: Initialize a variable to track the number of bytes expected
    bytes_expected = 0

    # Step 2: Iterate through each byte in the data
    for byte in data:
        # Step 3: Convert the byte to binary and check the leading bits
        # The & 0xFF ensures we're only working with the least significant 8 bits
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
            # Step 4: Check for continuation bytes (10xxxxxx)
            if (byte & 0xC0) != 0x80:  # Not a continuation byte
                return False  # Invalid byte sequence
            bytes_expected -= 1  # Decrement the count of expected bytes

    # Step 5: If we finished processing and have no more expected bytes, return True
    return bytes_expected == 0
