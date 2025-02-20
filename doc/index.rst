.. include:: shields.inc

.. image:: _static/logo.svg
   :height: 90 px
   :align: center
   :target: https://GitHub.com/edaa-org/pyEDAA.Launcher

.. raw:: html

    <br>

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:Launcher-github| |SHIELD:svg:Launcher-ghp-doc| |SHIELD:svg:Launcher-gitter|
   |  |SHIELD:svg:Launcher-gha-test| |SHIELD:svg:Launcher-codacy-quality|

.. Disabled shields: |SHIELD:svg:Launcher-src-license| |SHIELD:svg:Launcher-doc-license| |SHIELD:svg:Launcher-pypi-tag| |SHIELD:svg:Launcher-pypi-status| |SHIELD:svg:Launcher-pypi-python| |SHIELD:svg:Launcher-lib-status| |SHIELD:svg:Launcher-codacy-coverage| |SHIELD:svg:Launcher-codecov-coverage| |SHIELD:svg:Launcher-lib-dep| |SHIELD:svg:Launcher-req-status| |SHIELD:svg:Launcher-lib-rank|

.. only:: latex

   |SHIELD:png:Launcher-github| |SHIELD:png:Launcher-ghp-doc| |SHIELD:png:Launcher-gitter|
   |SHIELD:png:Launcher-gha-test| |SHIELD:png:Launcher-codacy-quality|

.. Disabled shields: |SHIELD:png:Launcher-src-license| |SHIELD:png:Launcher-doc-license| |SHIELD:png:Launcher-pypi-tag| |SHIELD:png:Launcher-pypi-status| |SHIELD:png:Launcher-pypi-python| |SHIELD:png:Launcher-lib-status| |SHIELD:png:Launcher-codacy-coverage| |SHIELD:png:Launcher-codecov-coverage| |SHIELD:png:Launcher-lib-dep| |SHIELD:png:Launcher-req-status| |SHIELD:png:Launcher-lib-rank|

The pyEDAA.Launcher Documentation
#################################

**pyEDAA.Launcher** starts the correct Xilinx Vivado version based on the version number written into the ``*.xpr`` file.
If no suitable version was found, an error message is shown.


.. _GOALS:

Main Goals
**********

When opening Xilinx Vivado by double-clicking an ``*.xpr`` file in the Windows Explorer, a default Vivado version is
launched by Windows. In many cases, this is the first Vivado version that was installed on a system, but not the latest
version. Anyhow, in most cases, Windows starts the wrong Vivado version, which leeds to a project upgrade question, or a
rejection, because the project file is too new.

**pyEDAA.Launcher** addresses exactly this problem. It will start the correct Xilinx Vivado installation with correct
working directory settings, if that requested Vivado version is found on the system.

How does it work?
=================

1. Check with which Vivado version was used to save the ``*.xpr`` file.
2. Scan the Xilinx installation directory for available Vivado versions.
3. If a matching version was found, start Vivado and pass the ``*.xpr`` as a parameter.

Differences to opening the ``*.xpr`` from within Vivado GUI?
============================================================

By default, Xilinx Vivado has its working directory in ``AppData``, but the working directory should be in the directory
where the ``*.xpr`` file is located. This is fixed by **pyEDAA.Launcher** as a side effect. Now, Vivado saves log and
journal files to the correct locations.


.. #_usecase:

   Use Cases
   *********

   * Handle multiple parallel Xilinx Vivado installations.


.. _NEWS:

News
****

.. only:: html

   Feb. 2022 - Documentation und Unit Test Enhancements
   ====================================================

.. only:: latex

   .. rubric:: Documentation und Unit Test Enhancements

* Updated documentation.
* Added simple unit tests.


.. only:: html

   Dec. 2021 - Initial Prototype
   =============================

.. only:: latex

   .. rubric:: Initial Prototype

* Development of a simple script to start the correct Vivado installation by reading the version from ``*.xpr`` file.


.. _CONTRIBUTORS:

Contributors
************

* :gh:`Patrick Lehmann <Paebbels>` (Maintainer)
* :gh:`Stefan Unrein <stefanunrein>` (Author)
* :gh:`Unai Martinez-Corral <umarcor>`
* `and more... <https://GitHub.com/VHDL/pyVHDLModel/graphs/contributors>`__


.. _LICENSE:

License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.


.. toctree::
   :hidden:

   Used as a layer of EDA² ➚ <https://edaa-org.github.io/>


.. toctree::
   :caption: Introduction
   :hidden:

   Installation
   Dependency
   Usage


.. raw:: latex

   \part{Main Documentation}

.. #toctree::
   :caption: Main Documentation
   :hidden:

   LanguageModel/index


.. raw:: latex

   \part{References and Reports}

.. toctree::
   :caption: References and Reports
   :hidden:

   Python Class Reference <pyEDAA.Launcher/pyEDAA.Launcher>
   unittests/index
   coverage/index
   Doc. Coverage Report <DocCoverage>
   Static Type Check Report ➚ <typing/index>

.. Coverage Report ➚ <coverage/index>

.. raw:: latex

   \part{Appendix}

.. toctree::
   :caption: Appendix
   :hidden:

   License
   Doc-License
   Glossary
   genindex
   Python Module Index <modindex>
   TODO
