# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from scipy import stats


def drop_columns(df, *args):
    '''
    input: 
    df: pandas dataframe 
    *args: flexible args as strings, ex 'str1','str2', etc
    returns:
    the dataframe with columns specified dropped 
    '''
    cols = [col for col in args]
    df.drop(columns=cols, inplace=True)


def create_masks(df, cols, conds, relations):
    '''
    input: 
    df: pandas dataframe 
    cols: a list of cols, ex, ['col1','col2', etc.]
    cods: a list of conds, ex, [cond1, cond2, etc.]
    relations: a list of np condition, ex, ['np.equal', 'np.greater', ..]
    returns:
    a list of masks and access each masks with list index 
    '''
    # relations a np numpy operator
    masks = []
    for i, col in enumerate(cols):
        mask = relations[i](df[col], conds[i])
        masks.append(mask)
    return masks


def r2(x, y):
    '''
    input:
    x: df column for x axis
    y: df column for y axis
    return:
    r2 for regression
    '''
    return stats.pearsonr(x, y)[0] ** 2


def split_rows(df, col1, col2, sep):
    '''
    input: 
    df: dataframe to use
    col1 and col2 (use col2 to split )
    return:
    a df table with col1 as common col and col2 split into multiple rows
    '''
    series = [pd.Series(row[col1], row[col2].split(sep))
              for _, row in df.iterrows()]
    table = pd.concat(series).reset_index()
    rename_columns(table, {0: col1, 'index': col2})
    return table


def object_binary(df, col, *args):
    '''
    input: 
    df: pandas dataframe 
    col: the col that you want to convert to dummy
    flexible argument str: 'str1', 'str2'
    return:
    binary (1, 0 ) column for original col 
    '''
    conds = [cond for cond in args]
    new_col = df[col].apply(lambda x: 1 if x in conds else 0)
    return new_col


def drop_repeatrows(df, col):
    '''
    input:
    col: a list of colname ['col1','col2', ...] for repeated columns only
    return:
    a dataframe with zero repeat col for specificed cols 
    '''
    df.drop_duplicates(subset=col, inplace=True)


def rename_columns(df, dict_map):
    '''
    input: 
    df: pandas data frame 
    dict_map: a dictionary {'old name':'new name', 'old name': 'new name'...}
    return:
    rename the columns in 'old name' for dict_map 
    '''
    df.rename(columns=dict_map, inplace=True)


def stringtonum(df, cols, chars):
    '''
    input: 
    df: pandas dataframe 
    cols: a list of colums ['col1', 'col2', etc]
    chars: a string 's''
    returns:
    the columns with the unncessary symbols removed and turned into float  
    '''
    table = str.maketrans(dict.fromkeys(chars))
    if len(cols) == 1:
        converted = df[cols[0]].dropna().apply(
            lambda x: float(x.translate(table)))
        df[cols[0]] = converted
    else:
        converted = df.loc[:, cols].dropna().applymap(
            lambda x: float(x.translate(table)))
        df.loc[:, cols] = converted


def merge_tables(df1, df2, common_col, how):
    '''
    input: 
    df1, df2: pandas dataframe with common column
    common_col: common cols either a string or a list of strings 
    how: a string: inner, left, and outer 
    return:
    merged table 
    '''
    merged = df1.merge(df2, on=common_col, how=how)
    return merged


def drop_NA(df, cols):
    '''
    input:
    df: pandas dataframe 
    cols: cols as a list of col string names 
    return:
    remove NA from the specific list of cols in df and 
    returns the dataframe with NAs dropped for specified columns 
    '''
    df.dropna(subset=cols, inplace=True)


def create_list(df, col, sep):
    '''
    df: pandas dataframe 
    col: a str, col name to split string into a list separated by sep 
    sep: a string such as ' ', '|', ',', etc.
    return:
    a new col with the col separated into a list of strings 
    '''
    new_col = df[col].apply(lambda x: x.split(sep))
    return new_col


def binning(x):
    '''
    input:
    x is numeric 
    output: 
    bin into 4 intervals:
    "< = 50 min"
    "50 to 100"
    "100 to 150"
    "150 to 200"
    '''
    if x <= 50:
        x = 'under 50 min'
    elif x <= 100:
        x = '50 to 100 min'
    elif x <= 150:
        x = '100 to 150 min'
    else:
        x = 'over 150 min'
    return x
    