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
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2021-2023 Stefan Unrein - Endingen, Germany                                                                #
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
__copyright__ = "2021-2023, Stefan Unrein"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.1.0"
__keywords__ =  ["launcher", "version selector", "xilinx", "vivado"]

from re import compile as re_compile

from sys import exit, argv
import subprocess
from pathlib import Path
from textwrap import dedent
from time import sleep
from typing import NoReturn, Generator

from pyTooling.Decorators import export


@export
class Program:
	"""Program instance of pyEDAA.Launcher."""

	vivadoBatchfile = Path("bin/vivado.bat")
	vvglWrapperFile = Path("bin/unwrapped/win64.o/vvgl.exe")

	versionLineRegExp = re_compile(r"^<!--\s*Product\sVersion:\s+Vivado\s+v(?P<major>\d+).(?P<minor>\d+)(?:.(?P<patch>\d+))?\s+\(64-bit\)\s+-->")

	_projectFilePath: Path


	def __init__(self, projectFilePath: Path):
		"""Initializer.

		:param projectFilePath: Path to the ``*.xpr`` file.
		:raises Exception: When the given ``*.xpr`` file doesn't exist.
		"""
		if not projectFilePath.exists():
			raise Exception(f"Vivado project file '{projectFilePath}' not found.") \
				from FileNotFoundError(f"File '{projectFilePath}' not found.")

		self._projectFilePath = projectFilePath

	def GetVersion(self) -> str:
		"""Opens an ``*.xpr`` file and returns the Vivado version used to save this file.

		:returns: Used Vivado version to save the given ``*.xpr`` file.
		:raises Exception: When the version information isn't found in the file.
		"""
		with self._projectFilePath.open("r") as file:
			for line in file:
				match = self.versionLineRegExp.match(line)
				if match is not None:
					return f"{match['major']}.{match['minor']}"
			else:
				raise Exception(f"Pattern not found in '{self._projectFilePath}'.")

	@classmethod
	def GetVivadoVersions(self, installPath: Path) -> Generator[str, None, None]:
		"""Scan a given directory for installed Vivado versions.

		:param installPath: Xilinx installation directory.
		:returns: A generator for a sequence of installed Vivado versions.
		"""
		for item in installPath.iterdir():
			if item.is_dir():
				yield item.name

	def StartVivado(self, xilinxInstallationPath: Path, version: str) -> NoReturn:
		"""Start the given Vivado version with an ``*.xpr`` file as parameter.

		:param xilinxInstallationPath: Path to the Xilinx toolchain installations.
		:param version: The Vivado version to start.
		"""
		vivadoInstallationPath = xilinxInstallationPath / version

		vvglWrapperPath = vivadoInstallationPath / self.vvglWrapperFile
		vivadoBatchfilePath = vivadoInstallationPath / self.vivadoBatchfile

		cmd = [str(vvglWrapperPath), str(vivadoBatchfilePath), str(self._projectFilePath)]
		subprocess.Popen(cmd, cwd=self._projectFilePath.parent)  # , creationflags=subprocess.DETACHED_PROCESS)

		print("")
		print(f"Opening project with Vivado {version}.")

		sleep(2)
		exit(0)

	@classmethod
	def PrintHelp(cls, scriptPath: Path) -> None:
		"""Print a help page.

		:param scriptPath: Path to this script.
		"""
		print(dedent(f"""\
			Run-Path '{scriptPath}'

			For using this Launcher, please bind the *.xpr file extension to this executable with:
			* Put this executable into the Vivado installation folder. E.g: C:\\Xilinx\\Vivado\\
			* Change *.xpr association: right-click -> open with -> VivadoManager.exe
		"""))


@export
def main() -> NoReturn:
	"""Entry point function.

	It creates an instance of :class:`Program` and hands over the execution to the OOP world.
	"""
	xilinxInstallationPath = Path.cwd()
	script_path = Path(argv[0])

	if len(argv) == 0:
		Program.PrintHelp(script_path)

		print(f"Current path '{xilinxInstallationPath}' has following folders in it:")
		for version in Program.GetVivadoVersions(xilinxInstallationPath):
			print(version)

		print("")
		print("Press any key to exit.")

		# wait on user interaction
		input()
		exit(0)

	elif len(argv) == 1:
		projectFileArgument = argv[1]
		projectFilePath = Path(projectFileArgument)

		program = Program(projectFilePath)

		try:
			versionFromXPRFile = program.GetVersion()
		except Exception as ex:
			print(f"[ERROR] {ex}")
			exit(1)

		for version in program.GetVivadoVersions(xilinxInstallationPath):
			if version == versionFromXPRFile:
				program.StartVivado(xilinxInstallationPath, versionFromXPRFile)
		else:
			vivadoPath = xilinxInstallationPath / versionFromXPRFile
			print(dedent(f"""\
				ERROR: Vivado version {versionFromXPRFile} not available at path '{vivadoPath}'. Please start manually!

				Press any key to exit.
			"""))

			# wait on user interaction
			input()
			exit(1)


# Entry point
if __name__ == "__main__":
	main()
