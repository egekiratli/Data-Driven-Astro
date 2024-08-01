import numpy as np


def hms2dec(h,m,s):
  return 15*(h+m/60 + s/(60*60))

def dms2dec(d,m,s):
  if d < 0:
    return d - m/60 - s/3600
  else:
    return d + m/60 + s/3600
  
#Calculates angular distance
def angular_dist(ra1,dec1,ra2,dec2):
  
  ra1 = np.radians(ra1)
  ra2 = np.radians(ra2)
  
  dec1 = np.radians(dec1)
  dec2 = np.radians(dec2)
  
  a = (np.sin(np.abs(dec1-dec2)/2))**2
  b = np.cos(dec1)*np.cos(dec2)*(np.sin(np.abs(ra1-ra2)/2))**2
  
  d = 2*np.arcsin(np.sqrt(a+b))
  d = np.degrees(d)
  
  return d

#Imports AT20G BSS catalogue
def import_bss():
  data = np.loadtxt('bss.dat',usecols=range(1,7))
  
  objID = [i+1 for i in range(len(data))]
  rightAsc = [hms2dec(i[0],i[1],i[2]) for i in data]
  dec = [dms2dec(i[3],i[4],i[5]) for i in data]
  
  convData = [(objID[i],rightAsc[i],dec[i]) for i in range(len(data))]
  
  return convData

#Imports SuperCOSMOS catalogue
def import_super():
  data = np.loadtxt('super.csv', delimiter=',',skiprows=1, usecols=[0,1])
  objID = [i+1 for i in range(len(data))]
                    
  convData = [(objID[i],data[i][0],data[i][1]) for i in range(len(data))]

  return convData

#Crossmatch function
def crossmatch(bss_cat,super_cat, max_dist):
  
  bssID = [bss_cat[i][0] for i in range(len(bss_cat))]
  bssRa = [bss_cat[i][1] for i in range(len(bss_cat))]
  bssDec = [bss_cat[i][2] for i in range(len(bss_cat))]
  
  supID = [super_cat[i][0] for i in range(len(super_cat))]
  supRa = [super_cat[i][1] for i in range(len(super_cat))]
  supDec = [super_cat[i][2] for i in range(len(super_cat))]
    
  bssRa = np.radians(bssRa)
  supRa = np.radians(supRa)
  
  bssDec = np.radians(bssDec)
  supDec = np.radians(supDec)
    
  matches = []
  no_matches = []
  
  
  for bssObj in bss_cat:
    bssID,bssRa,bssDec = bssObj
    closestD = np.inf
    closestMatch = None
    
    for supObj in super_cat:
      supID,supRa,supDec = supObj
      d = angular_dist(bssRa,bssDec,supRa,supDec)
      
      if d < closestD:
        closestD = d
        closestMatch = (supID, d)
      
    if closestD <= max_dist:
      matches.append((bssID,closestMatch[0],closestMatch[1]))
  
    else:
      no_matches.append(bssID)
  
  return matches, no_matches




if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
