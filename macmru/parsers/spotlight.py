#!/usr/bin/env python
"""
macmru.parsers.spotlight module

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

import plistlib


def SpotlightShortcuts(MRUFile, opts):
    try:
        plistfile = plistlib.readPlist(MRUFile)
        print "[Spotlight Shortcuts are shown with a UTC timestamp]"
        for n, item in enumerate(plistfile):
            print "    [Shortcut: '" + item + "']"
            try:
                print "        Display Name: \t\t" + plistfile[item]["DISPLAY_NAME"]
            except:
                print "        Display Name: No 'DISPLAY_NAME' Key"

            try:
                print "        Last Used Timestamp: \t" + str(plistfile[item]["LAST_USED"])
            except:
                print "        Last Used Timestamp: No 'LAST_USED' Key"

            try:
                print "        URL: \t\t\t" + plistfile[item]["URL"]
            except:
                print "        URL: No 'URL' Key"
    except:
        print "Cannot open file: " + MRUFile
