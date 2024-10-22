#!/bin/bash

export ENABLE_CONTRIB=1

export CMAKE_ARGS="-DCMAKE_BUILD_TYPE=Release
    -DWITH_CUDA=ON
    -DCUDA_ARCH_BIN='5.0;5.2;6.0;6.1;7.0;7.5'
    -DCUDA_ARCH_PTX='6.0;6.1'
    -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda
    -DOpenBLAS_INCLUDE_DIR=/usr/include/x86_64-linux-gnu/openblas-pthread
    -DOpenBLAS_LIB=/usr/lib/x86_64-linux-gnu/libopenblas.so
    -DBUILD_JPEG=ON
    -DBUILD_PNG=ON
    -DBUILD_TIFF=ON
    -DBUILD_WEBP=ON
    -DBUILD_OPENEXR=ON
    -DBUILD_JPEG2K=ON
    -DBUILD_OPENJPEG=ON
    -DWITH_SIMD=ON"

