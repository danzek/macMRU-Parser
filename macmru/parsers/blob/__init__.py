#!/usr/bin/env python
"""
macmru.parsers.blob package

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

from collections import OrderedDict


# =====================================================#
# Human readable helper functions and global variables #
# =====================================================#

_blob_bookmark_human_readable_report_offsets = OrderedDict([
    ("Volume Name", 0x2010),
    ("Volume Path", 0x2002),
    ("Volume Flags", 0x2020),
    ("Volume is Root FS", 0x2030),
    ("Volume UUID", 0x2011),
    ("Volume Size", 0x2012),
    ("Volume Creation Date", 0x2013),
    ("Volume URL", 0x2005),
    ("Volume Bookmark", 0x2040),
    ("Volume Mount Point", 0x2050),
    ("Security Extension (1)", 0xf080),
    ("Security Extension (2)", 0xf081),
    ("Target Path", 0x1004),
    ("Target CNID Path", 0x1005),
    ("Containing Folder Index", 0xc001),
    ("Target Creation Date", 0x1040),
    ("Target Flags", 0x1010),
    ("Target Filename", 0x1020),
    ("Creator Username", 0xc011),
    ("Creator UID", 0xc012),
    ("Unknown (1)", 0x1003),
    ("Unknown (2)", 0x1054),
    ("Unknown (3)", 0x1055),
    ("Unknown (4)", 0x1056),
    ("Unknown (5)", 0x1101),
    ("Unknown (6)", 0x1102),
    ("TOC Path", 0x2000),
    ("Unknown (7)", 0x2070),
    ("File Reference Flag", 0xd001),
    ("Creation Options", 0xd010),
    ("URL Length Array", 0xe003),
    ("Localized Name (?)", 0xf017),
    ("Unknown (8)", 0xf022)
])

_blob_alias_human_readable_report_fields = OrderedDict([
    ("Alias Version", "a.version"),
    ("Target Filename", "a.target.filename"),
    ("Target File CNID", "a.target.cnid"),
    ("Target Carbon Path", "a.target.carbon_path"),
    ("Target POSIX Path", "a.target.posix_path"),
    ("Target Creation Date", "a.target.creation_date"),
    ("Target Creator Code", "a.target.creator_code"),
    ("Target Type Code", "a.target.type_code"),
    ("Target Folder Name", "a.target.folder_name"),
    ("Target Folder CNID", "a.target.folder_cnid"),
    ("Target Kind", "'Folder' if a.target.kind else 'File'"),  # assumes type(a.target.kind) == bool
    ("Levels From", "a.target.levels_from"),
    ("Levels To", "a.target.levels_to"),
    ("User Home Prefix Length", "a.target.user_home_prefix_len"),
    ("Volume Name", "a.volume.name"),
    ("Volume Creation Date", "a.volume.creation_date"),
    ("Volume Filesystem Type", "a.volume.fs_type"),
    ("Volume Disk Type", "a.volume.disk_type"),
    ("Volume Attribute Flags", "a.volume.attribute_flags"),
    ("Volume Filesystem ID", "a.volume.fs_id"),
    ("Volume AppleShare Information", "a.volume.appleshare_info"),
    ("Volume Driver Name", "a.volume.driver_name"),
    ("Volume POSIX Path", "a.volume.posix_path"),
    ("Volume Disk Image Alias", "a.volume.disk_image_alias"),
    ("Volume Creation Date", "a.volume.creation_date"),
    ("Volume Dialup Information", "a.volume.dialup_info"),
    ("Volume Network Mount Information", "a.volume.network_mount_info"),
    ("Extra", "a.extra"),
    ("App Info", "a.appinfo"),
    ("Apple Share Info - Server", "a.AppleShareInfo.server"),
    ("Apple Share Info - User", "a.AppleShareInfo.user"),
    ("Apple Share Info - Zone", "a.AppleShareInfo.zone")
])
