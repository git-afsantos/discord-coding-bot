# SPDX-License-Identifier: MIT
# Copyright © 2023 André Santos

###############################################################################
# Imports
###############################################################################

import discodebot

###############################################################################
# Tests
###############################################################################


def test_import_was_ok():
    assert True


def test_pkg_has_version():
    assert hasattr(discodebot, '__version__')
    assert isinstance(discodebot.__version__, str)
    assert discodebot.__version__ != ''
