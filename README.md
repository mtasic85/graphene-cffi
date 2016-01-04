# graphene-cffi
python cffi wrapper for graphene


## API

API is same as C API. You can find more on: https://github.com/ebassi/graphene


## PIP Install

TODO


## Manual Install

First, you will need *graphene* installed. There is bug in graphene installation steps. *graphene-config.h* is missing, so we need to copy it manually to */usr/include/graphene-1.0*.

On ArchLinux:

```bash
yaourt -S graphene-git
```

```bash
git clone git://github.com/ebassi/graphene
cd graphene
./autogen.sh
make
make check
sudo cp src/graphene-config.h /usr/include/graphene-1.0/
cd ..
sudo rm -r graphene
```

```bash
git clone git@github.com:mtasic85/graphene-cffi.git
cd graphene-cffi
pypy -B graphene_cffi.py
```


## Example

```bash
pypy
```

```python
from graphene import graphene as lib

a = lib.graphene_vec2_alloc()
lib.graphene_vec2_init(a, 1.0, 2.0)
lib.graphene_vec2_free(a)
```
