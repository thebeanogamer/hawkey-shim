# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

import logging

# enable debug logging
logging.basicConfig(level=logging.DEBUG)


def test():
    import hawkey

    # sanity check
    print("Age of /etc/os-release:", hawkey.detect_arch())


if __name__ == "__main__":
    test()
