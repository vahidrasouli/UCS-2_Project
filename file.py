#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = str('"064506270646062F0647002006270639062A062806270631000A00330039003000360033003000200631064A06270644"'\
	.replace('"', '').decode("hex"))

def decode_ucs2(invite):
    decoded_data = None
    try:
        out_data = unicode(invite, "utf-16-be").encode("utf8")  # CONVERT UCS2 TO STRING
    except:
        out_data = invite
        print "couldn't decode: {}".format(out_data)
    else:
        decoded_data = out_data
    finally:
        return decoded_data

def encode_ucs2(invite):
    out_data = unicode(invite).encode("utf-16-be").encode("hex")  # CONVERT STRING TO UCS2
    print out_data

A_out = decode_ucs2(a)
print A_out
encode_ucs2(u'سلام')