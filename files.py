'''
Created on Jan 20, 2018

@author: Sourcode
'''

import numpy as np
import _csv
import os

'test.txt'
'''
0
1
'''


def main():
    r_file = open('test.txt', 'r')
    reader = _csv.reader(r_file, delimiter=" ")
    wr_array = []
    
    #test if file is empty
    if os.stat('test.txt').st_size == 0:
        print ('File is empty')
        return 0
    
    #read the rows
    for row in reader:
        wr_array.append(row[0])
    
    #display the array
    np_array = np.array(wr_array)
    print (np_array)
    
    #close the file opened in read mode
    r_file.close
    
    #do the swapping
    # must remember: wr_array is a list and direct conversion to int is essential
    ''''''
    a = int(wr_array[0])
    b = int(wr_array[1])
    a = a+b
    b = a-b
    a = a-b
    wr_array[0] = a
    wr_array[1] = b
    ''''''
    
    #open the file in write mode
    w_file = open('test.txt', 'w')
    w_file.write(str(wr_array[0]) + '\n' + str(wr_array[1]))
    w_file.close
    
    return

if __name__ == '__main__':
    main()
    
    
