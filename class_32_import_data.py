from class_31_hyperparameters import HyperParameters

import pandas as pd
# measure running time
from time import time

import os


class ImportData(HyperParameters):
    """:arg


    """
    def __init__(self):
        """:arg
        """
        HyperParameters.__init__(self)

    def import_data(self):
        """:arg
        Use this function to complete import data process
        """
        print("*" * 50, "Start import data", "*" * 50)
        start_time = time()

        path_t1 = os.path.join(self.ROOTPATH, 't1_user_active_min.csv')
        path_t2 = os.path.join(self.ROOTPATH, 't2_user_variant.csv')
        path_t3 = os.path.join(self.ROOTPATH, 't3_user_active_min_pre.csv')
        path_t4 = os.path.join(self.ROOTPATH, 't4_user_attributes.csv')
        
        df_t1 = pd.read_csv(path_t1)
        df_t2 = pd.read_csv(path_t2)
        df_t3 = pd.read_csv(path_t3)
        df_t4 = pd.read_csv(path_t4)

        return (df_t1, df_t2, df_t3, df_t4)
