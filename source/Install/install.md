# Installation Tutorial
Linux, MacOS and Windows packages are built for Python3 and require the following dependent packages: pyqt5, ete3, requests. In the case Kssdtree is installed using pip command, these dependencies should be installed automatically. For Windows, it also requires the installation of the gzip tool for sequence decompression and gcc compiler.

### Table of contents
1. [Linux](#1-Linux)
2. [MacOS](#2-MacOS)
3. [Windows](#3-Windows)

# 1 Linux
```
pip install kssdtree
```
# 2 MacOS
```
# install gcc
brew install gcc
# install kssdtree (x86_64)
pip install kssdtree
# install kssdtree (arm64)
arch -x86_64 $(which python3) -m pip install kssdtree
```
# 3 Windows
```
# create virtual environment
conda create --name=kssdtree python=3.x
# activate virtual environment
conda activate kssdtree
# install libpython and m2w64-toolchain 
conda install libpython m2w64-toolchain -c msys2
# install kssdtree
pip install kssdtree
```






