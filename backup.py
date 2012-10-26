# baliwan-backup/backup.py
#
#    A simple commandline backup utility for *nix machines
#
#    Copyright (C) 2012 Aldo Rey Balagulan
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import subprocess
import getopt
import sys

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

class Backup_Session():
    """Backup session class

    Instantiated for every backup session."""
    def backup_menu(self):
        """A menu showing various backup options"""
        print('Something')

    def __init__(self):
        self.home_dir = ''
        self.backup_dir = ''
        self.archive_file = ''

def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "use --help for help"
        return 2

    print('Hello world!')

if __name__ == "__main__":
    sys.exit(main())
