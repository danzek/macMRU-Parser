#!/usr/bin/env python
"""
macmru.parsers.blob.raw module

Copyright (c) 2017, Station X Labs, LLC
All rights reserved.

Contributions adding CSV output by Dan O'Day <d@4n68r.com>

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Station X Labs, LLC nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL STATION X LABS, LLC BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from mac_alias import Bookmark
from macmru import _hrule_width


def BLOBParser_raw(blob):
    print '-' * _hrule_width
    try:
        b = Bookmark.from_bytes(blob)
        print "Raw Parsed Bookmark BLOB:"
        print b
    except:
        pass

    try:
        a = Alias.from_bytes(blob)
        print "Raw Parsed Alias BLOB:"
        print a.version
        print a.target
        print a.volume
        print a.extra
        print a.appinfo
        print a.AppleShareInfo.server
        print a.AppleShareInfo.user
        print a.AppleShareInfo.zone
    except:
        pass
    print '-' * _hrule_width
