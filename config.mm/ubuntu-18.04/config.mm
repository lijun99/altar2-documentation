
# gsl
gsl.dir = /usr
gsl.incpath = /usr/include
gsl.libpath = /usr/lib/x86_64-linux-gnu

# mpi
mpi.dir = /usr/lib/x86_64-linux-gnu/openmpi/
mpi.binpath = /usr/bin
mpi.incpath = /usr/lib/x86_64-linux-gnu/openmpi/include
mpi.libpath = /usr/lib/x86_64-linux-gnu/openmpi/lib
mpi.flavor = openmpi
mpi.executive = mpirun

# hdf5
hdf5.dir = /usr
hdf5.incpath = /usr/include
hdf5.libpath = /usr/lib/x86_64-linux-gnu

# postgresql
libpq.dir = /usr
libpq.incpath = /usr/include/postgresql
libpq.libpath = /usr/lib/x86_64-linux-gnu

# openblas
openblas.dir = /usr
openblas.libpath = /usr/lib/x86_64-linux-gnu

# python3
python.version = 3.6
python.dir = /usr
python.binpath = /usr/bin
python.incpath = /usr/include/python3.6m
python.libpath = /usr/lib/python3.6

# numpy
numpy.dir = /usr/lib/python3/dist-packages/numpy/core

# cuda
cuda.dir = /usr/local/cuda
cuda.binpath = /usr/local/cuda/bin
cuda.incpath = /usr/local/cuda/include
cuda.libpath = /usr/local/cuda/lib64 /usr/lib/x86_64-linux-gnu/
cuda.libraries := cuda cudart cublas curand cusolver


# pyre
pyre.dir = ${HOME}/tools/pyre
pyre.libraries := pyre journal ${if ${value cuda.dir}, pyrecuda}

# end of file
