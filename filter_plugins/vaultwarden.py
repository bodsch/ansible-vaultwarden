# python 3 headers, required if submitting to Ansible

# (c) 2021-2022, Bodo Schulz <bodo@boone-schulz.de>
# Apache (see LICENSE or https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
# import json
import hashlib

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """

    def filters(self):
        return {
            'supported_databases': self.supported_databases,
            'web_vault_directory': self.web_vault_directory,
        }

    def supported_databases(self, data, distribution, os_family):
        """
        """
        display.v(f"supported_databases({data}, {distribution}, {os_family})")

        if distribution == "Debian" and (data.startswith("mysql") or data.startswith("postgresql")):
            display.v("This version of vaultwarden currently only supports one sqlite database!\nPlease change your configuration.")
            return False

        return True

    def web_vault_directory(self, data, web_vault_version):
        """
        """
        display.v(f"web_vault_directory({data}, {web_vault_version})")

        data = data.replace()
