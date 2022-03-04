## Static Slip Inversion with Cp: Epistemic Uncertainties


In addition to observational errors, one can calculate epistemic uncertainties (Minson et al., 2013), which affect the forward model and are related to our imperfect knowledge of the Earth interior. Epistemic uncertainties will stem from a various set of parameters, but the most prominent uncertainties will derive from elastic heterogeneity (Duputel et al., 2014) and fault geometry (Ragon et al., 2018, 2019). 

To estimate epistemic uncertainties, we assume that the real surface displacement follows a Gaussian distribution centred on the predictions with a prediction covariance matrix Cp that depends on the resulting source model. The misfit covariance matrix characterizing the misfit function becomes `Cx = Cd + Cp`.

**First approach: static Cp**

The prediction covariance matrix `Cp` can be included in the inversion following two different approaches. In the first, `Cp` is calculated a priori and included in the inversion process within `Cx`. In this case, the full `Cx` matrix replaces the `Cd ` matrix:

        dataobs = altar.cuda.data.datal2
        dataobs:
            observations = 1000
            data_file = d.txt
            cd_file = cx.txt ; Cx contains both Cd and Cp

**Second approach: Updated Cp**

The alternative approach, implemented in AlTar, is to update Cp with interim models at each step of the tempered inversion. The covariance matrix `Cp` is calculated from 3 variables: a sensitivity kernel for every investigated parameter, the standard deviation of the a priori distribution of investigated parameters, and an initial model chosen a priori. In this approach, `Cp` is re-calculated at each tempering step by choosing the mean of tested samples as the assumed initial model.


        ; sensitivity kernels
        nCmu = 8 ; number of investigated parameters
        cmu_file = Cmu.h5 ; standard deviation matrix
        kmu_file = Kelastic.h5 ; tensor of sensitivity kernels (matrix if only one investigated parameter)
        initial_model_file = inimodel.txt ; initial model vector

Additionnally, `Cp` can be incorporated in the inversion at any tempering step. The tempering step will be selected with its corresponding beta value, parameterized by `beta_cp_start`. 
If  `beta_cp_start = 0.01`, then `Cp` will be incorporated from the beginning of the inversion process. If  `beta_cp_start = 0.1` or `0.5`, then `Cp` will be incorporated after a few tempering steps, or once beta reaches 0.5, respectively. 
`beta_use_initial_model` will indicate if the initial model should be used (`1`) or not (`0`). If not, then a unit uniform initial model is used.

        beta_cp_start = 0.01 ; beta value to start incorporating Cp
        beta_use_initial_model = 1 ; use provided initial model
