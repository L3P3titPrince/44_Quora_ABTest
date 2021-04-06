from class_31_hyperparameters import HyperParameters

import numpy as np
import seaborn as sns
# this model will output degree of freedom
import statsmodels.stats.weightstats as st
from scipy import stats


class Hypothesis(HyperParameters):
    """:arg
    We use this class to calculate statical data and judge reject or accept hypothesis

    """
    def __init__(self):
        """:arg
        """
        HyperParameters.__init__(self)


    def ttest_ind(self, df_control, df_treat):
        """:arg


        Args:
        ------
        df_control:Series

        """
        print('Distribution of control group')
        sns.boxplot(x = df_control)
        sns.distplot(df_control)

        # caculate t-test for tow independtant dataset
        # because we caculate with total minutes, so the user rate 40000:10000 is imbalance
        # we need divide df_control with 4 to achieve same total minutes for 10000 users
        # t_value is t statical
        t_value, p_two, degree_free = st.ttest_ind(x1 = df_control
                                                   , x2 = df_treat
                                                   , usevar='unequal')
        # use a diiffernt function for t-test
        t_stat, p_value = stats.ttest_ind(df_control, df_treat, equal_var=False)
        # default confidence interval is 95%, so one side alpha = (1-95%)/2 = 0.025
        if (p_two < 1-self.ALPHA):
            print('P-value {} < {}'.format(p_two, 1-self.ALPHA))
            print('Reject H0 (control and treatment dont have siginificent differnet) hypothesis')
            print('Accept H1 (control and treatment have siginificent different) hypothesis')
        else:
            print('P-value {} > {}'.format(p_two, 1 - self.ALPHA))
            print('Accept H0 (control and treatment dont have siginificent differnet) hypothesis')
            print('Reject H1 (control and treatment have siginificent different) hypothesis')

        # start cacualte confidence interval (right tail=0.025) (two tail=0.05)
        # we have 150-200 data point, so when check t-distribution table,
        t_ci = stats.t.ppf(q = self.ALPHA, df=150)
        # sample number
        control_num = df_control.shape[0]
        treat_num = df_treat.shape[0]
        # cacualte stand diviation
        control_std = df_control.std()
        treat_std = df_treat.std()
        # cacualte se
        se = np.sqrt( np.square(control_std)/control_num + np.square(treat_std)/treat_num)
        #
        sample_mean = df_control.mean() - df_treat.mean()
        # calcuate confidenal interval
        upper_bound = sample_mean - t_ci * se
        lower_bound = sample_mean + t_ci * se

        print(upper_bound, lower_bound)

        return (t_value, p_two, degree_free, t_stat, p_value, upper_bound, lower_bound)



