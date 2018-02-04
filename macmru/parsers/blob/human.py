#!/usr/bin/env python
"""
macmru.parsers.blob.human module

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

import uuid

from mac_alias import Alias
from mac_alias import Bookmark


def BLOBParser_human(blob):  # todo -- major refactoring
    # As described in:
    # http://mac-alias.readthedocs.io/en/latest/bookmark_fmt.html
    # http://mac-alias.readthedocs.io/en/latest/alias_fmt.html
    if args.blob_parse_human == True:  # todo -- move this check to caller logic
        print '-' * _hrule_width
        print "Human Readable Parsed BLOB:"
        try:
            b = Bookmark.from_bytes(blob)
            print "\tBookmark BLOB: Volume Name [0x2010]: \t\t" + b.get(0x2010, default=None)
            print "\tBookmark BLOB: Volume Path [0x2002]: \t\t" + str(b.get(0x2002, default=None))
            print "\tBookmark BLOB: Volume Flags [0x2020]: \t\t" + str(b.get(0x2020, default=None))
            print "\tBookmark BLOB: Volume is Root FS [0x2030]: \t" + str(b.get(0x2030, default=None))
            print "\tBookmark BLOB: Volume UUID [0x2011]: \t\t" + str(b.get(0x2011, default=None))
            print "\tBookmark BLOB: Volume Size [0x2012]: \t\t" + str(b.get(0x2012, default=None))
            print "\tBookmark BLOB: Volume Creation Date [0x2013]: \t" + str(b.get(0x2013, default=None))
            print "\tBookmark BLOB: Volume URL [0x2005]: \t\t" + str(b.get(0x2005, default=None))
            print "\tBookmark BLOB: Volume Bookmark [0x2040]: \t" + str(b.get(0x2040, default=None))
            print "\tBookmark BLOB: Volume Mount Point [0x2050]: \t" + str(b.get(0x2050, default=None))
            print "\tBookmark BLOB: Security Extension [0xf080]: \t" + str(b.get(0xf080, default=None))
            print "\tBookmark BLOB: Security Extension [0xf081]: \t" + str(b.get(0xf081, default=None))
            print ""
            print "\tBookmark BLOB: Target Path [0x1004]: \t\t" + str(b.get(0x1004, default=None))
            print "\tBookmark BLOB: Target CNID Path [0x1005]: \t" + str(b.get(0x1005, default=None))
            print "\tBookmark BLOB: Containing Folder Index [0xc001]:" + str(b.get(0xc001, default=None))
            print "\tBookmark BLOB: Target Creation Date [0x1040]: \t" + str(b.get(0x1040, default=None))
            print "\tBookmark BLOB: Target Flags [0x1010]: \t\t" + str(b.get(0x1010, default=None))
            print "\tBookmark BLOB: Target Filename [0x1020]: \t" + str(b.get(0x1020, default=None))
            print ""
            print "\tBookmark BLOB: Creator Username [0xc011]: \t" + str(b.get(0xc011, default=None))
            print "\tBookmark BLOB: Creator UID [0xc012]: \t\t" + str(b.get(0xc012, default=None))
            print ""

            print "\tBookmark BLOB: Unknown [0x1003]: \t\t" + str(b.get(0x1003, default=None))
            print "\tBookmark BLOB: Unknown [0x1054]: \t\t" + str(b.get(0x1054, default=None))
            print "\tBookmark BLOB: Unknown [0x1055]: \t\t" + str(b.get(0x1055, default=None))
            print "\tBookmark BLOB: Unknown [0x1056]: \t\t" + str(b.get(0x1056, default=None))
            print "\tBookmark BLOB: Unknown [0x1101]: \t\t" + str(b.get(0x1101, default=None))
            print "\tBookmark BLOB: Unknown [0x1102]: \t\t" + str(b.get(0x1102, default=None))
            print "\tBookmark BLOB: TOC Path [0x2000]: \t\t" + str(b.get(0x2000, default=None))
            print "\tBookmark BLOB: Unknown [0x2070]: \t\t" + str(b.get(0x2070, default=None))

            print "\tBookmark BLOB: File Reference Flag [0xd001]: \t" + str(b.get(0xd001, default=None))
            print "\tBookmark BLOB: Creation Options [0xd010]: \t" + str(b.get(0xd010, default=None))
            print "\tBookmark BLOB: URL Length Array [0xe003]: \t" + str(b.get(0xe003, default=None))
            print "\tBookmark BLOB: Localized Name (?) [0xf017]: \t" + str(b.get(0xf017, default=None))
            print "\tBookmark BLOB: Unknown [0xf022]: \t\t" + str(b.get(0xf022, default=None))

            if b.get(0xf020, default=None):
                icon_uuid = uuid.uuid4()
                print icon_uuid

                filename = "ICNS_file_" + str(icon_uuid) + ".icns"

                saveICNS = open(filename, 'w')
                saveICNS.write(b.get(0xf020, default=None).bytes)
                saveICNS.close()

                print "\tBookmark BLOB: ICNS (Icon) File [0xf020]: \tICNS File Saved in: " + filename

        except:
            pass

        try:
            a = Alias.from_bytes(blob)
            print "\tAlias BLOB: Alias Version: \t\t" + str(a.version)
            print "\tAlias BLOB: Target Filename: \t\t" + a.target.filename
            print "\tAlias BLOB: Target File CNID: \t\t" + str(a.target.cnid)
            print "\tAlias BLOB: Target Carbon Path: \t" + a.target.carbon_path
            print "\tAlias BLOB: Target POSIX Path: \t\t" + a.target.posix_path
            print "\tAlias BLOB: Target Creation Date: \t" + str(a.target.creation_date)
            print "\tAlias BLOB: Target Creator Code: \t" + a.target.creator_code
            print "\tAlias BLOB: Target Type Code: \t\t" + a.target.type_code
            print "\tAlias BLOB: Target Folder Name: \t" + a.target.folder_name
            print "\tAlias BLOB: Target Folder CNID: \t" + str(a.target.folder_cnid)
            if a.target.kind == 0:
                print "\tAlias BLOB: Target Kind: \t\tFile"
            elif a.target.kind == 1:
                print "\tAlias BLOB: Target Kind: \t\tFolder"
            print ""
            print "\tAlias BLOB: Levels From: \t\t" + str(a.target.levels_from)
            print "\tAlias BLOB: Levels To: \t\t\t" + str(a.target.levels_to)
            print "\tAlias BLOB: User Home Prefix Length: \t" + str(a.target.user_home_prefix_len)
            print ""
            print "\tAlias BLOB: Volume Name: \t\t" + a.volume.name
            print "\tAlias BLOB: Volume Creation Date: \t" + str(a.volume.creation_date)
            print "\tAlias BLOB: Volume Filesystem Type: \t" + a.volume.fs_type
            print "\tAlias BLOB: Volume Disk Type: \t\t" + str(a.volume.disk_type)
            print "\tAlias BLOB: Volume Attribute Flags: \t" + str(a.volume.attribute_flags)
            print "\tAlias BLOB: Volume Filesystem ID: \t" + str(a.volume.fs_id)
            print ""
            print "\tAlias BLOB: Volume AppleShare Information: \t" + a.volume.appleshare_info
            print "\tAlias BLOB: Volume Driver Name: \t" + str(a.volume.driver_name)
            print "\tAlias BLOB: Volume POSIX Path: \t" + str(a.volume.posix_path)
            print "\tAlias BLOB: Volume Disk Image Alias: \t" + a.volume.disk_image_alias
            print "\tAlias BLOB: Volume Creation Date: \t" + str(a.volume.creation_date)
            print "\tAlias BLOB: Volume Dialup Information: \t" + str(a.volume.dialup_info)
            print "\tAlias BLOB: Volume Network Mount Information: \t" + str(a.volume.network_mount_info)
            print ""
            print "\tAlias BLOB: Extra: \t" + str(a.extra)
            print "\tAlias BLOB: App Info: \t" + str(a.appinfo)
            print "\tAlias BLOB: Apple Share Info - Server: \t" + str(a.AppleShareInfo.server)
            print "\tAlias BLOB: Apple Share Info - User: \t" + str(a.AppleShareInfo.user)
            print "\tAlias BLOB: Apple Share Info - Zone \t" + str(a.AppleShareInfo.zone)
        except:
            pass
        print '-' * _hrule_width
