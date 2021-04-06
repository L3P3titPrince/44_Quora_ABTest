from class_31_hyperparameters import HyperParameters

import pandas as pd
# test normal distribution
from scipy import stats

class JoinData(HyperParameters):
    """:arg
    """
    def __init__(self):
        """:arg
        """
        HyperParameters.__init__(self)

    def join_data_uid(self, df_t1, df_t2, df_t3, df_t4):
        """:arg
        We use function join to dataframe


        """
        # outer join df_t1 and df_t2 by uid
        df_t1t2 = pd.merge(df_t1, df_t2, on=['uid'], how='outer')
        # clean data drop NaN by row
        df_clean = df_t1t2.dropna(axis=0)
        # print clearn process
        print("Before {}, After {}".format(df_t1t2.shape[0], df_clean.shape[0]))
        # split into control group and treatment group and aggregate by user
        df_control = df_clean[df_clean['variant_number'] == 0].groupby(['uid'], as_index=False)['active_mins'].sum()
        # unit is total time spend per user per group, sometimes average or middle might have more meanning
        df_treat = df_clean[df_clean['variant_number'] == 1].groupby(['uid'], as_index=False)['active_mins'].sum()

        return df_clean, df_control, df_treat

    # def join_data_group(self, df_t1, df_t2, df_t3, df_t4):
    #     """:arg
    #     We use function join to dataframe
    #
    #
    #     """
        # # outer join df_t1 and df_t2 by uid
        # df_t1t2 = pd.merge(df_t1, df_t2, on=['uid'], how='outer')
        # # clean data drop NaN by row
        # df_clean = df_t1t2.dropna(axis=0)
        # # print clearn process
        # print("Before {}, After {}".format(df_t1t2.shape[0], df_clean.shape[0]))
        # # split into control group and treatment group and aggregate by user
        # df_control = df_clean[df_clean['variant_number'] == 0].groupby(['dt_x'], as_index=False)['active_mins'].sum()
        # # unit is total time spend per user per group, sometimes average or middle might have more meanning
        # df_treat = df_clean[df_clean['variant_number'] == 1].groupby(['dt_x'], as_index=False)['active_mins'].sum()
        #
        # return df_clean, df_control, df_treat

    def join_data_dt(self, df_t1, df_t2, df_t3, df_t4):
        """:arg
        I choose the unit is 'Total minutes per user per day in each group.
        First, we split data into control (not chagne)  and treatment (changed) group
        Second, we aggregate data records (88197 / 34175) in each group by date(['dt_x']
        This meaning is, in this group, everyday the total minutes from user log in action
        Typically, we have different log in user number in this whole 150 experiment days.
        Third, we divide everyday total mintues by the number of user who log in this day.

        They we can test them with normal distribution. If you want to calculate t-test, our dataset need to
        be normal distribution (stats.shapiro(df))


        """
        # outer join df_t1 and df_t2 by uid
        df_t1t2 = pd.merge(df_t1, df_t2, on=['uid'], how='outer')
        # clean data drop NaN by row
        df_clean = df_t1t2.dropna(axis=0)
        # print clearn process
        print("Before {}, After {}".format(df_t1t2.shape[0], df_clean.shape[0]))
        # split into control group and treatment group and aggregate by user
        df_dt_control = df_clean[df_clean['variant_number'] == 0].groupby(['dt_x'], as_index=False)['active_mins'].sum()
        # unit is total time spend per user per group, sometimes average or middle might have more meanning
        df_dt_treat = df_clean[df_clean['variant_number'] == 1].groupby(['dt_x'], as_index=False)['active_mins'].sum()
        # we caculate how many user log in each day
        df_usr_control = df_clean[df_clean['variant_number']==0].groupby(['dt_x'], as_index=False)['uid'].count()
        # caculate how many user login each day in treatment group
        df_usr_treat = df_clean[df_clean['variant_number']==1].groupby(['dt_x'], as_index=False)['uid'].count()

        # (total minutes per day) / (number of users who login in each day)
        df_control = df_dt_control['active_mins'].divide(df_usr_control['uid'])
        df_treat = df_dt_treat['active_mins'].divide(df_usr_treat['uid'])

        print('For df_control, its normal distribution test is {}'.format(stats.shapiro(df_control)))
        print('For df_treat, its normal distribution test is {}'.format(stats.shapiro(df_treat)))

        return (df_clean, df_control, df_treat)

