Linux, MacOS and Windows packages are built for Python3 and require the following dependent packages: pyqt5, ete3, requests. In the case Kssdtree is installed using pip command, these dependencies should be installed automatically. For Windows, it also requires the installation of the gzip tool for sequence decompression and gcc compiler.

# Linux
```
pip install kssdtree
```

# MacOS
```
# Install gcc
brew install gcc

# Install Kssdtree (x86_64 architecture)
pip install kssdtree

# Install Kssdtree (arm64 architecture)
arch -x86_64 $(which python3) -m pip install kssdtree
```

# Windows
```
# Create a virtual environment
conda create --name=kssdtree python=3.x

# Activate the virtual environment
conda activate kssdtree

# Install libpython and m2w64-toolchain 
conda install libpython m2w64-toolchain -c msys2

# Install Kssdtree
pip install kssdtree
```