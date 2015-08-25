jstream
=======

For processes working on data streams, it's convenient to dump objects
serialized as JSON to disk during a run to avoid buffering results in-mem until
process completion. For this to work, one must be able to deserialize JSON streams.
jstream provides a generator *json_objects* that provides this for python3.

example
-------

```
$ cat example.py 
import jstream
import io

data = io.StringIO('{"val":1}{"val":2}{"val":42}')
for v in jstream.json_objects(data):
    print(v["val"])
$ python3 example.py 
1
2
42
```

