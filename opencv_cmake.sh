#!/bin/bash

# 定义 OpenCV 源代码的路径
OPENCV_SOURCE_DIR=/kaggle/working/opencv_build/opencv  # 确保这个路径正确
OPENCV_BUILD_DIR=/kaggle/working/opencv_build/opencv/build

# 运行 CMake
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr/local \
    -DOPENCV_EXTRA_MODULES_PATH=/kaggle/working/opencv_build/opencv_contrib/modules \
    -DWITH_CUDA=ON \
    -DCUDA_ARCH_BIN="5.0;5.2;6.0;6.1;7.0;7.5" \
    -DCUDA_ARCH_PTX="6.0;6.1" \
    -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda \
    -DPYTHON_EXECUTABLE=/opt/conda/envs/newCondaEnvironment/bin/python \
    -DPYTHON_INCLUDE_DIR=/opt/conda/envs/newCondaEnvironment/include/python3.10 \
    -DPYTHON_LIBRARY=/opt/conda/envs/newCondaEnvironment/lib/libpython3.10.so \
    -S$OPENCV_SOURCE_DIR \
    -B$OPENCV_BUILD_DIR  # 指定构建目录

