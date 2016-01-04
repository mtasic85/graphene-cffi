# graphene-cffi
python cffi wrapper for graphene

## PIP Install

TODO

## Manual Install

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