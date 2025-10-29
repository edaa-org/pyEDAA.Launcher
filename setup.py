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
# Copyright 2021-2025 Stefan Unrein - Endingen, Germany                                                                #
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
"""Package installer for 'Start the correct Vivado Version based on version in ``*.xpr`` file.'."""
from setuptools          import setup

from pathlib             import Path
from pyTooling.Packaging import DescribePythonPackageHostedOnGitHub, DEFAULT_CLASSIFIERS

gitHubNamespace =        "edaa-org"
packageName =            "pyEDAA.Launcher"
packageDirectory =       packageName.replace(".", "/")
packageInformationFile = Path(f"{packageDirectory}/__init__.py")

setup(
	**DescribePythonPackageHostedOnGitHub(
		packageName=packageName,
		description="Start the correct Vivado Version based on version in '*.xpr' file.",
		gitHubNamespace=gitHubNamespace,
		sourceFileWithVersion=packageInformationFile,
		classifiers=list(DEFAULT_CLASSIFIERS) + [
			"Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
		],
		developmentStatus="beta",
		pythonVersions=("3.11", "3.12", "3.13", "3.14"),
		consoleScripts={
			"pyedaa-launcher": "pyEDAA.Launcher:main"
		},
		dataFiles={
			packageName: ["py.typed"]
		}
	)
)
