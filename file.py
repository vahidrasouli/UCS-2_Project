#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-

import codecs

ucs2_string = '"064506270646062F0647002006270639062A062806270631000A00330039003000360033003000200631064A06270644"'


def decode_ucs2(data, divider):
    """
    Decode first level: hex encrypt, second level: ucs2[utf-16-be] and finally to text[utf8].
    :param data: your input str. sample: [0633064406270645]
    :param divider: your text divider - sample['"'] and finally replace ''.
    :return: finally return encode text[utf8] - sample: [سلام]
    """
    decoded_data = None
    try:
        data = data.replace(divider, '')
        out_data = codecs.decode(data, 'hex').decode('utf-16-be')  # CONVERT UCS2 TO STRING
    except:
        out_data = data
        print("couldn't decode: {}".format(out_data))
    else:
        decoded_data = out_data
    finally:
        return decoded_data


def encode_ucs2(invite):
    """
    Encode text to first level: ucs2[utf-16-be] and finally to hex encrypt.
    :param invite: your input str. sample: [سلام]
    :return: hex encrypt. sample: [0633064406270645]
    """
    decoded_data = None
    try:
        data = codecs.encode(invite, 'utf-16-be')   # CONVERT STRING TO UCS2
        out_data = codecs.encode(data, 'hex')  # CONVERT UCS2 TO HEX
    except:
        out_data = invite
        print("couldn't decode: {}".format(out_data))
    else:
        decoded_data = out_data
    finally:
        return decoded_data


A_out = decode_ucs2(ucs2_string, '"')
print(A_out)

B_out = encode_ucs2(u'سلام')
print(B_out)
