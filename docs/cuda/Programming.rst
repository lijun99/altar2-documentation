#################
Programming Guide
#################
 (For Model Developers)


Introduction
============


Data Types and Structures
=========================

Configurable properties
-----------------------

pyre.properties.array
pyre.properties.bool
pyre.properties.catalog
pyre.properties.complex
pyre.properties.converter
pyre.properties.date
pyre.properties.decimal
pyre.properties.dict
pyre.properties.dimensional
pyre.properties.envpath
pyre.properties.envvar
pyre.properties.facility
pyre.properties.float
pyre.properties.identity
pyre.properties.inet
pyre.properties.int
pyre.properties.istream
pyre.properties.list
pyre.properties.normalizer
pyre.properties.object
pyre.properties.ostream
pyre.properties.path
pyre.properties.paths
pyre.properties.property
pyre.properties.set
pyre.properties.str
pyre.properties.strings
pyre.properties.time
pyre.properties.tuple
pyre.properties.uri
pyre.properties.uris
pyre.properties.validator


Matrix/Vector
-------------
The Matrix/Vector is based on GSL Matrix/Vector.

GSL matrix (size1, size2) -> (rows, cols) and is row-major.

Convert altar array to gsl_vector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    array = altar.properties.array(default=(0, 0, 0,0))
    gvector = altar.vector(shape=4)
    for index, value in enumerate(array): gvector[index] = value

Basic matrix/vector operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    mat = altar.matrix(shape=(rows, cols)) # create a new matrix with dimension rows x cols (row-major)
    mat.zero() # initialize 0 to each element
    mat.fill(number) #
    mat_clone = mat.clone() #
    mat1.copy(mat2)


Altar framework
===============

Application
-----------

An altar application, as an instance of `altar.shells.application`, is the executor of altar programs and the organizer of other altar components. The four primary components of an altar application are

- job : to config the run environment, such as number of tasks per host, number of hosts, number of gpus
- controller: to control the adaptive annealing process, the default is `altar.bayesian.Annealer.Annealer`
- model: a user-defined package specifying parameters, data, the forward model, as well as other necessary components to construct prior, likelihood, and posterior probabilities pursuant to the Bayes' theorem
- rng: the random number generator, the default is gsl.rng.

Other altar components include

- distributions: common pdf functions used for prior distributions
- norms: the distance functions used for computing likelihood, such as L2-norm.



Controller
----------

An altar controller is a Markov-Chain Monte-Carlo sampler. The current controller is based on the CATMIP, or an adaptive annealing algorithm. Here, we assign a `beta` power to the likelihood and vary `beta` from 0 to 1 in steps.

- scheduler: control how beta varies, the default is COV scheduler.
- sampler: Metropolis sampler for each beta step, as a burn-in process
- worker: sequential, mpi, cuda annealing methods
- Coolingstep:
-

Altar application configuration file `.pfg`
===========================================

Most configurations are loaded by the configuration file (for most classes, current __init__.py method takes no input parameters).


Writing Python bindings for C/C++ modules
=========================================

Let's use an example of vector copy .
Define in ``copy.h`` the

::

        // vector_copy
        extern const char * const vector_copy__name__;
        extern const char * const vector_copy__doc__;
        PyObject * vector_copy(PyObject *, PyObject *);

The source code ``copy.cc``

::

    PyObject *
    vector_copy(PyObject *, PyObject * args) {
    // the arguments
    PyObject * sourceCapsule;
    PyObject * destinationCapsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(
                                  args, "O!O!:vector_copy",
                                  &PyCapsule_Type, &destinationCapsule,
                                  &PyCapsule_Type, &sourceCapsule
                                  );
    // if something went wrong
    if (!status) return 0;
    // bail out if the source capsule is not valid
    if (!PyCapsule_IsValid(sourceCapsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid vector capsule for source");
        return 0;
    }
    // bail out if the destination capsule is not valid
    if (!PyCapsule_IsValid(destinationCapsule, capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid vector capsule for destination");
        return 0;
    }

    // get the vectors
    gsl_vector * source =
        static_cast<gsl_vector *>(PyCapsule_GetPointer(sourceCapsule, capsule_t));
    gsl_vector * destination =
        static_cast<gsl_vector *>(PyCapsule_GetPointer(destinationCapsule, capsule_t));
    // copy the data
    gsl_vector_memcpy(destination, source);

    // return None
    Py_INCREF(Py_None);
    return Py_None;
    }





