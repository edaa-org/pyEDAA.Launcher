<p align="center">
  <a title="edaa-org.github.io/pyEDAA.Launcher" href="https://edaa-org.github.io/pyEDAA.Launcher"><img height="80px" src="doc/_static/logo.svg"/></a>
</p>

[![Sourcecode on GitHub](https://img.shields.io/badge/pyEDAA-Launcher-ffca28.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=ff8f00)](https://GitHub.com/edaa-org/pyEDAA.Launcher)
[![Documentation](https://img.shields.io/website?longCache=true&style=flat-square&label=edaa-org.github.io%2FpyEDAA.Launcher&logo=GitHub&logoColor=fff&up_color=blueviolet&up_message=Read%20now%20%E2%9E%9A&url=https%3A%2F%2Fedaa-org.github.io%2FpyEDAA.Launcher%2Findex.html)](https://edaa-org.github.io/pyEDAA.Launcher/)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-4db797.svg?longCache=true&style=flat-square&logo=gitter&logoColor=e8ecef)](https://gitter.im/hdl/community)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/actions/workflow/status/edaa-org/pyEDAA.Launcher/Pipeline.yml?longCache=true&style=flat-square&label=Build%20and%20Test&logo=GitHub%20Actions&logoColor=FFFFFF)](https://GitHub.com/edaa-org/pyEDAA.Launcher/actions/workflows/Pipeline.yml)
[![Codacy - Quality](https://img.shields.io/codacy/grade/83936550d5094383bb89bb117c0abbfe?longCache=true&style=flat-square&logo=Codacy)](https://app.codacy.com/gh/edaa-org/pyEDAA.Launcher)

<!--
[![Sourcecode License](https://img.shields.io/pypi/l/pyEDAA.Launcher?longCache=true&style=flat-square&logo=Apache&label=code)](LICENSE.md)
[![Documentation License](https://img.shields.io/badge/doc-CC--BY%204.0-green?longCache=true&style=flat-square&logo=CreativeCommons&logoColor=fff)](LICENSE.md)

[![PyPI](https://img.shields.io/pypi/v/pyEDAA.Launcher?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pyEDAA.Launcher/)
![PyPI - Status](https://img.shields.io/pypi/status/pyEDAA.Launcher?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyEDAA.Launcher?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)

[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyEDAA.Launcher?longCache=true&style=flat-square&logo=Libraries.io&logoColor=fff)](https://libraries.io/github/edaa-org/pyEDAA.Launcher)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/83936550d5094383bb89bb117c0abbfe?longCache=true&style=flat-square&logo=Codacy)](https://app.codacy.com/gh/edaa-org/pyEDAA.Launcher)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/edaa-org/pyEDAA.Launcher?longCache=true&style=flat-square&logo=Codecov)](https://codecov.io/gh/edaa-org/pyEDAA.Launcher)

[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/pyEDAA.Launcher?longCache=true&style=flat-square&logo=GitHub)](https://GitHub.com/edaa-org/pyEDAA.Launcher/network/dependents)
[![Requires.io](https://img.shields.io/requires/github/edaa-org/pyEDAA.Launcher?longCache=true&style=flat-square)](https://requires.io/github/EDAA-ORG/pyEDAA.Launcher/requirements/?branch=main)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyEDAA.Launcher?longCache=true&style=flat-square)](https://libraries.io/github/edaa-org/pyEDAA.Launcher/sourcerank)
-->

**pyEDAA.Launcher** starts the correct Xilinx Vivado version based on the version number written into the ``*.xpr`` file.
If no suitable version was found, an error message is shown.

# Main Goals

When opening Xilinx Vivado by double-clicking an ``*.xpr`` file in the Windows Explorer, a default Vivado version is
launched by Windows. In many cases, this is the first Vivado version that was installed on a system, but not the latest
version. Anyhow, in most cases, Windows starts the wrong Vivado version, which leeds to a project upgrade question, or a
rejection, because the project file is too new.

**pyEDAA.Launcher** addresses exactly this problem. It will start the correct Xilinx Vivado installation with correct
working directory settings, if that requested Vivado version is found on the system.

## How does it work?

1. Check with which Vivado version was used to save the ``*.xpr`` file.
2. Scan the Xilinx installation directory for available Vivado versions.
3. If a matching version was found, start Vivado and pass the ``*.xpr`` as a parameter.

## Differences to opening the ``*.xpr`` from GUI?
 
By default, Xilinx Vivado has its working directory in ``AppData``, but the working directory should be in the directory
where the ``*.xpr`` file is located. This is fixed by **pyEDAA.Launcher** as a side effect. Now, Vivado saves log and
journal files to the correct locations.


> # Installation
> * Copy the executable from the releases to the Vivado installation Path. For me its `C:\Xilinx\Vivado\`.
> * In this Path you should see the installation-folders of all Vivado Versions. E.g: 2018.3, 2019.1, ...
> * Change File-association: Right click on `*.xpr` -> open with -> choose another app -> and select the `VivadoLauncher.exe`
> * That's it.

> Note for Xilinx: Feel free to include this in the next release to stop this version madness. Please inform us then.

# Contributors

* [Stefan Unrein](https://GitHub.com/stefanunrein) (Maintainer)
* [Patrick Lehmann](https://GitHub.com/Paebbels) (Maintainer)
* [Unai Martinez-Corral](https://GitHub.com/umarcor) (Maintainer)
* [and more...](https://GitHub.com/edaa-org/pyEDAA.Launcher/graphs/contributors)

# License

This Python package (source code) licensed under [Apache License 2.0](LICENSE.md).  
The accompanying documentation is licensed under [Creative Commons - Attribution 4.0 (CC-BY 4.0)](doc/Doc-License.rst).

-------------------------
SPDX-License-Identifier: Apache-2.0
