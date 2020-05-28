## AlTar 2.0

### About AlTar
AlTar(Al-Tar) is a software package to solve inverse problems with Bayesian inference. It is named after the Spanish-French physicist [Albert Tarantola](https://en.wikipedia.org/wiki/Albert_Tarantola), for his pioneering work on the Bayesian perspective of inverse problems.

AlTar uses primarily the [Cascading Adaptive Tempered Metropolis In Parallel (CATMIP) algorithm](https://thesis.library.caltech.edu/5918/), which is designed to efficiently simulate problems with high-dimensional spaces on parallel computers, include Graphics Processing Units(GPUs).

### Guides
(work in progress, currently for AlTar 2.0 CUDA version only)

Readthedocs ([html](https://altar.readthedocs.io)/[pdf](https://altar.readthedocs.io/_/downloads/en/cuda/pdf/)/[epub](https://altar.readthedocs.io/_/downloads/en/cuda/epub/)):

- [Installation Guide](https://altar.readthedocs.io/en/cuda/cuda/Installation.html) 
- [User Guide](https://altar.readthedocs.io/en/cuda/cuda/Manual.html) 
- [Programming Guide](https://altar.readthedocs.io/en/cuda/cuda/Programming.html) 
- [API Reference](https://altar.readthedocs.io/en/cuda/api/index.html)

[Source on github](https://github.com/lijun99/altar2-documentation).

### Tutorials
Tutorials presented with jupyter notebooks:

- [An introduction to AlTar/pyre applications: HelloApp](https://github.com/lijun99/altar2-documentation/tree/cuda/jupyter/hello/hello.ipynb)
- [An overview of the AlTar framework](https://github.com/lijun99/altar2-documentation/tree/cuda/jupyter/linear/linear.ipynb)

- Static slip inversion: a toy model with epistemic uncertainties

  - [Step 1: prepare the input files](https://github.com/lijun99/altar2-documentation/blob/thearagon-patch-1/jupyter/intro_cp/toymodel_step1.ipynb)
  - [Step 2: run AlTar2](https://github.com/lijun99/altar2-documentation/blob/thearagon-patch-1/jupyter/intro_cp/toymodel_step2.ipynb)

### Discussion groups

- [AlTar mailing list](http://lists.gps.caltech.edu/mailman/listinfo/altar)
- [slack](https://altar-group.slack.com)

### Bug reporting

- [Issues @ github](https://github.com/AlTarFramework/altar/issues)

### Copyright

```text
    Copyright (c) 2013-2020 ParaSim Inc.
    Copyright (c) 2010-2020 California Institute of Technology
    All Rights Reserved
    
    This software is subject to the provisions of its LICENSE, a copy of
    which should accompany all distributions, in both source and binary
    form. If you received this software without a copy of the LICENSE,
    please contact the author at michael.aivazis@para-sim.com.
    
    THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
    WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
    FOR A PARTICULAR PURPOSE.
```
