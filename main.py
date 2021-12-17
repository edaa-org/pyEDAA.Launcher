import sys
import os
import subprocess
from pathlib import Path

# accept command line arguments
inputArg1 = sys.argv[1]
install_path = Path("C:\Xilinx\Vivado")
sub_path = ["bin", "vivado.bat"]

# print('inputArg1: ', inputArg1)

file_path = Path(inputArg1)


def get_version(file_path):
    if not file_path.exists():
        raise Exception(f"Vivado project file '{file_path!s}' not found.") from FileNotFoundError(f"File '{file_path!s}' not found.")

    project_file = file_path.open()
    match_line = "<!-- Product Version: Vivado v"

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
    my_list = os.listdir(install_path)
    return my_list



file_version = get_version(file_path)
# print(file_version)

vivado_versions = get_vivado_versions(install_path)
for version in vivado_versions:
    if file_version == str(version):
        # print("matching version:", file_version)
        exec_path = os.path.join(install_path, file_version)
        for i in sub_path:
            exec_path = os.path.join(exec_path, i)
        cmd = [exec_path, inputArg1]
        # print(cmd)

        subprocess.Popen(cmd)
        exit()

print("ERROR: Vivado Version " + file_version + " not available at path '" + os.path.join(install_path, file_version) + "'. Please start manually!")
exit(-1)
