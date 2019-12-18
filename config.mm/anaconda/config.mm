# file config.mm

conda.dir = /opt/anaconda3

# gsl
gsl.dir = ${conda.dir}

# mpi
mpi.dir = ${conda.dir}
mpi.binpath = ${conda.dir}/bin
mpi.flavor = openmpi
mpi.executive = mpirun

# hdf5
hdf5.dir = ${conda.dir}

# postgresql
libpq.dir = ${conda.dir}

# python3
python.version = 3.7
python.dir = ${conda.dir}
python.incpath = ${conda.dir}/include/python3.7m
python.libpath = ${conda.dir}/lib

# numpy
numpy.dir = ${conda.dir}/lib/python3.7/site-packages/numpy/core

# cuda; may be different for different systems
cuda.dir = /usr/local/cuda
cuda.incpath = ${cuda.dir}/include
cuda.libpath = ${cuda.dir}/lib64
cuda.libraries := cudart cublas curand cusolver

# pyre
pyre.dir = ${HOME}/tools/pyre
pyre.libraries := pyre journal ${if ${value cuda.dir}, pyrecuda}

# end of file
