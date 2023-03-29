import camb
from camb import model, initialpower
from matplotlib import pyplot as plt # Matplotlib is a plotting library
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--G', help='do gadget spectre [1,0]')
args = parser.parse_args()
args = vars(args)
post = bool(int(args['G']))

print('Using CAMB %s installed at %s'%(camb.__version__,os.path.dirname(camb.__file__)))
params = camb.CAMBparams()
params.set_cosmology(H0=68, ombh2=0.022, omch2=0.12, mnu=0.06, omk=0, tau=0.06)

PK = camb.get_matter_power_interpolator(params, nonlinear=True, kmax=11000)

# Get matter power spectrum at redshift z=0.5
for z in np.loadtxt('RSs.txt'):
    k = np.logspace(-1, 5, 10000,dtype=np.double)
    P = PK.P(z, k)

    #cutoff the data when it flatlines
    for i in range(len(P)):
        if P[i] == P[i-1]:
            P = P[:i]
            k = k[:i]
            break

    if post:
        #camb postprocessing
        P = 4*np.pi*(k**3)*P
        k = k
    #plt.plot(k,P)
    #plt.show()
    P = np.log10(P,dtype=np.double)
    k = np.log10(k,dtype=np.double)
    #plt.plot(k,P)
    #plt.show()
    op = np.transpose([k, P])
    print(op.shape)
    if f'camb-pipeline-spec-z{z}.txt' in os.listdir():
        os.remove(f'camb-pipeline-spec-z{z}.txt')
    np.savetxt(f'camb-pipeline-spec-z{z}.txt', op,fmt='%.18e')


