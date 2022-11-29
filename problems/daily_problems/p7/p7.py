"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import unittest


def count_decodings(message: str) -> int:
    num_encodings = [1]
    for i in range(len(message)):
        if i == 0:
            num_encodings.append(1)
        else:
            num_local_encodings = 0
            part = message[i:i+1]
            if int(part) > 0:
                num_local_encodings += num_encodings[i]
            
            part = message[i-1:i+1]
            if int(part) < 27 and part[0] != "0":
                num_local_encodings += num_encodings[i-1]

            num_encodings.append(num_local_encodings)
    return num_encodings[-1]


class Test_P7(unittest.TestCase):

    def test_cases(self):
        assert count_decodings("111") == 3
        assert count_decodings("26") == 2
        assert count_decodings("126") == 3
        assert count_decodings("127") == 2
    