#!/usr/bin/env python3
import argparse
import json

import base58


def base58_to_uintarray(key):
    byte_array = base58.b58decode(key)
    return [int(b) for b in byte_array]


if __name__ == "__main__":
    flagp = argparse.ArgumentParser()
    flagp.add_argument("private_key", help="base58 private key")
    flagp.add_argument(
        "-o", "--output", required=False, help="output file path", action="store"
    )
    args = flagp.parse_args()

    uint_array = base58_to_uintarray(args.private_key)
    if args.output:
        with open(args.output, "w") as fd:
            fd.write(json.dumps(uint_array))
    else:
        print(json.dumps(uint_array))
