:mod:`altar.models.cdm.libcdm`
==============================

.. py:module:: altar.models.cdm.libcdm


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   altar.models.cdm.libcdm.cosd
   altar.models.cdm.libcdm.sind
   altar.models.cdm.libcdm.norm
   altar.models.cdm.libcdm.CDM
   altar.models.cdm.libcdm.RDdispSurf
   altar.models.cdm.libcdm.CoordTrans
   altar.models.cdm.libcdm.AngSetupFSC
   altar.models.cdm.libcdm.AngDisDispSurf


.. function:: cosd(angd)


.. function:: sind(angd)


.. function:: norm(v)


.. function:: CDM(X, Y, X0, Y0, depth, ax, ay, az, omegaX, omegaY, omegaZ, opening, nu)

   CDM
   calculates the surface displacements and potency associated with a CDM
   that is composed of three mutually orthogonal rectangular dislocations in
   a half-space.

   CDM: Compound Dislocation Model
   RD: Rectangular Dislocation
   EFCS: Earth-Fixed Coordinate System
   RDCS: Rectangular Dislocation Coordinate System
   ADCS: Angular Dislocation Coordinate System
   (The origin of the RDCS is the RD centroid. The axes of the RDCS are
   aligned with the strike, dip and normal vectors of the RD, respectively.)

   INPUTS
   X and Y:
   Horizontal coordinates of calculation points in EFCS (East, North, Up).
   X and Y must have the same size.

   X0, Y0 and depth:
   Horizontal coordinates (in EFCS) and depth of the CDM centroid. The depth
   must be a positive value. X0, Y0 and depth have the same unit as X and Y.

   omegaX, omegaY and omegaZ:
   Clockwise rotation angles about X, Y and Z axes, respectively, that
   specify the orientation of the CDM in space. The input values must be in
   degrees.

   ax, ay and az:
   Semi-axes of the CDM along the X, Y and Z axes, respectively, before
   applying the rotations. ax, ay and az have the same unit as X and Y.

   opening:
   The opening (tensile component of the Burgers vector) of the RDs that
   form the CDM. The unit of opening must be the same as the unit of ax, ay
   and az.

   nu:
   Poisson's ratio.

   OUTPUTS
   ue, un and uv:
   Calculated displacement vector components in EFCS. ue, un and uv have the
   same unit as opening and the CDM semi-axes in inputs.

   DV:
   Potency of the CDM. DV has the unit of volume (the unit of displacements,
   opening and CDM semi-axes to the power of 3).

   Example: Calculate and plot the vertical displacements on a regular grid.

   [X,Y] = numpy.meshgrid(-7:.02:7,-5:.02:5);
   X0 = 0.5; Y0 = -0.25; depth = 2.75; omegaX = 5; omegaY = -8; omegaZ = 30;
   ax = 0.4; ay = 0.45; az = 0.8; opening = 1e-3; nu = 0.25;
   import te[ [ue,un,uv,DV] = CDM(X,Y,X0,Y0,depth,omegaX,omegaY,omegaZ,ax,ay,az,...
   opening,nu);
   figure
   surf(X,Y,reshape(uv,size(X)),'edgecolor','none')
   view(2)
   axis equal
   axis tight
   set(gcf,'renderer','painters')

   Reference journal article:
   Nikkhoo, M., Walter, T. R., Lundgren, P. R., Prats-Iraola, P. (2016):
   Compound dislocation models (CDMs) for volcano deformation analyses.
   Submitted to Geophysical Journal International
   Copyright (c) 2016 Mehdi Nikkhoo

   Permission is hereby granted, free of charge, to any person obtaining a
   copy of this software and associated documentation files
   (the "Software"), to deal in the Software without restriction, including
   without limitation the rights to use, copy, modify, merge, publish,
   distribute, sublicense, and/or sell copies of the Software, and to permit
   persons to whom the Software is furnished to do so, subject to the
   following conditions:

   The above copyright notice and this permission notice shall be included
   in all copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
   OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
   NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
   DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
   OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
   USE OR OTHER DEALINGS IN THE SOFTWARE.

   I appreciate any comments or bug reports.

   Mehdi Nikkhoo
   Created: 2015.5.22
   Last modified: 2016.10.18

   Section 2.1, Physics of Earthquakes and Volcanoes
   Department 2, Geophysics
   Helmholtz Centre Potsdam
   German Research Centre for Geosciences (GFZ)

   email:
   mehdi.nikkhoo@gfz-potsdam.de
   mehdi.nikkhoo@gmail.com

   website:
   http://www.volcanodeformation.com

   Converted from Matlab to Python
   April 2018 by Eric Gurrola
   Jet Propulsion Lab/Caltech


.. function:: RDdispSurf(X, Y, P1, P2, P3, P4, opening, nu)

   RDdispSurf calculates surface displacements associated with a rectangular
   dislocation in an elastic half-space.


.. function:: CoordTrans(x1, x2, x3, A)

   CoordTrans transforms the coordinates of the vectors, from
   x1x2x3 coordinate system to X1X2X3 coordinate system. "A" is the
   transformation matrix, whose columns e1,e2 and e3 are the unit base
   vectors of the x1x2x3. The coordinates of e1,e2 and e3 in A must be given
   in X1X2X3. The transpose of A (i.e., A') will transform the coordinates
   from X1X2X3 into x1x2x3.


.. function:: AngSetupFSC(X, Y, bX, bY, bZ, PA, PB, nu)

   AngSetupSurf calculates the displacements associated with an angular
   dislocation pair on each side of an RD in a half-space.


.. function:: AngDisDispSurf(y1, y2, beta, b1, b2, b3, nu, a)

   AngDisDispSurf calculates the displacements associated with an angular dislocation
   in a half-space.


