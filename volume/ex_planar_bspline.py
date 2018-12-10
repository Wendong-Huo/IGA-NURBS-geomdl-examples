#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

from geomdl import BSpline
from geomdl import multi
from geomdl import CPGen
from geomdl import utilities
from geomdl import construct
from geomdl.visualization import VisMPL as vis


# Required for multiprocessing module
if __name__ == "__main__":
    # Generate control points grid for Surface #1
    sg01 = CPGen.Grid(15, 10, z_value=0.0)
    sg01.generate(8, 8)

    # Create a BSpline surface instance
    surf01 = BSpline.Surface()

    # Set degrees
    surf01.degree_u = 1
    surf01.degree_v = 1

    # Get the control points from the generated grid
    surf01.ctrlpts2d = sg01.grid

    # Set knot vectors
    surf01.knotvector_u = utilities.generate_knot_vector(surf01.degree_u, surf01.ctrlpts_size_u)
    surf01.knotvector_v = utilities.generate_knot_vector(surf01.degree_v, surf01.ctrlpts_size_v)

    # Generate control points grid for Surface #2
    sg02 = CPGen.Grid(15, 10, z_value=1.0)
    sg02.generate(8, 8)

    # Create a BSpline surface instance
    surf02 = BSpline.Surface()

    # Set degrees
    surf02.degree_u = 1
    surf02.degree_v = 1

    # Get the control points from the generated grid
    surf02.ctrlpts2d = sg02.grid

    # Set knot vectors
    surf02.knotvector_u = utilities.generate_knot_vector(surf02.degree_u, surf02.ctrlpts_size_u)
    surf02.knotvector_v = utilities.generate_knot_vector(surf02.degree_v, surf02.ctrlpts_size_v)

    # Generate control points grid for Surface #3
    sg03 = CPGen.Grid(15, 10, z_value=2.0)
    sg03.generate(8, 8)

    # Create a BSpline surface instance
    surf03 = BSpline.Surface()

    # Set degrees
    surf03.degree_u = 1
    surf03.degree_v = 1

    # Get the control points from the generated grid
    surf03.ctrlpts2d = sg03.grid

    # Set knot vectors
    surf03.knotvector_u = utilities.generate_knot_vector(surf03.degree_u, surf03.ctrlpts_size_u)
    surf03.knotvector_v = utilities.generate_knot_vector(surf03.degree_v, surf03.ctrlpts_size_v)

    # Construct the parametric volume
    pvolume = construct.construct_volume(surf01, surf02, surf03, degree=1)
    pvolume.vis = vis.VisVoxel(vis.VisConfig(ctrlpts=False))
    pvolume.delta_u = pvolume.delta_v = 0.025
    pvolume.delta_w = 0.05
    pvolume.render(evalcolor="firebrick", use_mp=True, num_procs=16)

    # Extract surfaces from the parametric volume
    surfvol = construct.extract_surfaces(pvolume)

    # Construct the isosurface
    msurf = multi.SurfaceContainer(surfvol['uv'][0], surfvol['uv'][-1], surfvol['uw'][0], surfvol['uw'][-1],
                                   surfvol['vw'][0], surfvol['vw'][-1])
    msurf.vis = vis.VisSurface(vis.VisConfig(ctrlpts=False))
    msurf.delta = 0.05
    msurf.render(evalcolor=["skyblue", "cadetblue", "crimson", "crimson", "crimson", "crimson"])

# Good to have something here to put a breakpoint
pass
