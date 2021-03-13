import aplpy
import matplotlib.pyplot as plt
import numpy as np

f = aplpy.FITSFigure('iextGalCM2812YYNN.fit',figsize=(10,10))

###tick_labels.set_format###
f.tick_labels.set_yformat('dd:mm:ss')
f.tick_labels.set_xformat('hh:mm:ss')
f.axis_labels.set_xtext(r'$\rm{Right\;Ascension\:(J2000)}$')
f.axis_labels.set_ytext(r'$\rm{Declination\:(J2000)}$')

###colorbar###
f.show_colorscale(vmin=60,vmax=2000,cmap='gray',stretch='linear')
# f.show_contour(colors='black',levels=[50,75,100,125,150,175])

f.add_colorbar()
f.colorbar.set_location('right')
f.colorbar.set_pad(0.3)
f.colorbar.set_width(0.6)
f.colorbar.set_font(size=10)
###axis_labels###
f.colorbar.set_axis_label_text(r'$mJy~beam^{-1}$')
f.colorbar.set_axis_label_font(size=10,weight='bold')
f.colorbar.set_axis_label_pad(20)
f.colorbar.set_axis_label_rotation(270)

# f.recenter(ra, dec, width=0.3, height=0.3) # degrees

import pandas as pd
from astropy.coordinates import SkyCoord

ziba = pd.read_csv("ziba.csv")

ziba_ra = ziba.iloc[:,2]
ziba_dec = ziba.iloc[:,3]
ziba_p = ziba.iloc[:,10]
ziba_ang = ziba.iloc[:,12]

ziba_coord = SkyCoord(ziba_ra, ziba_dec, frame='fk5')

# line = np.array([[ziba_coord[0].ra-0.2,ziba_coord[0].ra+0.2],[ziba_coord[0].dec-0.2,ziba_coord[0].dec+0.2]])
print(ziba_coord[0].ra)
