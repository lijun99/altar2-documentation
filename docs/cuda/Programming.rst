
.. _Programming Guide:

#################
Programming Guide
#################


Introduction
============

This guide aims to help developers to write their own models for AlTar.



Code Organization
=================

New models can be added to the ``altar/models`` directory. We recommend the AlTar/pyre convention to organize the source code inside the directory.

The simplest model can be constructed all by Python. The minimum set of files includes, e.g., for a new model named ``regression``,

::

  altar/models/regression # root
  ├── CMakeLists.txt # cmake script
  ├── bin  # binary commands
  │   └── regression # command to invoke AlTar simulation for this model
  ├── regression # python scripts
  │   ├── __init__.py # export modules at the package level
  │   ├── meta.py.in # metadata includes version/copyright/authors ...
  │   └── Regression.py # the main Python program
  └── examples # (optional) provide examples to users
      ├── regression.pfg # an example of the configuration file
      └── synthetic # a directory includes data files for the example

If C/C++/Fortran routines are needed, which are wrapped as extension modules in Python, these additional files can be arranged as

::

  altar/models/regression # root
  ├── lib # C/C++/Fortran routines compiled as shared libraries
  │   └── libregression # compiled to INSTALL_DIR/lib/libregression.so(dylib)
  │      ├── version.h # version header file
  │      ├── version.cc  # version code
  │      ├── Source.h  # C++ source code header file
  │      ├── Source.icc  # C++ source code header include file for static methods/variables
  │      └── Source.cc # # C++ source code
  ├── ext  # CPython extension modules
  │   └── regression # compiled to regression.cpython-{}.so
  │      ├── capsules.h # Python Capsule (pass pointers of C++ objects) definitions
  │      ├── regression.cc  # extension module definition
  │      ├── source.h  # header file for wrappers
  │      ├── source.cc  # CPython wrappers for C/C++/Fortran routines/classes
  │      ├── metadata.h  # metadata header file includes version ...
  │      └── metadata.cc # # metadata source file includes version ...
  └── regression # python scripts
      └── ext  # to host the regression.cpython-{}.so product
         └── __init__.py # export extension modules at the package level

GPU/CUDA models can be constructed in the same fashion. The following files will be added,

::

  altar/models/regression # root
  ├── lib # C/C++/Fortran routines compiled as shared libraries
  │   └── libcudaregression # compiled to INSTALL_DIR/lib/libcudaregression.so(dylib)
  │      ├── version.h # version header file
  │      ├── version.cc  # version code
  │      ├── Source.h  # CUDA source code header file
  │      ├── Source.icc  # CUDA source code header include file for static methods/variables
  │      └── Source.cu # # CUDA source code
  ├── ext  # CPython extension modules
  │   └── cudaregression # compiled to cudaregression.cpython-{}.so
  │      ├── capsules.h # Python Capsule (pass pointers of C++ objects) definitions
  │      ├── regression.cc  # extension module definition
  │      ├── source.h  # header file for wrappers
  │      ├── source.cc  # CPython wrappers for C/C++/Fortran routines/classes
  │      ├── metadata.h  # metadata header file includes version ...
  │      └── metadata.cc # # metadata source file includes version ...
  └── regression # python scripts
      ├──cuda #
      │  ├── __init__.py # export modules at the package level
      │  ├── meta.py.in # metadata includes version/copyright/authors ...
      │  └── cudaRegression.py # the main Python program
      └── ext  # to host the regression.cpython-{}.so product
         └── __init__.py # export cuda extension modules as well

Additional compile/build scripts are also required, for either CMake or (new) MM build tools.

For ``CMAKE``, in addition to the ``CMakeLists.txt`` file under the model directory, these files need to be added to modified,

::

  altar # root directory
  ├── .cmake # for cmake
  │   └── altar_regression.cmake # functions to build packages/lib/modules/driver(bin)
  └── CMakeLists.txt # to include the new model

For (new) MM build tool,

::

  altar # root directory
  └── .mm # for cmake
     ├── regression.def # new model configurations
     └── altar.mm # to include the new model

Details for the above files will be illustrated by specific examples in the following sections.


Bayesian Model
================

An AlTar application can be broadly separated into two parts, the MCMC framework for Bayesian statistics and a Bayesian Model who is responsible for calculating the prior/data likelihood/posterior probabilities for a given set of parameters :math:`\theta`.

Specifically, a Model is required to provide the methods as listed in the :altar_src:`Model <altar/altar/models/Model.py>` protocol,

