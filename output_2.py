from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import sys,getopt
import csv
import random
import os
import logging
import seaborn as sns
import colorama
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
logging.basicConfig(filename="101916086-log.txt", level=logging.INFO)
if __name__=="__main__":
    try:
        para=len(sys.argv)
        if para!=2:
            print(para)
            logging.error("Invalid number of arguments,needed parameters: 1")
            print("Invalid number of arguments,needed parameters: 1")
            logging.shutdown()     
        f = sys.argv[1]
        df=pd.read_csv("input.csv")
        new_df = pd.read_csv(f)
        Argument=new_df.isnull().sum()
        f1 = open("101916086-statistics.txt", "a")
        f1.write(str(Argument))
        f1.write("\n")
        new_df.describe().to_csv("101916086-statistics.txt", header=None, index=None, sep=' ', mode='a')
        f1.write("\n")
        col=new_df.columns
        subject_list=[]
        for i in col:
            subject_list.append(i)  
        subject_list.remove("RollNumber") 
        h1=new_df.iloc[:,1:].plot.hist()

        h1.get_figure().savefig("101916086_histogram_combine.png")
        hisplot=[]
        for i in subject_list:
            li=new_df[i].tolist()
            hisplot.append(li)
        plt.figure(figsize=(10,7)) 
        plt.hist(hisplot,label=subject_list)
        plt.legend()
        plt.xlabel("Marks of Assignments")
        plt.title("Histogram of Mark Ananlysis")
        plt.ylabel("Frequency of Students")
        plt.savefig('101916086-histogram.png')
        mean_marks=[]
        for i in subject_list:
            mean_marks.append(new_df[i].mean())
        plt.pie(mean_marks,labels=subject_list)
        plt.title("Mean marks of various subjects:")
        plt.savefig('101916086-pie_plot.png')
        line_plot=[]
        for i in subject_list:
            li=new_df[i].tolist()
            line_plot.append(li)
        plt.figure(figsize=(10,7))     
        plt.plot(line_plot)
        plt.savefig('101916086-line_plot.png')
        med=[]
        for i in subject_list:
            med.append(new_df[i].median())
        f1.write(f"Median of subjects is: {med}")
        f1.write("/n")          
        sd=[]
        for i in subject_list:
            sd.append(new_df[i].std())
        f1.write(f"Standard Deviation of subjects is: {sd}")
        f1.write("/n")        
        maxi=[]
        for i in subject_list:
            maxi.append(new_df[i].max())
        f1.write(f"Maximum of subjects is: {maxi}")
        f1.write("/n")       
        mini=[]
        for i in subject_list:
            mini.append(new_df[i].min())
        f1.write(f"Minimum of subjects is: {mini}")
        f1.write("/n")      
        mean=[]
        for i in subject_list:
            mean.append(new_df[i].mean())
        f1.write(f"Mean of subjects is: {mean}")
        f1.write("/n") 
        dictionary={"Subject-name":subject_list,"Medain":med,"Mean":mean,"Max_values":maxi,"Min_values":mini,"StandardDeviation":sd}
        stat_anal=pd.DataFrame(data=dictionary)
        stat_anal
        f1.write("Statistics Analysis:")
        stat_anal.to_csv("101916086-statistics.txt", header=None, index=None, sep=' ', mode='a')
        # f1.write(stat_anal)
        f1.write("\n")
        # fig, ax = plt.subplots()
        # new_df.iloc[:,1:].hist(ax=ax)
        # plt.savefig('101916086-sub_plots.png') 
        df2=pd.DataFrame(data=df.iloc[:,1])
        df2
        plt.figure(figsize=(14,7)) 
        sns.countplot(x ='Submission',hue = "Submission", data = df2,palette="pastel")
        plt.savefig('101916086-count_plot.png')      
        fig = plt.figure(figsize = (10, 5))
        type(df.iloc[0,1])
        # print(mean)
        df3 = pd.DataFrame({"Subjects": subject_list,
                           "Mean_Marks": mean})
        df3
        df3.sort_values('Mean_Marks')
        sns.barplot(x='Subjects',
                    y="Mean_Marks", data=df3,order=df3.sort_values('Mean_Marks',ascending = False).Subjects)
        plt.legend()
        plt.title("Mean Marks Ananlysis Corresponding to subject")
        plt.savefig('101916086-bar_plot.png')  
                 
#         print(mean)
#         print(med)
#         print(sd)
#         print(maxi)
#         print(mini)
                 
    except OSError:
        logging.error("File not found")
        print("File not found")
    logging.shutdown()    

