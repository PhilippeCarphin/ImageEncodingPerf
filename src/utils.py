#!/usr/bin/env python
import os


def get_size_in_bytes(file) -> int:
    size = os.path.getsize(file)
    return size


def get_compression_factor(**kwargs) -> float:
    try:
        after = kwargs['after']
        before = kwargs['before']
    except KeyError:
        raise FileNotFoundError

    factor = 1 - (get_size_in_bytes(after)\
                 /get_size_in_bytes(before))
    return factor
