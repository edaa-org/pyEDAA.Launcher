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
# Copyright 2021-2026 Stefan Unrein - Endingen, Germany                                                                #
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
__author__ =    "Stefan Unrein, Patrick Lehmann"
__email__ =     "paebbels@gmail.com"
__copyright__ = "2021-2026, Stefan Unrein"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.2.2"
__keywords__ =  ["launcher", "version selector", "amd", "xilinx", "vivado"]

from colorama   import init as colorama_init, Fore as Foreground
from pathlib    import Path
from re         import compile as re_compile
from subprocess import Popen
from sys        import exit, argv, stdout
from textwrap   import dedent
from time       import sleep
from typing     import NoReturn, Generator, Tuple

from pyTooling.Decorators import export
from pyTooling.Versioning import YearReleaseVersion


@export
class Program:
	"""Program instance of pyEDAA.Launcher."""

	_vivadoBatchfile = Path("bin/vivado.bat")
	_vvglWrapperFile = Path("bin/unwrapped/win64.o/vvgl.exe")

	_vivadoVersionPattern = re_compile(r"\d+\.\d+(\.\d+)?")
	_versionLinePattern =   re_compile(r"^<!--\s*Product\sVersion:\s+Vivado\s+v(?P<major>\d+).(?P<minor>\d+)(?:.(?P<patch>\d+))?\s+\(64-bit\)\s+-->")

	_projectFilePath: Path

	def __init__(self, projectFilePath: Path) -> None:
		"""Initializer.

		:param projectFilePath: Path to the ``*.xpr`` file.
		:raises Exception:      When the given ``*.xpr`` file doesn't exist.
		"""
		if not projectFilePath.exists():
			raise Exception(f"Vivado project file '{projectFilePath}' not found.") \
				from FileNotFoundError(f"File '{projectFilePath}' not found.")

		self._projectFilePath = projectFilePath

	def GetVersion(self) -> YearReleaseVersion:
		"""Opens an ``*.xpr`` file and returns the Vivado version used to save this file.

		:returns:          Used Vivado version to save the given ``*.xpr`` file.
		:raises Exception: When the version information isn't found in the file.
		"""
		with self._projectFilePath.open("r", encoding="utf-8") as file:
			for line in file:
				match = self._versionLinePattern.match(line)
				if match is not None:
					return YearReleaseVersion(year=int(match['major']), release=int(match['minor']))
			else:
				raise Exception(f"Pattern not found in '{self._projectFilePath}'.")

	@classmethod
	def GetVivadoVersions(cls, xilinxInstallPath: Path) -> Generator[Tuple[YearReleaseVersion, Path], None, None]:
		"""Scan a given directory for installed Vivado versions.

		:param xilinxInstallPath: Xilinx installation directory.
		:returns:                 A generator for a sequence of installed Vivado versions.
		"""
		for directory in xilinxInstallPath.iterdir():
			if directory.is_dir():
				if directory.name == "Vivado":
					for version in directory.iterdir():
						if cls._vivadoVersionPattern.match(version.name):
							yield YearReleaseVersion.Parse(version.name), version
				elif cls._vivadoVersionPattern.match(directory.name):
					yield YearReleaseVersion.Parse(directory.name), directory / "Vivado"

	def StartVivado(self, vivadoInstallationPath: Path) -> None:
		"""Start the given Vivado version with an ``*.xpr`` file as parameter.

		:param vivadoInstallationPath: Path to the Xilinx toolchain installations.
		:param version: The Vivado version to start.
		"""
		vvglWrapperPath =     vivadoInstallationPath / self._vvglWrapperFile
		vivadoBatchfilePath = vivadoInstallationPath / self._vivadoBatchfile

		cmd = [str(vvglWrapperPath), str(vivadoBatchfilePath), str(self._projectFilePath)]
		Popen(cmd, cwd=self._projectFilePath.parent)


@export
def printHeadline() -> None:
	"""
	Print the programs headline.

	.. code-block::

	   ================================================================================
	                                   pyEDAA.Launcher
	   ================================================================================

	"""
	print(f"{Foreground.MAGENTA}{'=' * 80}{Foreground.RESET}")
	print(f"{Foreground.MAGENTA}{'pyEDAA.Launcher':^80}{Foreground.RESET}")
	print(f"{Foreground.MAGENTA}{'=' * 80}{Foreground.RESET}")


@export
def printVersion() -> None:
	"""
	Print author(s), copyright notice, license and version.

	.. code-block::

	   Author:    Jane Doe
	   Copyright: ....
	   License:   MIT
	   Version:   v2.1.4

	"""
	print(f"Author:    {__author__} ({__email__})")
	print(f"Copyright: {__copyright__}")
	print(f"License:   {__license__}")
	print(f"Version:   {__version__}")


