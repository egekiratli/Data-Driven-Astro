from astropy.io import fits
import numpy as np
import time
import sys

#This function takes a list of FITS filenames, loads them into a NumPy array,
#and returns tuple of the median NumPy array, 
#the time it took the function to run, 
#and the amount of memory (in kB) used to store all the FITS files in the NumPy array in memory

def median_fits(listFITS):  
  start = time.perf_counter()
  
  dSet = []
  memory = 0
  
  for file in listFITS:
    hdulist = fits.open(file)
    dLoad = hdulist[0].data
    dSet.append(dLoad)
    memory += dLoad.nbytes
      
  memory = memory/1024
  
  median = np.median(dSet,axis=0)

  seconds = time.perf_counter() - start
  
  return median, seconds, memory
  

if __name__ == '__main__':
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])  
  print(result[0][100, 100], result[1], result[2])