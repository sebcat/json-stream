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
    while True:
        buf = buf.lstrip(WHITESPACE)
        try:
            obj, off = dec.raw_decode(buf)
            yield obj
            buf = buf[off:]
        except ValueError:
            chunk = readable.read(BUFSIZE)
            if len(chunk) == 0:
                break
            else:
                buf += chunk
