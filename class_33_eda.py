from class_31_hyperparameters import HyperParameters

# use sns for visulization
import seaborn as sns
# numpy
import numpy as np
# solve statistical problem
from scipy import stats

class EDA(HyperParameters):
    """:arg
    Preproceess EDA



    """
    def __init__(self):
        """:arg
        """
        HyperParameters.__init__(self)

    def outlier_eda(self, df):
        """:arg
        We use several way to detect and remove outliers

        Args:
        -------
        df:DataFrame
            This can be data_t1 or data_t3. These two dataframe need ourlier detect and clean

        """
        # first we need to make sure this is outlier or error exist
        # we use boxplot()
        sns.boxplot(x=df['active_mins'])
        # use z-score to eliminate outliers, the output is for indivudal data point
        z_score = np.abs(stats.zscore(df['active_mins']))
        # set a z-score threshold, any greater than this value will be eliminate
        z_threshold = 3
        # filter that ooutlier rows in dataframe
        index_outlier = np.where(z_score > z_threshold)
        # print out result
        print('We have {} data points are outliers'.format(len(index_outlier[0])))
        # drop these rows by index
        df = df.drop(index_outlier[0])

        return df