.. code-block:: python

    # services for the simulation controller
    @altar.provides
    def initialize(self, application):
        """
        Initialize the state of the model given a {problem} specification
        """

    @altar.provides
    def initializeSample(self, step):
        """
        Fill {step.theta} with an initial random sample from my prior distribution.
        """

    @altar.provides
    def priorLikelihood(self, step):
        """
        Fill {step.prior} with the likelihoods of the samples in {step.theta} in the prior
        distribution
        """

    @altar.provides
    def dataLikelihood(self, step):
        """
        Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
        data. This is what is usually referred to as the "forward model"
        """

    @altar.provides
    def posteriorLikelihood(self, step):
        """
        Given the {step.prior} and {step.data} likelihoods, compute a generalized posterior using
        {step.beta} and deposit the result in {step.post}
        """

    @altar.provides
    def likelihoods(self, step):
        """
        Convenience function that computes all three likelihoods at once given the current {step}
        of the problem
        """

    @altar.provides
    def verify(self, step, mask):
        """
        Check whether the samples in {step.theta} are consistent with the model requirements and
        update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones
        """

    # notifications
    @altar.provides
    def top(self, annealer):
        """
        Notification that a β step is about to start
        """

    @altar.provides
    def bottom(self, annealer):
        """
        Notification that a β step just ended
        """

and these methods are called by the AlTar framework at respective places. (``@altar.provides`` decorated methods are similar to C++ virtual functions for which the derived classes must declare).

- ``initialize`` is to initialize various parameters and settings of the Model, as also being required for other components in AlTar. It takes ``application``, the root component, as inputs in order to pull information from other components, e.g. obtaining the number of chains and the processor information (cpu/gpu) from the ``job`` component.

- Most other methods take :altar_src:`CoolingStep (step) <altar/altar/bayesian/CoolingStep.py>` as inputs, which stores the process data including

  - the parameters being sampled, :math:`\theta`, in 2d array ``shape=(samples, parameters)``,
  - the prior, data likelihood, and posterior probability densities for samples, each in 1d vector ``shape=samples``.

  Note that AlTar processes a batch of samples (number of Markov Chains) in parallel.

- ``initializeSample`` is to generate random samples from a prior distribution in the beginning of the simulations. Samples can also be loaded from pre-calculated values using the ``preset`` prior.

- ``priorLikelihood`` computes the prior probability densities from the given prior distribution(s). During the simulation, when new proposed samples fall outside of the support of certain ranged distributions, the density is 0 and therefore the proposals are invalid. Because AlTar uses the logarithmic value of the densities, we need an extra ``verify`` method to check the ranged priors.

- ``dataLikelihood`` computes the data likelihood. It performs

  - the forward modeling, calculating the data predictions from :math:`\theta`,
  - computes the residual between data predictions and observations,
  - and return the data likelihood with a given Norm function (e.g., L2-Norm).

- ``posteriorLikelihood`` computes the posterior probability densities from prior and data likelihood. For transitional `posterior` distributions in annealing schemes, it is simply :math:`prior + \beta * data`.

- ``top`` and ``bottom`` methods are hooks for developers to insert model-specific procedures before or after each annealing step. For example, for models considering model uncertainties, these methods are the places to invoke computing Cp and updating the covariance matrix (Cd+Cp).

Many models may share the same procedures to compute the prior, data likelihood, and posterior; they may differ in forward modeling. We offer some templates to simplify the model development.


Model with the BayesianL2 template
===================================

A :altar_src:`BayesianL2 <altar/altar/models/BayesianL2.py>` template assumes a fixed structure of contiguous parameter sets and the data observations with L2-norm. With these assumptions, all required model methods are pre-defined while developers are only required to define a ``forwardModel`` method which performs the forward modeling. This template offers the easiest approach to write a new model.

We use the linear regression model to demonstrate how to construct a Bayesian model with the BayesianL2 template in the following. The linear regression model fits a group of data :math:`(x_n, y_n)` with a linear function

.. math::

    y = slope \times x + intercept + \epsilon_i

where ``slope`` and ``intercept`` are parameters to be sampled while :math:`\epsilon_i` are random noises. The Python program for this example is available at :altar_src:`models/regression/regression/Linear.py <models/regression/regression/Linear.py>`.

Parametersets(psets)
--------------------

In the linear regression model, :math:`\theta = [slope, intercept]`. In principle, slope and intercept could have different prior distributions. Each set of parameters with the same prior distribution is defined as a (contiguous) parameter set. :math:`\theta` can therefore be described as a parametersets (psets) with each parameter set arranged sequentially and contiguously in 1d vector (or columns in batched samples). In Python, ``psets`` is a ``dict`` with a collection of ``contiguous`` parameter set objects. We further define a list ``psets_list`` to assure the orders of parameter sets in :math:`\theta` (it is also useful in model ensembles to select model-relevant parameter sets from the global ``psets``).

A description of ``psets`` in the configuration file ``linear.pfg`` appears as

