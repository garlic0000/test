#!/bin/bash

OPENCV_SOURCE_DIR=/kaggle/working/opencv_build/opencv
OPENCV_BUILD_DIR=/kaggle/working/opencv_build/opencv/build
OPENCV_EXTRA_MODULES_PATH=/kaggle/working/opencv_build/opencv_contrib/modules
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr/local \
    -DOPENCV_EXTRA_MODULES_PATH=$OPENCV_EXTRA_MODULES_PATH \
    -DWITH_CUDA=ON \
    -DCUDA_ARCH_BIN="5.0;5.2;6.0;6.1;7.0;7.5" \
    -DCUDA_ARCH_PTX="6.0;6.1" \
    -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda \
    -DCUDA_CUDA_LIBRARY=/usr/local/cuda/lib64/libcudart.so \
    -DCUDA_LIBRARY=/usr/local/cuda/lib64/stubs/libcuda.so \
    -DPYTHON3_EXECUTABLE=/opt/conda/envs/newCondaEnvironment/bin/python \
    -DPYTHON3_INCLUDE_DIR=/opt/conda/envs/newCondaEnvironment/include/python3.10 \
    -DPYTHON3_LIBRARY=/opt/conda/envs/newCondaEnvironment/lib/libpython3.10.so \
    -DOpenBLAS_INCLUDE_DIR=/usr/include/x86_64-linux-gnu \
    -DLAPACKE_INCLUDE_DIR=/usr/include \
    -DBUILD_SHARED_LIBS=OFF \
    -DWITH_SIMD=ON \
    -S $OPENCV_SOURCE_DIR \
    -B $OPENCV_BUILD_DIR

