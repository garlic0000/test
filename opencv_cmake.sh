#!/bin/bash

export ENABLE_CONTRIB=1
OPENCV_SOURCE_DIR=/kaggle/working/opencv-python/opencv
OPENCV_BUILD_DIR=/kaggle/working/opencv-python/opencv/build
OPENCV_EXTRA_MODULES_PATH=/kaggle/working/opencv-python/opencv_contrib/modules
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DOPENCV_EXTRA_MODULES_PATH=$OPENCV_EXTRA_MODULES_PATH \
    -DWITH_CUDA=ON \
    -DCUDA_ARCH_BIN='5.0;5.2;6.0;6.1;7.0;7.5' \
    -DCUDA_ARCH_PTX='6.0;6.1' \
    -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda \
    -DBUILD_opencv_python3=ON \
    -DBUILD_opencv_python2=OFF \
    -DPYTHON3_EXECUTABLE=/opt/conda/envs/newCondaEnvironment/bin/python3.10 \
    -DPYTHON_DEFAULT_EXECUTABLE=/opt/conda/envs/newCondaEnvironment/bin/python3.10 \
    -DPYTHON3_INCLUDE_DIR=/opt/conda/envs/newCondaEnvironment/include/python3.10 \
    -DPYTHON3_LIBRARY=/opt/conda/envs/newCondaEnvironment/lib/libpython3.10.so \
    -DOPENCV_PYTHON3_INSTALL_PATH=python \
    -DPYTHON3_LIMITED_API=ON \
    -DINSTALL_CREATE_DISTRIB=ON \
    -DBUILD_opencv_apps=///OFF \
    -DBUILD_opencv_freetype=OFF \
    -DBUILD_SHARED_LIBS=OFF \
    -DBUILD_TESTS=OFF \
    -DBUILD_PERF_TESTS=OFF \
    -DBUILD_DOCS=OFF \
    -DOpenBLAS_INCLUDE_DIR=/usr/include/x86_64-linux-gnu/openblas-pthread \
    -DOpenBLAS_LIB=/usr/lib/x86_64-linux-gnu/libopenblas.so \
    -DBUILD_JPEG=ON \
    -DBUILD_PNG=ON \
    -DBUILD_TIFF=ON \
    -DBUILD_WEBP=ON \
    -DBUILD_OPENEXR=ON \
    -DBUILD_JPEG2K=ON \
    -DWITH_V4L=ON \
    -DWITH_LAPACK=ON \
    -DENABLE_PRECOMPILED_HEADERS=OFF \
    -DWITH_SIMD=ON \
    -S $OPENCV_SOURCE_DIR \
    -B $OPENCV_BUILD_DIR



