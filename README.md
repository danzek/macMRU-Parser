# macMRU-Parser  ![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)
Python script to parse the Most Recently Used (MRU) plist files on macOS into a more human friendly format.

## Usage:
`python macMRU.py [-h] [--csv] [--blob_hex] [--blob_parse_human] [--blob_parse_raw] MRU_DIR`

## Output Options:
* `--csv` - Specify path to tab-delimited output file (csv file will not include binary/hex nor "raw" output)
* `--blob_hex` - Extract the binary BLOB Bookmark data
* `--blob_parse_raw` - Parse the BLOB data in a raw format
* `--blob_parse_human` - Parse the BLOB data in a (mostly) human-friendly format (can be used with `--csv`)

## Dependencies:      
- ccl_bplist.py v0.21: https://github.com/cclgroupltd/ccl-bplist (not available in PyPI/pip)
- Additional requirements in [`requirements.txt`](requirements.txt) (`pip install -r requirements.txt`)
  - hexdump.py v3.3: https://pypi.python.org/pypi/hexdump
  - mac_alias v2.0.6: https://pypi.python.org/pypi/mac_alias

## Related Information:
https://www.mac4n6.com/blog/2016/7/10/new-script-macmru-most-recently-used-plist-parser
