from AshuDict import Ashu
import pandas as pd


def a1():
    df = pd.read_csv('data.csv')
    Ashu.put_df_key("ashu", df)
    x = Ashu.get_df_key("ashu")
    print(x.head())


def a2():
    df1 = pd.read_csv('summary.csv')
    Ashu.put_df_key("nidhi", df1)


def a3():
    y = Ashu.get_df_key("ashu")
    print(y.head())


def a4():
    z = Ashu.get_df_key("ashu")
    print(z.head())


def a5():
    a = Ashu.get_df_key("nidhi")
    print(a.head())


def a6():
    b = Ashu.get_df_key("nidhi")
    print(b.head())


def main():
    a1()
    a2()
    a3()
    a4()
    a5()
    a6()


if __name__ == '__main__':
    main()
