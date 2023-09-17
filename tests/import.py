# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

import logging

# enable debug logging
logging.basicConfig(level=logging.DEBUG)


def test():
    import libdnf

    # sanity check
    print("SHA256 of /etc/os-release:", libdnf.utils.checksum_value("sha256", "/etc/os-release"))


if __name__ == "__main__":
    test()
