def ziba_xy(factor = 0.001, ang=90):
    import pandas as pd
    import numpy as np
    from astropy.coordinates import SkyCoord

    ziba = pd.read_csv("magnetic_field/ziba.csv")

    ziba_ra = ziba.iloc[:,2]
    ziba_dec = ziba.iloc[:,3]
    ziba_p = ziba.iloc[:,10]
    ziba_ang = ziba.iloc[:,12]

    ziba_coord = SkyCoord(ziba_ra, ziba_dec, frame='fk5')

    deg2rad = np.pi / 180

    ra = ziba_coord.ra.deg
    dec = ziba_coord.dec.deg
    y = ziba_p * np.cos((ang+ziba_ang) * deg2rad) * factor
    x = ziba_p * np.sin((ang+ziba_ang) * deg2rad) * factor
    return(ra, dec, x, y)

