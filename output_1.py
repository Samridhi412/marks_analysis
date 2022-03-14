import sys
import logging
import numpy as np
import pandas as pd
# mylogs = logging.getLogger(__name__)
# file = logging.FileHandler("101916086-log.txt")
# file.setLevel(logging.INFO)
# fileformat = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s",datefmt="%H:%M:%S")
# file.setFormatter(fileformat)

# mylogs.addHandler(file)
logging.basicConfig(filename="101916086-log.txt", level=logging.INFO)
def preprocess():
    para=len(sys.argv)
    if para!=2:
        print(para)
        logging.error("Invalid number of arguments,needed parameters: 1")
        print("Invalid number of arguments,needed parameters: 1")
        logging.shutdown()     
    f = sys.argv[1]
    df = pd.read_csv(f)
    if len(df.columns)!=3:
        logging.error("No of inappropriate columns")
        print("No of inappropriate columns")      
        logging.shutdown() 
    s1 = pd.Series(df['Marks'])
    df["Marks"].unique()
    col=['RollNumber', 'Submission', 'Marks']
    arr=np.array(col)
    columns=df.columns
    lst=[]
    for i in columns:
        lst.append(i)
    arr1=np.array(lst)
    comparison = arr == arr1
    equal_arrays = comparison.all()
    if not equal_arrays:
        logging.error("Enter correct column names RollNumber,Submission,Marks")
        print("Enter correct column names RollNumber,Submission,Marks")
        logging.shutdown() 
    # count=0
    # val=0
    # num=0
    # nil=0

    # for i in df['Marks']:
    #     if i=='X':
    #         count+=1
    #     elif i=='-':
    #         val+=1
    #     elif i=='NAN'or i=='nan':
    #         nil+=1
    #     elif i=='13'or i=='14'or i=='15' or i=='0':
    #         num+=1


    # no_num=count    
    # no_null=nil
    # no_miss=val
    # index_names = df[ (df['Marks'] == 'X')].index
    # df.drop(index_names,inplace=True)
    # in_names=df[(df['Marks']=='NAN') | (df['Marks']=='-')].index
    # df.drop(in_names,inplace=True)
    # df.dropna(inplace=True)
    df['Marks'].unique()
    df
    # print(num)
    # print(no_miss)
    # print(no_num)
    # print(no_null)
    df.columns
    df.isnull().sum()
    # df['Marks'].isnumeric()
    df['Marks'].unique()
#     print(df)
    missing_value={}
    notnumeric_value={}
    subjects=df["Submission"].unique()
    for i in subjects:
        missing_value[i]=0
        notnumeric_value[i]=0
    col=["RollNumber","Marks"]
    for j in col:
        l=[]
        for i in range(len(df[j])):

            if(str(df[j][i])=="nan" or str(df[j][i])=="NAN"):
                l.append(i)
                a=df.at[i,"Submission"]
                b=missing_value[a]
                b=b+1
                missing_value[a]=b
                continue
            if np.char.isnumeric(str(df[j][i]))!=True:
                a=df.at[i,"Submission"]
                b=notnumeric_value[a]
                b=b+1
                notnumeric_value[a]=b
                l.append(i)
                continue
        for i in l:
            a=df.loc[i]
            df.drop(i,inplace=True)   
            logging.warning(f'{j} are not numeric {a}')
        df.reset_index(drop=True,inplace=True)
        df.isnull().sum()
        data_columns=['Marks']
        # num_df = (df.drop(data_columns, axis=1).join(df[data_columns].apply(pd.to_numeric, errors='coerce')))
#         df = df.reset_index(drop=True)
        df['Marks'].unique()
    li=[]
    for i in range(len(df["Submission"])):
        a=df["Submission"][i]
        if type(a)!=str:
            li.append(i)
    for i in li:
            a=df.loc[i]
            df.drop(i,inplace=True)   
            logging.warning(f'subject is not a string {a}')
    df.reset_index(drop=True,inplace=True)            
        #     print(missing_value)
        #     print(notnumeric_value)
        # s1=pd.Series(df['Submission'].unique())
        # s2=pd.Series(df['RollNumber'].unique())
    roll_num=df["RollNumber"].unique()
    l2=[]
    for i in range(len(roll_num)):
        l2.append(0) 
    l1=[]
    for i in roll_num:
        l1.append(i)    
    d1={"RollNumber":l1}  
    for i in subjects:
        d1[i]=l2  
    new_df=pd.DataFrame(d1)
    index = new_df.index
    for i in range(df.shape[0]):
        dt=df.iloc[i]
        rno=dt["RollNumber"]
        sub=dt["Submission"]
        mark=dt["Marks"]
        c=new_df["RollNumber"]==rno
        ind= index[c]
        ind=ind[0]
        new_df.at[ind,sub]=mark
        miss_val=[]
    for key,value in missing_value.items():
        miss_val.append(value)
        logging.info('{key} ---> {value} missing value')
    nonnum_val=[]
    for key,val in notnumeric_value.items():
        nonnum_val.append(val)   
        logging.warning(f'{key} ---> {val} non numeric value')
    logging.info(f"missing values corresponding subjects are: {miss_val}")
    logging.info(f"non_numeric values corresponding subjects are: {nonnum_val}")        
#         new_df    
    new_df.to_csv("101916086-output.csv")
if __name__=="__main__":
    try:
        preprocess()

    except OSError:
        logging.error("File not found")
        print("File not found")
    logging.shutdown()    


    