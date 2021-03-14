from astropy.coordinates import SkyCoord

try:
    print("ex. R.A.(hms):00h00m00s")
    ra_hms = raw_input("R.A.(hms):")  
    print("")
    print("ex. DEC.(dms):00d00m00s")
    dec_dms = raw_input("DEC.(dms):")
except:
    print("ex. R.A.(hms):00h00m00s")
    ra_hms = input("R.A.(hms):")
    print("")
    print("ex. DEC.(dms):00d00m00s")
    dec_dms = input("DEC.(dms):")

c = SkyCoord(ra_hms, dec_dms, frame='fk5')
print("")
print("R.A. hms to deg\n{}".format(c.ra))
print("DEC. dms to deg\n{}".format(c.dec))