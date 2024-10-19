cmake -D CMAKE_BUILD_TYPE=Release \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
      -D WITH_CUDA=ON \
      -D CUDA_ARCH_BIN="5.0;5.2;6.0;6.1;7.0;7.5" \
      -D CUDA_ARCH_PTX="6.0;6.1" \
      -D CUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda \
      -D PYTHON_EXECUTABLE=/opt/conda/envs/newCondaEnvironment/bin/python \
      -D PYTHON_INCLUDE_DIR=/opt/conda/envs/newCondaEnvironment/include/python3.10 \
      -D PYTHON_LIBRARY=/opt/conda/envs/newCondaEnvironment/lib/libpython3.10.so \
      ..
