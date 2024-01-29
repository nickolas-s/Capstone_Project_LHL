# Adds n columns from the split string dataframe to the original dataframe

def col_loop(df, start_index, name_list, data_df):
    i = 0
    for name in name_list:
        df.insert(
            loc = start_index,
            column = name,
            value = data_df[i]
        )

        i += 1
        start_index += 1
        

# Transforms the 'Estimated owners' string into an integer (average)

def format_est_owners(sting):
    str_to_list = sting.split()
    return (int(str_to_list[-1])+int(str_to_list[0]))//2