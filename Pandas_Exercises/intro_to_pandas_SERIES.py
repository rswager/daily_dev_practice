import random

import pandas as pd
import numpy as np


def insert_tab(panda_in, indent_in):
    if isinstance(panda_in, pd.Series) and len(panda_in) > 0:
        return panda_in.to_string().replace("\n", f"\n{indent_in}")
    else:
        return "EMPTY"


if __name__ == '__main__':
    # ------------------ General Population of Data -------------------
    print("############################################################\n"
          "Series - 1D unlabeled Array (like a normal array)")
    s_unlabeled_array = pd.Series([10, 20, 30])

    print(f"\tYou can print the series: \n\tprint(s_unlabeled_array)")
    print('\tOUTPUT:\n\t\t', end='')
    print(insert_tab(s_unlabeled_array, "\t\t"))

    print("Series - 1D Labeled Array")
    # create the Series
    s_labeled_array = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print(f"\tYou can print the series: \n\tprint(s_labeled_array)")
    print('\tOUTPUT:\n\t\t', end='')
    print(insert_tab(s_labeled_array, "\t\t"))

    print("Series - Dictionaries")
    s_dict = pd.Series({'a': 10, 'b': 20, 'c': 30})
    print(f"\tYou can print the series: \n\tprint(s_dict)")
    print('\tOUTPUT:\n\t\t', end='')
    print(insert_tab(s_dict, "\t\t"))

    print("Series - NumPy array")
    s_numpy = pd.Series(np.random.randn(3))
    print(f"\tYou can print the series: \n\tprint(s_numpy)")
    print('\tOUTPUT:\n\t\t', end='')
    print(insert_tab(s_numpy, "\t\t"))

    print("Series - Scalar Value (single numerical values)")
    s_scalar = pd.Series(3.14, index=['x', 'y', 'z'])
    print(f"\tYou can print the series: \n\tprint(s_scalar)")
    print('\tOUTPUT:\n\t\t', end='')
    print(insert_tab(s_scalar, "\t\t"))

    # Going to shove all of these into an array so I don't have to duplicate things
    all_s = {'s_unlabeled_array': s_unlabeled_array,
             's_labeled_array': s_labeled_array,
             's_dict': s_dict,
             's_numpy': s_numpy,
             's_scalar': s_scalar}

    # ------------------ Access Information about Data -------------------
    print("\n############################################################")
    print(f"You can get the data type by calling .dtype")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.dtype")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].dtype
        print(temp)

    print("\n############################################################")
    print(f"You can get the index by calling .index")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.index")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].index
        print(temp)

    print("\n############################################################")
    print(f"You can get the list of values by calling .values")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.values")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].values
        print(temp)

    print("############################################################")
    print(f"You can access the value by the Key value:\n")
    for s_type in all_s.keys():
        print(f'\t{s_type}')
        for key in all_s[s_type].keys():
            print(f"\t\t{s_type}[{key}] = {all_s[s_type][key]}")
        print()

    print("############################################################")
    print(f"You can access the value by the Index value:\n")
    for s_type in all_s.keys():
        print(f'\t{s_type}')
        for index in range(len(all_s[s_type])):
            print(f"\t\t{s_type}[{index}] = {all_s[s_type].iloc[index]}")
        print()

    # ------------------ Filtering Information ---- -------------------
    print("############################################################")
    print(f"You can filter using a statement!:")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}[{s_type} >= 20]")
        print('\tOUTPUT:\n\t\t', end='')
        temp = pd.Series(all_s[s_type][all_s[s_type] >= 20])
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"You can filter using a where statement!:")

    print(f"\n\tWhen using a where statement you will be left with nan's")
    print(f"\ts_unlabeled_array.where(s_unlabeled_array >= 20)")
    print('\tOUTPUT:\n\t\t', end='')
    temp = s_unlabeled_array.where(s_unlabeled_array >= 20)
    print(insert_tab(temp, "\t\t"))

    print(f"\n\tYou can drop the nan's though", end='')
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.where({s_type} >= 20).dropna()")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].where(all_s[s_type] >= 20).dropna()
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"\n\tYou can also  fill nan's", end='')
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.where({s_type} >= 20).fillna(0)")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].where(all_s[s_type] >= 20).fillna(0)
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"\n\tYou can also  check to see if a column is a nan with .isna()", end='')
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.where({s_type} >= 20).isna()")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].where(all_s[s_type] >= 20).isna()
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"You can filter using and(&)/or(|) where statement, but you need to use () a lot!:")
    print(f"\t~WHERE ((data >= 20) OR ((data>0) AND (data<10))) AND (data != 3.14)")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.where((({s_type} >= 20) | (({s_type} > 0) & ({s_type} < 10))) & ({s_type} != 3.14)).dropna()")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].where(((all_s[s_type] >= 20) | ((all_s[s_type] > 0) & (all_s[s_type] < 10))) & (all_s[s_type] != 3.14)).dropna()
        print(insert_tab(temp, "\t\t"))

    # -------------------------- Std Expressions ------------------------
    print("\n############################################################")
    print(f"You can get first n elements using .head()")
    print("\n\tIf you enter n > len(Series) it will just return the series")
    print("\ts_unlabeled_array.head(n=5)")
    print('\tOUTPUT:\n\t\t', end='')
    print(insert_tab(s_unlabeled_array.head(n=5), "\t\t"))

    print(f"Other wise it will return n elements from the start of the Series")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.head(1)")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].head(1)
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"You can get last n elements using .tail()")
    print("\n\tIf you enter n > len(Series) it will just return the series")
    print("\ts_unlabeled_array.tail(n=5)")
    print('\tOUTPUT:\n\t\t', end='')
    print(insert_tab(s_unlabeled_array.tail(n=5), "\t\t"))

    print(f"Other wise it will return n elements from the end of the Series")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.tail(1)")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].tail(1)
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"You can get a statistical descriptions of a set using .describe()")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.describe()")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].describe()
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"You can git a list of unique values using unique()")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.unique()")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].unique()
        print(temp)

    print("\n############################################################")
    print(f"You can get the count for each value using value_counts()")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.value_counts()")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].value_counts()
        print(insert_tab(temp, "\t\t"))

    # -------------------------- Operational Expressions ------------------
    print("\n############################################################")
    print(f"You can do element wise operations like *")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}*2()")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type]*2
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"You can do element wise operations like adding 2 together (need to have matching labels!")
    for index in range(len(all_s)):
        if index < len(all_s)-1:
            print(f"\n\t{list(all_s)[index]} + {list(all_s)[index+1]}")
            print('\tOUTPUT:\n\t\t', end='')
            temp = all_s[list(all_s)[index]] + all_s[list(all_s)[index+1]]
            print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"You can add constancts using the .add() function")
    for s_type in all_s.keys():
        print(f"\n\t{s_type}.add(2)")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].add(2)
        print(insert_tab(temp, "\t\t"))

    # -------------------------- Sorting Expressions ------------------
    print("\n############################################################")
    print(f"You can sort information by index using sort_index()")
    for s_type in all_s.keys():
        ascend = bool(random.getrandbits(1))
        print(f"\n\t{s_type}.sort_index(ascending={ascend})")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].sort_index(ascending=ascend)
        print(insert_tab(temp, "\t\t"))

    print("\n############################################################")
    print(f"You can sort information by value using sort_values()")
    for s_type in all_s.keys():
        ascend = bool(random.getrandbits(1))
        print(f"\n\t{s_type}.sort_values(ascending={ascend})")
        print('\tOUTPUT:\n\t\t', end='')
        temp = all_s[s_type].sort_values(ascending=ascend)
        print(insert_tab(temp, "\t\t"))

    # -------------------------- Chained Expressions ------------------
    print("\n############################################################")
    print(f"You can chain operations!")
    print(f"\tWHERE ((data >= 20) OR ((data>0) AND (data<10))) AND (data != 3.14)."
          f"dropna().sort_values(ascnding=random.bool).head(1)")
    for s_type in all_s.keys():
        ascend = bool(random.getrandbits(1))
        print(f"\n\t{s_type}.where((({s_type} >= 20) | (({s_type} > 0) & ({s_type} < 10))) & ({s_type} "
              f"!= 3.14)).dropna().sort_values(ascending={ascend}).head(1)")
        print('\tOUTPUT:\n\t\t', end='')
        # you can also store the condition
        condition = (((all_s[s_type] >= 20) | ((all_s[s_type] > 0) & (all_s[s_type] < 10))) & (all_s[s_type] != 3.14))
        temp = all_s[s_type].where(condition).dropna().sort_values(ascending=ascend).head(1)
        print(insert_tab(temp, "\t\t"))
