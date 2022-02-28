# ==================================================================================================================== #
#              _____ ____    _        _      _                           _                                             #
#  _ __  _   _| ____|  _ \  / \      / \    | |    __ _ _   _ _ __   ___| |__   ___ _ __                               #
# | '_ \| | | |  _| | | | |/ _ \    / _ \   | |   / _` | | | | '_ \ / __| '_ \ / _ \ '__|                              #
# | |_) | |_| | |___| |_| / ___ \  / ___ \ _| |__| (_| | |_| | | | | (__| | | |  __/ |                                 #
# | .__/ \__, |_____|____/_/   \_\/_/   \_(_)_____\__,_|\__,_|_| |_|\___|_| |_|\___|_|                                 #
# |_|    |___/                                                                                                         #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Stefan Unrein                                                                                                      #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2021-2022 Stefan Unrein - Endingen, Germany                                                                #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""Start the correct Vivado Version based on version in `*.xpr`file."""
__author__ =    "Stefan Unrein"
__email__ =     "stefan.unrein@gmx.net"
__copyright__ = "2021-2022, Stefan Unrein"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.1.0"
__keywords__ =  ["launcher", "version selector", "xilinx", "vivado"]

import sys
import subprocess
from pathlib import Path
from textwrap import dedent
import time

sub_path_bat  = Path("bin/vivado.bat")
sub_path_vvgl = Path("bin/unwrapped/win64.o/vvgl.exe")
match_line = "<!-- Product Version: Vivado v"


def get_version(file_path):
	if not file_path.exists():
		raise Exception(f"Vivado project file '{file_path}' not found.") from FileNotFoundError(f"File '{file_path}' not found.")

	project_file = file_path.open()

	while True:
		line = project_file.readline()
		if match_line in line:
			break

	version = line.split(match_line)[1]
	version = version.split(" ")[0]
	version = version.split(".")
	version_major = version[0]
	version_minor = version[1]
	project_file.close()
	return str(version_major + "." + version_minor)


def get_vivado_versions(install_path):
	return [directory.name for directory in install_path.iterdir()]


def help():
	script_path = Path(sys.argv[0])
	print(f"Run-Path '{script_path}'")
	print()
	print(dedent("""\
			For using this VivadoManager please bind xpr extension to this executable with:
			* Put this executable into the Vivado installation folder. E.g: c:\\Xilinx\\Vivado\\
			* Change *.xpr association: right-click-> open-width-> VivadoManager.exe
	"""))

def main():
	install_path = Path.cwd()
	if len(sys.argv) > 1:
		inputArg1 = sys.argv[1]
		file_path = Path(inputArg1)

		file_version = get_version(file_path)
		vivado_versions = get_vivado_versions(install_path)

		for version in vivado_versions:
			if file_version == str(version):
				exec_path1 = install_path / file_version / sub_path_vvgl
				exec_path2 = install_path / file_version / sub_path_bat
				a = str(file_path)
				cmd = [str(exec_path1), str(exec_path2), a]
				subprocess.Popen(cmd, cwd=file_path.parent)#, creationflags=subprocess.DETACHED_PROCESS)
				print("")
				print(f"Open Project with Vivado Version {file_version}.")
				time.sleep(2)
				sys.exit(0)
		else:
			vivadoPath = install_path / file_version
			print(f"ERROR: Vivado version {file_version} not available at path '{vivadoPath}'. Please start manually!")
			print("")
			print("Press any key to exit.")
			input()
			sys.exit(-1)

	else:
		help()

		vivado_versions = get_vivado_versions(install_path)
		print(f"Current path '{install_path}' has following Files/Folders in it:")
		for version in vivado_versions:
			print(version)

		print("")
		print("Press any key to exit.")
		input()
		sys.exit(0)


# entry point
if __name__ == "__main__":
		main()
