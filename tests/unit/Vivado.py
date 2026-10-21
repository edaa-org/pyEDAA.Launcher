# ==================================================================================================================== #
#              _____ ____    _        _      _                           _                                             #
#  _ __  _   _| ____|  _ \  / \      / \    | |    __ _ _   _ _ __   ___| |__   ___ _ __                               #
# | '_ \| | | |  _| | | | |/ _ \    / _ \   | |   / _` | | | | '_ \ / __| '_ \ / _ \ '__|                              #
# | |_) | |_| | |___| |_| / ___ \  / ___ \ _| |__| (_| | |_| | | | | (__| | | |  __/ |                                 #
# | .__/ \__, |_____|____/_/   \_\/_/   \_(_)_____\__,_|\__,_|_| |_|\___|_| |_|\___|_|                                 #
# |_|    |___/                                                                                                         #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2026 Patrick Lehmann - Bötzingen, Germany                                                             #
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
"""Unit tests for Vivado."""
from pathlib              import Path
from shutil               import rmtree
from unittest             import TestCase

from pyTooling.Versioning import YearReleaseVersion

from pyEDAA.Launcher      import Program


class VivadoInstallation(TestCase):
	_PROJECT_DIRECTORY = Path.cwd()
	_XILINX_DIRECTORY =  _PROJECT_DIRECTORY / "tests" / "xilinx"

	@classmethod
	def setUpClass(cls) -> None:
		print()

		installations = (
			"Vivado/2023.1",
			"Vivado/2023.2",
			"Vivado/2024.1",
			"2025.1/Vivado"
		)
		print(f"Creating '{cls._XILINX_DIRECTORY}' ... ", end="")
		try:
			cls._XILINX_DIRECTORY.mkdir(parents=True)
			print("[ok]")
		except FileExistsError:
			print("[skip]")

		for installation in installations:
			installationDirectory = cls._XILINX_DIRECTORY / installation
			print(f"  {installation}", end="")
			try:
				installationDirectory.mkdir(parents=True)
				print("[ok]")
			except FileExistsError:
				print("[skip]")

	@classmethod
	def tearDownClass(cls) -> None:
		print()
		print(f"Removing '{cls._XILINX_DIRECTORY}' ... ", end="")
		try:
			rmtree(cls._XILINX_DIRECTORY)
			print("[ok]")
		except FileNotFoundError:
			print("[skip]")

	def test_Iterate(self) -> None:
		expectedVersions = [
			YearReleaseVersion(2023, 1),
			YearReleaseVersion(2023, 2),
			YearReleaseVersion(2024, 1),
			YearReleaseVersion(2025, 1)
		]
		versions = [version for version, _ in Program.GetVivadoVersions(self._XILINX_DIRECTORY)]
		versions.sort()

		self.assertListEqual(expectedVersions, versions)


class ReadXPRFile(TestCase):
	def test_ExtractVersionFromXPRFile(self) -> None:
		xprFilePath = Path("tests/StopWatch.xpr")
		program = Program(xprFilePath)
		version = program.GetVersion()

		self.assertEqual("2021.2", version)
