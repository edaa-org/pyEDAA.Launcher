<p align="center">
  <a title="edaa-org.github.io/pyEDAA.Launcher" href="https://edaa-org.github.io/pyEDAA.Launcher"><img height="80px" src="doc/_static/logo.svg"/></a>
</p>

[![Sourcecode on GitHub](https://img.shields.io/badge/pyEDAA-Launcher-ffca28.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=ff8f00)](https://GitHub.com/edaa-org/pyEDAA.Launcher)
[![Documentation](https://img.shields.io/website?longCache=true&style=flat-square&label=edaa-org.github.io%2FpyEDAA.Launcher&logo=GitHub&logoColor=fff&up_color=blueviolet&up_message=Read%20now%20%E2%9E%9A&url=https%3A%2F%2Fedaa-org.github.io%2FpyEDAA.Launcher%2Findex.html)](https://edaa-org.github.io/pyEDAA.Launcher/)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-4db797.svg?longCache=true&style=flat-square&logo=gitter&logoColor=e8ecef)](https://gitter.im/hdl/community)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/workflow/status/edaa-org/pyEDAA.Launcher/Pipeline/main?longCache=true&style=flat-square&label=Build%20and%20Test&logo=GitHub%20Actions&logoColor=FFFFFF)](https://GitHub.com/edaa-org/pyEDAA.Launcher/actions/workflows/Pipeline.yml)
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


# Main Goals
If one is using the Xilinx Vivado IDE, you will know that you can't just open the xpr project file with a double click if you have installed more then one Vivado version. This is because Xilinx has no Launcher which is checking the version of the project and passing the xpr to the correct Vivado Version. This project addresses exactly this problem.

1. Check with which Vivado Version a xpr was created
1. and pass the xpr to the correct Version.
1. Now you can open every xpr just with a simple double click!
1. It behaves exactly as you would open the xpr directly with Vivado itself. **With one exeption**: 
   The working dir in Vivado is set to the xpr path and not to AppData, like it should be!

# Installation
* Copy the executable from the releases to the Vivado installation Path. For me its `C:\Xilinx\Vivado\`.
* In this Path you should see the installation-folders of all Vivado Versions. E.g: 2018.3, 2019.1, ...
* Change File-association: Right click on `*.xpr` -> open with -> choose another app -> and select the `VivadoLauncher.exe`
* That's it.

Note for Xilinx: Feel free to include this in the next release to stop this version madness. Please inform us then.

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