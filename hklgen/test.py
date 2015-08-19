import os,sys;sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
import fswig_hklgen as H
import hkl_model as Mod
np.seterr(divide="ignore", invalid="ignore")    

DATAPATH = os.path.dirname(os.path.abspath(__file__))
infoFile = os.path.join(DATAPATH,"test.cif")

(spaceGroup, crystalCell, atoms) = H.readInfo(infoFile)
wavelength = 1.5403


def main():
    cell = H.CrystalCell([4.761,4.761,13.001],[90,90,120])
    uvw = [0.151066141044763,-0.0914698313404034,0.0693509296318546]
    H.diffPattern(infoFile=infoFile, wavelength=wavelength,
                  cell=cell, uvw=uvw, scale=1.40313478468024,
                  plot=True)

if __name__ == "__main__":
    # program run normally
    main()
else:
    # called using bumps
    import bumps.names as bumps
    problem = fit()
