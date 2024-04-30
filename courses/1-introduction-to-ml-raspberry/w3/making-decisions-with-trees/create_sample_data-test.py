
# Create Sample of Data
import pandas as pd
import numpy as np
Emotion=['sick','sick','sick','notsick','notsick','sick','notsick','notsick']
Temperature = ['under','over','under','under','over','over','under','over']
StayHome=['N','Y','Y','N','Y','N','N','Y']
df=pd.DataFrame (list(zip(Emotion,Temperature,StayHome)),
                columns=["Emotion","Temperature","StayHome"])
print(df.sort_values(['Temperature','StayHome']).reset_index(drop=True))

# Deciding where to split the data at the root node. 
## (EMOTION: sick or notsick)
print("====EMOTION=====")
print(df[df.iloc[:,0]=='sick'].sort_values('StayHome'))
print(df[df.iloc[:,0]=='notsick'].sort_values('StayHome'))

## (TEMPERATURE: under or over)
print("====TEMPERATURE=====")
print(df[df.iloc[:,1]=='under'].sort_values('StayHome'))
print(df[df.iloc[:,1]=='over'].sort_values('StayHome'))

## An Iteration of the Two
print("===Iteration=====")
### Emotion
print("====EMOTION=====")
## Get the non duplicated values in the list emotion
unique_emotion_list=list(set(Emotion))
emotion_index = df.columns.get_loc('Emotion')
for emotion in unique_emotion_list:
    print(df[df.iloc[:,emotion_index]==emotion].sort_values('StayHome'))
### Temperature
print("====TEMPERATURE=====")
## Get the non duplicated values in the list temperature
unique_temperature_list=list(set(Temperature))
emotion_index = df.columns.get_loc('Temperature')
for temperature in unique_temperature_list:
    print(df[df.iloc[:,1]==temperature].sort_values('StayHome'))

# Deciding where to split the data from root but we have not split it yet

#Identify Outcome Variable
print("======Deciding Decision Nodes======")
outcome_variable='StayHome'
## Create a list of index without the outcome column
outcome = df.columns.get_loc(outcome_variable)
column_list = list(range(len(df.columns)))
## Remove the outcome index
column_list.remove(outcome)
#create copy of data and get unique values in each feature
new_df = df
names, count = np.unique(new_df.iloc[:,column_list[0]], return_counts = True)
## Return how many unique features there are in this split
split_df = len(names)
for name in range(0, len(names)):
    print(f"We have a split on feature: ({new_df.columns[0]}), where it equals ({names[name]}), and has {count[name]} observations")

# Split the data now based on the new identifier
for name in names:
    # name = sick or notsick
    print("🐍======================================")
    print(new_df[new_df.iloc[:,column_list[0]]==name],"\n","\n")

## Using Gianna Measure (Gini 🐍24)
print("🐍🐍🐍🐍🐍 Gianna Mamba")
split_data_sick=new_df[new_df.iloc[:,column_list[0]]==names[1]]
split_data_nonsick=new_df[new_df.iloc[:,column_list[0]]==names[0]]
print(split_data_sick)
print(split_data_nonsick)
## get the unique outcome values
    #This will be used later when we computed the weighted gini value
print("=====unique values========")
values = np.unique(df.iloc[:,outcome])
den_s_sick = len(split_data_sick)
den_s_nonsick = len(split_data_nonsick)
impurity = 0

print("=====gini impurity values========")
for value in values:
    # value = Y, N
    probability_sick = split_data_sick.iloc[:,outcome].eq(value).sum()/den_s_sick
    impurity += probability_sick * (1 - probability_sick)
print ("The gini impurity index is: ",impurity,"for \n \n", split_data_sick.sort_values("StayHome").reset_index(drop=True))

print("=====gini impurity values========")
impurity = 0
for value in values:
    # value = Y, N
    probablity_non_sick = split_data_nonsick.iloc[:,outcome].eq(value).sum()/den_s_nonsick
    impurity += probablity_non_sick * (1 - probablity_non_sick)

print ("The gini impurity index is: ",impurity,"for \n \n", split_data_nonsick.sort_values("StayHome").reset_index(drop=True))

    ## Get the weighed values
# # Weight each split by it's proportion to the data before the split
print("\n=====identifying weights========")
# ## Create empty list to hold each splits impurity and split count
gini_metric = []
den_s_split = []

for name in names:
    split_data = new_df[new_df.iloc[:,column_list[0]]==name]
    print(f"===={name}=====")
    print(split_data)
    values = np.unique(df.iloc[:,outcome])
    print(f"**value****")
    print(values)
    #This will be used later when we computed the weighted gini value
    denS = len(split_data)
    ## Length of Split Data
    print(f"**length of new split data****")
    print(denS)
    impurity = 0

    for value in values:
        p = split_data.iloc[:,outcome].eq(value).sum()/denS
        impurity += p * (1-p)
    gini_metric.append(impurity)
    den_s_split.append(denS)
    print("**geni metric****")
    print(gini_metric)
    print("**denS split****")
    print(den_s_split)

feature = split_df
# ## get the proportion of the split for current feature
den_split1 = [x/sum(den_s_split[0:feature]) for x in den_s_split[0:feature]]
weighted_gini = sum(np.asarray(den_split1) * np.asarray(gini_metric[0:feature]))

print("The weighted gini impurity measure is:",weighted_gini)
