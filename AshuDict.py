
class Ashu:
    df_dict = dict()

    def put_df_key(key, df):
        Ashu.df_dict[key] = df

    def get_df_key(key):
        return Ashu.df_dict[key]
