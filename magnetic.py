import pandas as pd
from astropy.coordinates import SkyCoord

ziba = pd.read_csv("ziba.csv")

ziba_ra = ziba.iloc[:,2]
ziba_dec = ziba.iloc[:,3]
ziba_p = ziba.iloc[:,10]
ziba_ang = ziba.iloc[:,12]

ziba_coord = SkyCoord(ziba_ra, ziba_dec, frame='fk5')

