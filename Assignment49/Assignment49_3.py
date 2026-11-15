# Python program using standardScaler to perform feature scalling on the following data
# [[25,20000],
#  [30, 40000],
#  [35, 80000]]

import numpy as np
from sklearn.preprocessing import StandardScaler

def Stdscalar():
    
    Dataset =np.array([
        [25,20000],
        [30, 40000],
        [35, 80000]
    ])
    
    model = StandardScaler()
    
    scaled_data = model.fit_transform(Dataset)
    
    print("Original dataset :" )
    print(Dataset)
    print("Scaled Dataset :")
    print(scaled_data)
    
def main():
    
    Stdscalar()
    
if __name__ =="__main__":
    main()