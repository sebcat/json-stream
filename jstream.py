#!/usr/bin/env python3
import json

WHITESPACE='\t\n\r '
BUFSIZE=8192

def json_objects(readable):
    """ Generator producing a stream of JSON objects from a file-like object

    Should only be used for lists or objects, as literal values may be split 
    between read buffers and decoded as separate values (e.g., 1234 -> 12, 34 
    if 1234 ends upp crossing a buffer boundary)
    """
    dec = json.JSONDecoder()
    buf = readable.read(BUFSIZE)
    while len(buf) > 0:
        buf = buf.lstrip(WHITESPACE)
        has_obj = True
        try:
            obj, off = dec.raw_decode(buf)
        except ValueError:
            has_obj = False
        if has_obj:
            yield obj
            buf = buf[off:]
        buf += readable.read(BUFSIZE)
