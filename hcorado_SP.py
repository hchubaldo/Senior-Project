import pandas as pd
import numpy as np
import scipy.stats

read_file = pd.read_csv (r'C:\Users\admin\Dropbox\Bioinformatics\Senior Project\gut_16s_abundance.txt')
read_file.to_csv (r'C:\Users\admin\Dropbox\Bioinformatics\Senior Project\gut_16s_abundance.csv', index=None)
