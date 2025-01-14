# -*- coding: utf-8 -*-

"""
This file is part of the Reset Card Scheduling add-on for Anki.

Global variables

Copyright: (c) 2018 Glutanimate <https://glutanimate.com/>
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
"""

import sys
import os
from anki.utils import pointVersion

sys_encoding = sys.getfilesystemencoding()

anki21 = pointVersion() > 0

if anki21:
    addon_path = os.path.dirname(__file__)
else:
    addon_path = os.path.dirname(__file__).decode(sys_encoding)