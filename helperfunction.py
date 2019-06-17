# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 

def split_rows(df, col1, col2, sep):
    series = [pd.Series(row[col1],row[col2].split(sep))
    for _,row in df.iterrows()]
    table = pd.concat(series).reset_index()
    rename_columns(table, {0: col1, 'index': col2})
    return table


def object_binary(df, col, *args):
    conds = [cond for cond in args]
    new_col = df[col].apply(lambda x: 1 if x in conds else 0)
    return new_col
    
def drop_repeatrows(df, col):
    df.drop_duplicates(subset = col, inplace = True)
  
def drop_columns(df, *args):
    cols = [col for col in args]
    df.drop(columns = cols, inplace = True)

def rename_columns(df, dict_map):
    df.rename(columns = dict_map, inplace = True)
  

def stringtonum(df, cols, chars):
    table = str.maketrans(dict.fromkeys(chars))
    if len(cols)==1:
        converted = df[cols[0]].dropna().apply(lambda x: int(x.translate(table))) 
        df[cols[0]] = converted
    else:
        converted = df.loc[:,cols].dropna().applymap(lambda x: int(x.translate(table)))
        df.loc[:,cols] = converted

def merge_tables(df1,df2, common_col,how):
    merged = df1.merge(df2,on = common_col, how = how )
    return merged

def drop_NA(df, cols):
    df.dropna(subset = cols, inplace = True)
    

def create_masks(df, cols, conds, relations):
    # relations a np numpy operator 
    masks = []
    for i,col in enumerate(cols):
        mask = relations[i](df[col], conds[i])
        masks.append(mask)
    return masks        

def create_list(df, col, sep):
    new_col = df[col].apply(lambda x: x.split(sep))
    return new_col
    
    