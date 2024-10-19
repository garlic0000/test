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
    # CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
    # Please set them or make sure they are set and tested correctly in the CMake files:
    # CUDA_CUDA_LIBRARY (ADVANCED)
    # linked by target "opencv_cudacodec" in directory /kaggle/working/opencv_build/opencv_contrib/modules/cudacodec
    -DCUDA_CUDA_LIBRARY=/usr/local/cuda/lib64/libcudart.so \
    -DPYTHON3_EXECUTABLE=/opt/conda/envs/newCondaEnvironment/bin/python \
    -DPYTHON3_INCLUDE_DIR=/opt/conda/envs/newCondaEnvironment/include/python3.10 \
    -DPYTHON3_LIBRARY=/opt/conda/envs/newCondaEnvironment/lib/libpython3.10.so \
    # Lapack:                      YES
    -DOpenBLAS_INCLUDE_DIR=/usr/include/x86_64-linux-gnu/openblas-pthread \
    -DOpenBLAS_LIB=/usr/lib/x86_64-linux-gnu/libopenblas.so \
    -DLAPACKE_INCLUDE_DIR=/usr/include \
    -DLAPACKE_LIBRARIES=/usr/lib/x86_64-linux-gnu/liblapacke.so \
    # C/C++:
          #    Built as dynamic libs?:      NO
    -DBUILD_SHARED_LIBS=OFF \
    -S $OPENCV_SOURCE_DIR \
    -B $OPENCV_BUILD_DIR

