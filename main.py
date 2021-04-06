from class_31_hyperparameters import HyperParameters
from class_32_import_data import ImportData
from class_33_eda import EDA
from class_34_join_data import JoinData
from class_35_hypothesis import Hypothesis


def main():
    """:arg
    All program running here by sequence

    1.import data
    2.Through EDA delete outliers
    3.Join data and split control and treatment

    """
    class_import = ImportData()
    (df_t1, df_t2, df_t3, df_t4) = class_import.import_data()

    class_eda = EDA()
    # clean df_t1 dataframe by deleting outliers
    df_t1 = class_eda.outlier_eda(df_t1)

    class_join = JoinData()
    # outer join t1 table and t2 table
    df_clean, df_control, df_treat = class_join.join_data_dt(df_t1, df_t2, df_t3, df_t4)

    class_hypo = Hypothesis()
    (t_value, p_two, degree_free
     , t_stat, p_value, upper_bound, lower_bound) = class_hypo.ttest_ind(df_control, df_treat)


    return (df_t1, df_t2, df_t3, df_t4, df_clean, df_control, df_treat
            , t_value, p_two, degree_free, t_stat, p_value, upper_bound, lower_bound)


if __name__=="__main__":
    """:arg
    """
    (df_t1, df_t2, df_t3, df_t4, df_clean, df_control, df_treat
     , t_value, p_two, degree_free, t_stat, p_value, upper_bound, lower_bound) = main()

    print('OVER')