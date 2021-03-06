#!/usr/bin/env python
"""
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

import argparse
import fnmatch
import os
from argparse import RawTextHelpFormatter

from macmru import __version__ as ver, _hrule_width
from macmru.globalopts import GlobalOptions
from macmru.parsers.unified import ParseSFL, ParseSFL2, ParseSFL2_FavoriteVolumes
from macmru.parsers.spotlight import SpotlightShortcuts
from macmru.parsers.plists import ParseFinderPlist, ParseLSSharedFileListPlist, ParseMSOffice2011Plist, \
    ParseMSOffice2016Plist, ParseRecentItemsPlist, ParseSidebarlistsPlist


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='\
    Parse the Mac MRU (Most Recently Used) Plist Files \
    \n\n\tMac MRU File Locations: \
    \n\t- /Users/<username>/Library/Preferences/<bundle_id>.LSSharedFileList.plist\
    \n\t- /Users/<username>/Library/Preferences/com.apple.finder.plist\
    \n\t- [10.10-] /Users/<username>/Library/Preferences/com.apple.recentitems.plist\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/<bundle_id>.sfl\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/RecentApplications.sfl\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/RecentDocuments.sfl\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/RecentServers.sfl\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/RecentHosts.sfl\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/<bundle_id>.sfl2\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentApplications.sfl2\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentDocuments.sfl2\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentServers.sfl2\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentHosts.sfl2\
    \n\t- MS Office 2011 - /Users/<username>/Library/Preferences/com.microsoft.office.plist\
    \n\t- MS Office 2016 - /Users/<username>/Library/Containers/com.microsoft.<app>/Data/Library/Preferences/com.microsoft.<app>.securebookmarks.plist \
    \n\t- Spotlight Shortcuts - /Users/<username>/Library/Application Support/com.apple.spotlight.Shortcuts \
    \n\t- [10.12-]/Users/<username>/Library/Preferences/com.apple.sidebarlists.plist \
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.FavoriteVolumes.sfl2\ \
    \n \
    \n\tAuthor:     Sarah Edwards | @iamevltwin | mac4n6.com | oompa@csh.rit.edu \
    \n\tCSV Output: Dan O\'Day     | @4n68r      | 4n68r.com  | d@4n68r.com'
        , prog='macmru.py'
        , formatter_class=RawTextHelpFormatter)
    parser.add_argument("--csv", help="Create CSV output to file provided as parameter")
    parser.add_argument('--blob_hex', action='store_true', help="Include hex dump of Bookmark BLOBs in standard output (can very verbose!)")
    parser.add_argument('--blob_parse_human', action='store_true', help="Parse the BLOB data in human readable format (can very verbose!)")
    parser.add_argument('--blob_parse_raw', action='store_true', help="Parse the BLOB data in raw format (can very verbose!)")
    parser.add_argument('MRU_DIR')
    args = parser.parse_args()

    print "###### MacMRU Parser v{0} ######".format(ver)

    global_options = GlobalOptions(args.MRU_DIR, args.csv,
                                   args.blob_parse_hex,
                                   args.blob_parse_raw,
                                   args.blob_parse_human)

    for root, dirs, filenames in os.walk(global_options.path):
        for f in filenames:
            MRUFile = os.path.join(root, f)
            print "Parsing: " + MRUFile

            if os.path.isfile(MRUFile):
                if f.endswith(".sfl") and not fnmatch.fnmatch(f,'*Favorite*.sfl') and not fnmatch.fnmatch(f,'*Project*.sfl') and not fnmatch.fnmatch(f,'*iCloudItems*.sfl'):
                    ParseSFL(MRUFile, global_options)
                elif f.endswith(".sfl2") and not fnmatch.fnmatch(f,'*Favorite*.sfl2') and not fnmatch.fnmatch(f,'*Project*.sfl2') and not fnmatch.fnmatch(f,'*iCloudItems*.sfl2'):
                    ParseSFL2(MRUFile, global_options)
                elif f.endswith("FavoriteVolumes.sfl2"):
                    ParseSFL2_FavoriteVolumes(MRUFile, global_options)
                elif f.endswith(".LSSharedFileList.plist"):
                    ParseLSSharedFileListPlist(MRUFile, global_options)
                elif f == "com.apple.finder.plist":
                    ParseFinderPlist(MRUFile, global_options)
                elif f == "com.apple.sidebarlists.plist":
                    ParseSidebarlistsPlist(MRUFile, global_options)
                elif f == "com.apple.recentitems.plist":
                    ParseRecentItemsPlist(MRUFile, global_options)
                elif f.endswith(".securebookmarks.plist"):
                    ParseMSOffice2016Plist(MRUFile, global_options)
                elif f == "com.microsoft.office.plist":
                    ParseMSOffice2011Plist(MRUFile, global_options)
                elif f == "com.apple.spotlight.Shortcuts":
                    SpotlightShortcuts(MRUFile, global_options)
                else:
                    print "Invalid MRU file"
            else:
                print "ERROR: Bad file name or path: {0}".format(MRUFile)

            print '=' * _hrule_width
