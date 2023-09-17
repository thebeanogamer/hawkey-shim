# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

import logging

# enable debug logging
logging.basicConfig(level=logging.DEBUG)


def test():
    import dnf

    # sanity check
    print("Age of /etc/os-release:", dnf.util.file_age("/etc/os-release"))


if __name__ == "__main__":
    test()
