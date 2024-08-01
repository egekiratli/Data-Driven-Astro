import numpy as np

#This function takes a list of values and the number of bins, B, 
#and returns the mean μ and standard deviation σ of the values,
#the number of values smaller than μ−σ, 
#and a NumPy array with B elements containing the bin counts.

def median_bins(dList, B):
  
  mean = np.mean(dList)
  std = np.std(dList)
  
  minVal = mean - std
  maxVal = mean + std
  
  widthBin = 2*std/B
  
  minCount = 0
  binCount = np.zeros(B)
 
  
  for value in dList:
    if value < minVal:
      minCount += 1
    elif minVal <= value and value < maxVal:
      binIndex = int((value-minVal)/widthBin)
      if binIndex < B:
        binCount[binIndex] += 1
      
  return mean, std, minCount, binCount

#This function takes the same input as median_bins. 
#It returns the approximate median using median_bins to calculate the bins

def median_approx(dList, B):
  
  mean,std,sumCount,binCount = median_bins(dList, B)
  
  N = len(dList)
  
  for i in range(B):
    sumCount += binCount[i]
    if sumCount >= (N+1)/2:
      midpointBin = mean - std + (i+0.5)*2*std/B
        
      return midpointBin
    
  return std + mean

if __name__ == '__main__':

  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))


  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4)) #4.5

  print(median_bins([0, 1], 5))
  print(median_approx([0, 1], 5))