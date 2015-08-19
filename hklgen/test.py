import os,sys;sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
import fswig_hklgen as H
np.seterr(divide="ignore", invalid="ignore")    

DATAPATH = os.path.dirname(os.path.abspath(__file__))
infoFile = os.path.join(DATAPATH,"test.cif")
print "here"
(spaceGroup, crystalCell, atoms) = H.readInfo(infoFile)

def getS(tt, wavelength):
    return np.sin(np.radians(tt/2))/wavelength

def main():
    print "here"
    #spaceGroup = None
    #cell = None
    wavelength = 1.5403
    cell = H.CrystalCell([11.372,10.272,7.359],[108.92,71.07,96.16]) # AABHTZ cell parameters
    uvw = [0.151066141044763,-0.0914698313404034,0.0693509296318546]
    #H.diffPattern(infoFile=infoFile, wavelength=wavelength,
    #              cell=cell, uvw=uvw, scale=1.40313478468024,
    #              info=True,plot=True)
    
    
    sMin, sMax = getS(0.0, wavelength), getS(180.0, wavelength)
    spaceGroup = None
    infofile = H.readInfo(infoFile)
    if (spaceGroup == None): spaceGroup = infofile[0]
    if (cell == None): cell = infofile[1]
    refList = H.hklGen(spaceGroup, cell, sMin, sMax, True, xtal=False) # gets the reflections list but not the positions
    for value in refList:
        print value.hkl
    
    

if __name__ == "__main__":
    # program run normally
    main()
