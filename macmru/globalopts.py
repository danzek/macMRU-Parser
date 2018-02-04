#!/usr/bin/env python
"""
macmru.globalopts module

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

import os
import sys


class GlobalOptions(object):
    def __init__(self, mru_directory_path, csv_output_path, blob_parse_hex, blob_parse_raw, blob_parse_human):
        self.path = self.validate_directory_path(mru_directory_path)
        self.csv_output = False
        self.csv_path = self.set_csv_output_values(csv_output_path)
        self.blob_parse_hex = blob_parse_hex
        self.blob_parse_raw = blob_parse_raw
        self.blob_parse_human = blob_parse_human

    @staticmethod
    def validate_directory_path(directory_path):
        if not directory_path or directory_path is None or not os.path.exists(directory_path):
            print "Invalid directory path (path provided does not exist)"
            sys.exit(1)
        return directory_path

    def set_csv_output_values(self, parameter):
        if parameter and len(parameter.strip()) > 0:
            self.csv_output = True
        return parameter
