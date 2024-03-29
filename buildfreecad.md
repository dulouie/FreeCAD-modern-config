## FreeCAD build options

```bash
cmake -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_ENABLE_CXX_STD="C++17" \
      -DBUILD_QT5=ON \
      -DFREECAD_USE_OCC_VARIANT="Official Version" \
      -DPYTHON_EXECUTABLE=/usr/bin/python3 \
      -DBUILD_ARCH=ON \
      -DBUILD_DRAFT=ON \
      -DBUILD_INSPECTION=OFF \
      -DBUILD_MATERIAL=ON \
      -DBUILD_MESH=ON \
      -DBUILD_MESH_PART=ON \
      -DBUILD_OPENSCAD=OFF \
      -DBUILD_PATH=ON \
      -DBUILD_RAYTRACING=OFF \
      -DBUILD_REVERSEENGINEERING=OFF \
      -DBUILD_ROBOT=OFF \
      -DBUILD_SHIP=OFF \
      -DBUILD_START=OFF \
      -DBUILD_WEB=OFF\
      -DBUILD_COMPLETE=OFF\
      -DBUILD_TEST=OFF\
      -DBUILD_SURFACE=ON\
      -DBUILD_RAYRACING=OFF\
      -DBUILD_POINTS=OFF\
      -DBUILD_PLOT=OFF\
      -DBUILD_IMAGE=OFF\
      -DBUILD_TUX=OFF\
      -DBUILD_FEM=OFF \
      -DBUILD_FEM_NETGEN=OFF ..
  ```


## Solvespace build options

```bash
cmake -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_PYTHON=1 \
      -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 \
      -DPYTHON_INCLUDE_DIR=/usr/include/python3.6/ \
      -DPYTHON_LIBRARY=/usr/lib/python3.6/ ..
```

## Solvespace install on Ubuntu 20.04

* `git clone https://github.com/realthunder/slvs_py`
* `cd slvs_py`
* `sudo apt install docker.io`
* `pip3 install scikit-build`
* `git submodule update --init slvs`
* `./make.sh`
* `pip3 install .`
