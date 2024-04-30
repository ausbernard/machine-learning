import pandas as pd
import numpy as np

Emotion=['sick','sick','sick','notsick','notsick','sick','notsick','notsick']
Temperature = ['under','over','under','under','over','over','under','over']
StayHome=['N','Y','Y','N','Y','N','N','Y']
df=pd.DataFrame (list(zip(Emotion,Temperature,StayHome)),
                columns=["Emotion","Temperature","StayHome"])

print("=ORIGINAL DATA=====")
print(df.sort_values(['Temperature','StayHome']).reset_index(drop=True))
print("------------------------")

# Establish the Gini Function
def gini_impurity_dens_calculator(split_data, outcome):
    # Get unique Outcome values
    values = np.unique(split_data.iloc[:,outcome])
    denS = len(split_data)
    impurity = 0
    for value in values:
        p = split_data.iloc[:,outcome].eq(value).sum()/denS
        impurity += p * (1 - p)
    
    return (impurity, denS)

# Tree
def simple_tree(df, Outcome):
    if type(Outcome) == str:
        # empty list to hold information
        split_df_list = []
        gini_metric = []
        weighted_gini_list = []
        den_split = []
        split_data = []
        split_data_index = []
        P = []

        # create a list of index without the outcome column
        outcome = df.columns.get_loc(Outcome)
        outcome_removed_column_list = list(range(len(df.columns)))
        outcome_removed_column_list.remove(outcome)

        # let the looping begin
        for column in outcome_removed_column_list:
            # create a copy of the data and get unique values in each feature
            new_copy = df
            names,count = np.unique(new_copy.iloc[:,column], return_counts = True)
            # desire: return the number of splits per feature
            split_df_list.append(len(names))

            for name in names:
                # return the columns such that it equals the split criteria
                split_df = new_copy[new_copy.iloc[:,column]==name]
                # add df to list
                split_data.append(split_df)
                # keep track of columns split data set
                index = pd.DataFrame(list([column]))
                split_data_index.append(index)
        
        # get the unique outcome variables
        value = np.unique(df.iloc[:,outcome])

        for data in split_data:
            # calculate the gini at each split
            impurity, denS = gini_impurity_dens_calculator(data,outcome)
            # append results to list
            gini_metric.append(impurity)
            den_split.append(denS)
        
        # iterate on the number of splits per feature to get weighted gini metric
        for feature in split_df_list:
            # calculate the proportion of the split for current feature
            den_split_value = [x/sum(den_split[0:feature]) for x in den_split[0:feature]]
            weighted_gini = sum(np.asarray(den_split_value) * np.asarray(gini_metric[0:feature]))
            # add weighed gini
            weighted_gini_list.append(weighted_gini)
            # remove the gini and feature count split for the next iteration
            del(gini_metric[0:feature], den_split[0:feature])
                              
    else: 
        print("Place Outcome Variable Name in \'Single'\ quotes")
    
    f_column = weighted_gini_list.index(min(weighted_gini_list))
    # return the name
    best_split = df.columns[f_column]
    return (outcome_removed_column_list, weighted_gini_list, split_data, split_data_index, f_column)

def additional_leaf(df,Outcome):
    #root node split
    column_list,weighted_gini,split_data,split_index,best_split=simple_tree(df,Outcome)
    # Grab the best split and then create the leaf leaf and right leaf split
    #hold the resulting datasets
    final_data_set=list()
    
    # col that holds the index for each column (for instance col 1 (Emotion) has index 1,2 which would help us find the split data)
    index = pd.concat(split_index, ignore_index=True)
    #grab the index for the best split
    best_split_index=list(index[index.iloc[:,0]==best_split].index)
    
    # for each split data set re run the simpletree
    for n in best_split_index:
        leaf_data=split_data[n]
        leaf_data.drop(leaf_data.columns[best_split],axis='columns',inplace=True)
        column_list2,weighted_gini2,split_data2,split_index2,best_split2=simple_tree(leaf_data,Outcome)
        #grab the index for the best split
        best_split_index=list(index[index.iloc[:,0]==best_split2].index)
        for i in best_split_index:
            print(pd.DataFrame(split_data2[i]))
            final_data_set.append(pd.DataFrame(split_data2[i]))
            print("-----------------")
    return(final_data_set,n,best_split2)

if __name__ == "__main__":
    final_data_set,n,col=additional_leaf(df,"StayHome")
        
    
    