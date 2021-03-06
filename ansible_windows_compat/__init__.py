from __future__ import absolute_import

__version__ = '0.1.1'

import sys
import types

for module in ('syslog', 'grp', 'pwd'):
    try:
        __import__(module)
    except ImportError:
        __import__('ansible_windows_compat.%s' % module)
        sys.modules[module] = sys.modules['ansible_windows_compat.%s' % module]
