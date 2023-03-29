from snaptools import snapshot
from snaptools import plot_tools
import gc

size=[10,100,1000]
BOX=[0.01,0.1,1]
gridsize=[256,256,512]

RS=[1.000e+01,
1.078e+01,
1.152e+01,
1.230e+01,
1.326e+01,
1.442e+01,
1.567e+01,
1.717e+01,
1.899e+01,
2.404e+01,
3.233e+01,
4.907e+01,
6.564e+01,
9.912e+01,
1.000e+02]


for k in range(3):
    for j in range(14,15):
        snaps=[]
        for i in range(30):
            snaps.append("E:Final_Runs/%ikpc/snapdir_0%02d/snapshot_0%02d.%i.hdf5"%(size[k],j,j,i))
        plot_tools.plot_powerspec(snaps, 
                                outfolder='C:/Users/Sebas/Downloads/powerspeX-%ikpc/'%size[k],
                                outname='powerspec%i-%i_z=%.1f'%(size[k],j,RS[14-j]),
                                NBINS=512,
                                boxsize=BOX[k],                    #Mpc/h
                                gadgetGridsize=gridsize[k])        #kpc
        
        gc.collect()

#plot_tools.plot_combined_3D(snaps,parttype='gas',xlen=(0,1),ylen=(0,1),zlen=(0,1),NBINS=256, gadgetGridsize=512)