@export
def printCLIOptions() -> None:
	"""
	Print accepted CLI arguments and CLI options.
	"""
	print(f"{Foreground.LIGHTBLUE_EX}Accepted argument:{Foreground.RESET}")
	print("  <path to xpr file>   AMD/Xilinx Vivado project file")
	print()
	print(f"{Foreground.LIGHTBLUE_EX}Accepted options:{Foreground.RESET}")
	print("  --help               Show a help page.")
	print("  --version            Show tool version.")
	print("  --list               List available Vivado versions.")


@export
def printSetup(scriptPath: Path) -> None:
	"""
	Print how to setup pyEDAA.Launcher.

	:param scriptPath: Path to this script.
	"""
	print(dedent(f"""\
		For using this {scriptPath.stem}, please associate the '*.xpr' file extension to
		this executable.

		{Foreground.LIGHTBLUE_EX}Setup steps:{Foreground.RESET}
		* Copy this executable into the Xilinx installation directory.
		  Example: C:\\Xilinx\\
		* Set '*.xpr' file association:
		  1. right-click on any existing '*.xrp' file in Windows Explorer
		  2. open with
		  3. {scriptPath}""")
		)


@export
def printAvailableVivadoVersions(xilinxInstallationPath: Path) -> None:
	"""
	Print a list of discovered Xilinx Vivado installations.

	:param xilinxInstallationPath: Directory were Xilinx software is installed.
	"""
	print(dedent(f"""\
		{Foreground.LIGHTBLACK_EX}Detecting Vivado installations in Xilinx installation directory '{xilinxInstallationPath}' ...{Foreground.RESET}

		{Foreground.LIGHTBLUE_EX}Detected Vivado versions:{Foreground.RESET}""")
	)
	for version, installDirectory in Program.GetVivadoVersions(xilinxInstallationPath):
		print(f"* {Foreground.GREEN}{version}{Foreground.RESET}  -> {installDirectory}")


@export
def waitForReturnKeyAndExit(exitCode: int = 0) -> NoReturn:
	"""
	Ask the user to press Return. Afterwards exit the program with ``exitcode``.

	:param exitCode: Exit code when returning to caller.
	"""
	print()
	print(f"{Foreground.CYAN}Press Return to exit.{Foreground.RESET}")
	input()  # wait on user interaction
	exit(exitCode)


@export
def main() -> NoReturn:
	"""Entry point function.

	It creates an instance of :class:`Program` and hands over the execution to the OOP world.
	"""
	colorama_init()

	scriptPath = Path(argv[0])
	xilinxInstallationDirectory = scriptPath.parent

	printHeadline()
	if (argc := len(argv)) == 1:
		printVersion()
		print()
		print(f"{Foreground.RED}[ERROR] No argument or option provided.{Foreground.RESET}")
		print()
		printSetup(scriptPath)
		print()
		printAvailableVivadoVersions(xilinxInstallationDirectory)
		print()
		printCLIOptions()
		waitForReturnKeyAndExit(2)
	elif argc == 2:
		if (option := argv[1]) == "--help":
			print(dedent(f"""\
				{scriptPath.stem} launches the matching Vivado installation based on the Vivado
				version used to save an '*.xpr' file""")
						)
			print()
			printCLIOptions()
			exit(0)
		elif option == "--version":
			printVersion()
			exit(0)
		elif option == "--list":
			printAvailableVivadoVersions(xilinxInstallationDirectory)
			exit(0)
		else:
			try:
				program = Program(Path(option))
				versionFromXPRFile = program.GetVersion()

				for version, vivadoInstallationDirectory in program.GetVivadoVersions(xilinxInstallationDirectory):
					if version == versionFromXPRFile:
						print(f"Using Vivado {Foreground.GREEN}{version}{Foreground.RESET} to open '{program._projectFilePath.parent.as_posix()}/{Foreground.CYAN}{program._projectFilePath.name}{Foreground.RESET}'.")
						print()
						program.StartVivado(vivadoInstallationDirectory)

						i = 3
						print(f"Closing in {i}", end="")
						stdout.flush()
						for i in range(i - 1, 0, -1):
							sleep(1)
							print(f"\x1b[1D{i}", end="")
							stdout.flush()
						sleep(1)
						print()
						exit(0)
				else:
					print(dedent(f"""\
						{Foreground.RED}[ERROR] Vivado version {versionFromXPRFile} not available.{Foreground.RESET}

						Please start manually!""")
					)
					printAvailableVivadoVersions(xilinxInstallationDirectory)
					waitForReturnKeyAndExit(2)

			except Exception as ex:
				print(f"{Foreground.RED}[ERROR]    {ex}{Foreground.RESET}")
				if ex.__cause__ is not None:
					print(f"{Foreground.YELLOW}Caused by: {ex.__cause__}{Foreground.RESET}")
				waitForReturnKeyAndExit(1)
	else:
		printHeadline()
		print(f"{Foreground.RED}[ERROR] Too many arguments.{Foreground.RESET}")
		print()
		printCLIOptions()
		waitForReturnKeyAndExit(2)


# Entry point
if __name__ == "__main__":
	main()