::

        ; parameter sets
        psets_list = [slope, intercept]
        psets:
            slope = contiguous
            intercept = contiguous

            slope:
                count = 1
                prep = uniform
                prep.support = (0, 5)
                prior = uniform
                prior.support = (0, 5)

            intercept:
                count = 1
                prep = uniform
                prep.support = (0, 5)
                prior = uniform
                prior.support = (0, 5)

where slope and intercept are each described as a ``contiguous`` parameter set and each set has its own ``prep`` (to initialize random samples and ``prior`` (for verify and prior probability) distributions.

We use the static earthquake inversion as another example, where the sampling parameters are dip-slip (:math:`D_d`), strike-slip (:math:`D_s`) displacements for :math:`N`-patches, and if necessary the inSAR ramping parameters (:math:`R`). Each is described by a ``contiguous`` parameter set and assembled as a ``psets``. (Each row of) :math:`\theta` is therefore :math:`(D_{d1}, D_{d2}, \ldots, D_{dN}, D_{s1}, D_{s2}, \ldots, D_{sN}, R_1, R_2, \ldots)`. The order of sets :math:`D_d`, :math:`D_s` and :math:`R` can be switched as long as it is consistent with the forward modeling, e.g., the Green's functions. If you want to use different priors for strike slips in different patches, you may separate :math:`D_s` into several parameter sets.

With ``psets``, various methods related to parameters, including ``initializeSamples``, ``verify`` and ``priorLikelihood``, are pre-defined in  BayesianL2 template. Users only need to specify its included parameter sets in the configuration file.

Data observations(dataobs) with L2-norm
----------------------------------------

L2-norm is recommended for models which need to incorporate various uncertainties. The data likelihood is computed as

.. math::

   \log (Data Likelihood) = -\frac 12 \left[ d_{pred} - d_{obs}\right] C_{\chi}^{-1} \left[ d_{pred} - d_{obs}\right]^T + C

where :math:`d_{pred} = G(\theta)` are the data predictions from the forward model, :math:`d_{pred}` the data observations, :math:`C_\chi` the covariance matrix capturing data (Cd) and/or model(Cp) uncertainties, and :math:`C` a normalization constant depending on the determinant of :math:`C_\chi`.

In BayesianL2 template, the observed data are described by a ``dataobs`` object with L2-norm. It includes

- observed data points (``dataobs.dataobs``) in 1d vector with ``shape=observations``, ``observations`` is the number of observed data points;
- data covariance matrix (``dataobs.cd``) in 2d array with ``shape=(observations, observations)``. (If only constant diagonal elements are available, use ``cd_std`` instead).

``dataobs`` is responsible for

- loading the data observations (:math:`d_{obs}`) and the data covariance (:math:`C_d`),
- calculating the Cholesky decomposition of the inverse :math:`C_d` and saving it in ``dataobs``,
- when called by the ``model.dataLikelihood``, computing the L2-norm (likelihood) between data predictions and observations with L2-norm,
- for Cp models, updating the covariance matrix :math:`C_\chi = C_d + C_p` (though still denoted as :math:`C_d`),
- when needed, merging the covariance matrix with data in ``initialize``, as controlled by a flag ``dataobs.merge_cd_with_data=True/False``. This procedure improves performance greatly for models when the covariance matrix can also be merged with model parameters, such as the Green's functions in the linear model, by avoiding repeating the matrix-vector (or matrix-matrix for batched) multiplication.

For the linear regression model, the data points :math:`(x_n, y_n)` don't fit perfectly into the ``dataobs`` description. Instead, we treat :math:`y_n` as data observations and :math:`x_n` as model parameters. We need to initialize them with the ``initialize`` method,

.. code-block:: python

    @altar.export
    def initialize(self, application):
        """
        Initialize the state of the model
        """

        # call the super class initialization
        super().initialize(application=application)
        # super class method loads and initializes dataobs with y_n

        # model specific initialization after superclass
        # grab data
        self.x = self.loadFile(self.x_file)
        self.y = self.dataobs.dataobs

        ... ...

so that ``x`` and ``y`` are now accessible by the forward modeling.

Their descriptions in the configuration file ``linear.pfg`` appear as, e.g.,

.. code-block:: none

        case = synthetic ; input directory
        dataobs:
            observations = 200
            data_file = y.txt
            cd_std = 1.e-2
        x_file = x.txt

where :math:`(x_n, y_n)` are separated into two text files (raw binary and H5 input files are also supported by the ``loadFile`` function).

With L2-norm ``dataobs``, the ``dataLikelihood`` method can be defined straightforwardly: it calls a ``forwardModel`` defined
for a specific model and with the data predictions or residuals it calls dataobs' norm method to compute the likelihood.

Forward modeling
-----------------

As shown above, with ``psets`` and ``dataobs``, the BayesianL2 template only requires developers to write a ``forwardModel`` or ``forwardModelBatched`` method to compute the data predictions from a given set of :math:`\theta`.

Developers have the options to

- Choose whether to implement ``forwardModelBatched`` or ``forwardModel``.
  The ``forwardModelBatched`` computes the data predictions for all samples. A pre-defined version iterates over all samples (rows of :math:`\theta`) and calls ``forwardModel`` which computes the data predictions for one sample. The batched mode sometimes improves the speed, e.g., in the linear model, one may use the matrix-matrix product (a routine commonly optimized for both CPU and GPU) to compute :math:`d = G \theta`. In this case, a customized ``forwardModelBatched`` method may be defined to override the one pre-defined in BayesianL2.

- Choose to simply compute the data predictions or return the residuals between predictions and observations, depending on the performance or convenience;
  This is controlled by a flag ``return_residual = True/False`` which can be specified either in ``model.initialize`` code or in the configuration file ``model.return_residual=True/False``.

- How to incorporate the data covariance (Cd). If the model uncertainties (Cp) are also considered, please refer to the examples such as ``models/seismic/staticCp``.

For the linear regression model, the simplest implementation is to use the ``forwardModel`` method for a single set of parameters, and the code appears as

.. code-block:: python

    def forwardModel(self, theta, prediction):
        """
        Forward Model
        :param theta: sampling parameters for one sample
        :param prediction: data prediction or residual (prediction - observation)
        :return:
        """

        # grab the parameters from theta

        slope = theta[0]
        intercept = theta[1]

        # calculate the residual between data prediction and observation
        size = self.observations
        for i in range(size):
            prediction[i] = slope * self.x[i] + intercept - self.y[i]

        # all done
        return self

we also need to specify the flag ``return_residual = True`` accordingly.

We can also use the batch method ``forwardModelBatched``, where we can construct a 2d array ``G=[[x1, x2, ..., xN], [1, 1, ... ,1]]``, and simply use the matrix-matrix product ``gemm`` to calculate the predictions for all samples :math:`d_{pred} = G \theta`.

We now complete a new model with the BayesianL2 template. Note that if either parameter sets or L2-``dataobs`` descriptions doesn't fit your model, you may write your own methods following the ``Model`` protocol.

Please also note that vectors/matrices in AlTar are based on GSL, while they can operate as numpy arrays. But if you would like to use some numpy/scipy functions on numpy arrays, on you may create a numpy ndarray view or copy from GSL vectors/matrices. See :ref:`Matrix/Vector (GSL)` for more details.


C/C++/CUDA extension modules
============================

For certain procedures, the Python code might not be efficient and you might want to write them in other high performance programming languages. For example, the Linear Algebra libraries (BLAS, LAPACK) are written in FORTRAN/C while are accessible in Python by extension modules.

While there are many convenient tools to write Python wrappers for C/C++/Fortran/CUDA functions, such as ``cython``, ``SWIG``, ``Boost.Python``, ``pybind11``, we recommend the native CPython method.

Let's use an example of vector copy.
Define in ``copy.h``:

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

CUDA Models
===========
TBD


Data Types and Structures
=========================

Configurable properties
-----------------------

.. code-block:: python

    altar.properties.array
    altar.properties.bool
    altar.properties.catalog
    altar.properties.complex
    altar.properties.converter
    altar.properties.date
    altar.properties.decimal
    altar.properties.dict
    altar.properties.dimensional
    altar.properties.envpath
    altar.properties.envvar
    altar.properties.facility
    altar.properties.float
    altar.properties.identity
    altar.properties.inet
    altar.properties.int
    altar.properties.istream
    altar.properties.list
    altar.properties.normalizer
    altar.properties.object
    altar.properties.ostream
    altar.properties.path
    altar.properties.paths
    altar.properties.property
    altar.properties.set
    altar.properties.str
    altar.properties.strings
    altar.properties.time
    altar.properties.tuple
    altar.properties.uri
    altar.properties.uris
    altar.properties.validator


.. _Matrix/Vector (GSL):

Matrix/Vector (GSL)
-------------------
The Matrix/Vector is based on GSL Matrix/Vector.

GSL matrix shape (size1, size2) -> (rows, cols) and is row-major.

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

Interfacing as numpy arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~

As there are more utilities available for numpy ``ndarray``s, you may view or copy GSL vectors/matrices are numpy arrays.

.. code-block:: python

    # create a gsl vector
    gslv = altar.vector(shape=10).fill(1)
    # create a numpy array view (data changes to npa_view will change gslv)
    npa_view = gslv.ndarray()
    # create a numpy array view (data changes to npa_view don't affect gslv)
    npa_copy = gslv.ndarray(copy=True)





