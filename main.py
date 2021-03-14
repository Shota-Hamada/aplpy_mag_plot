import aplpy
import numpy as np

# (figure filename) extension
filename = "sgr_a_ziba"
extension = "pdf" #selection of .png, .ps, .eps, .pdf, .jpg
# Figure => figure/filename.extension

#====================
# FITS load to aplpy
#====================
f = aplpy.FITSFigure('fits_file/iextGalCM2812YYNN.fit',figsize=(8,6))


#=========================
# tick_labels.set
#=========================
f.tick_labels.set_yformat('dd:mm:ss')
f.tick_labels.set_xformat('hh:mm:ss')
f.axis_labels.set_xtext(r'$\rm{Right\;Ascension\:(J2000)}$')
f.axis_labels.set_ytext(r'$\rm{Declination\:(J2000)}$')


#==========================
# colorscale and contour
#==========================
f.show_colorscale(vmin=60,vmax=4000,cmap='jet',stretch='linear', aspect='auto')
# f.show_contour(colors='black',levels=[50,75,100,125,150,175], lw=0.8)


#=============
# colorbar
#=============
f.add_colorbar()
f.colorbar.set_location('right')
f.colorbar.set_pad(0.3)
f.colorbar.set_width(0.5)
f.colorbar.set_font(size=10)


#=============
# axis_labels
#=============
f.colorbar.set_axis_label_text(r'$mJy\;beam^{-1}$')
f.colorbar.set_axis_label_font(size=10,weight='bold')
f.colorbar.set_axis_label_pad(10)
f.colorbar.set_axis_label_rotation(270)


#===============
# Magnetic field
#===============

Magnetic_field_plot = "yes" # yes or no

if Magnetic_field_plot == "yes":
    # Importing self-made modules
    from magnetic_field import ziba

    factor = 0.001 # P=1 => 1deg
    ang = 90 

    ziba_ra = ziba.ziba_xy(factor=factor, ang=ang)[0] 
    ziba_dec = ziba.ziba_xy(factor=factor, ang=ang)[1] 
    ziba_x = ziba.ziba_xy(factor=factor, ang=ang)[2]
    ziba_y = ziba.ziba_xy(factor=factor, ang=ang)[3]

    for i in range(len(ziba_ra)):
        line = np.array([[ziba_ra[i]-ziba_x[i],ziba_ra[i]+ziba_x[i]],[ziba_dec[i]-ziba_y[i],ziba_dec[i]+ziba_y[i]]])
        f.show_lines([line],color='r',lw=0.8)
elif Magnetic_field_plot == "no":
    pass
else:
    pass

#============
# scalebar
#============

length = 4.0

f.add_scalebar(length=factor*length,corner='top right',color='r',lw=0.8) #corner: top raight(left), bottom right(left)
f.scalebar.set_label(str(length))
f.scalebar.set_font(size=8,weight='bold')


#=========
# marker
#=========

marker_ra_deg = 266.418
marker_dec_deg = -29.008

f.add_label(marker_ra_deg+0.003, marker_dec_deg+0.003, r'$\bf{Sgr\:A^{\star}}$', color='w', size=12)
f.show_markers(marker_ra_deg, marker_dec_deg, marker='+', s=300, c="w", lw=3) # x, y (deg)

 
#=========
# recenter
#=========

ra_center = 266.418 # (deg)
dec_center = -29.008 # (deg)

f.recenter(ra_center, dec_center, width=0.06, height=0.06) # width, height (deg)


#========
# save
#========
f.save('figure/'+filename+'.'+extension)
f.close()


print('################')
print("End: Good job!!")
print('################')