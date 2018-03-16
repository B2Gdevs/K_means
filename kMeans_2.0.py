import pandas as pd
import math
import numpy as np


def generate_centroids(inital_dataframe, k):
    
    df = inital_dataframe.iloc[:, 0:inital_dataframe.shape[1]-1]
    centroid_frame = pd.DataFrame(np.random.randint(df.values.min(),df.values.max(),size=(k, inital_dataframe.shape[1])))
    
    return centroid_frame
    
def mean(centroids, initial_dataframe):
    copy_centroids = centroids.copy()
    
    for i in range(0, copy_centroids.shape[0]):
        #This is a boolean way to get only the values from the real frame for each cluster
        df = initial_dataframe[initial_dataframe[initial_dataframe.columns[-1]] == i]
        #shorten it so we dont get categorical data now.
        df = df.iloc[:, 0:initial_dataframe.shape[1]-1]
        #add in the previous centroid for calculation
        df = df.append( copy_centroids.iloc[i])
        #do the calculation and the reset the centroid
        copy_centroids.iloc[i] = df.mean()
        
    return copy_centroids
    
def kMeans(initial_dataframe, k = 3, epsilon = .1):
    
    centroids = generate_centroids(initial_dataframe, k)
    
    frame_without_cluster_class = initial_dataframe.copy()   
    
    initial_dataframe['cluster'] = np.NaN

    while True:
        #assigning clusters to every point in the dataset
        #remember that you must have only numerical values when doing the 
        #distance
        for index_of_points, point_in_data in frame_without_cluster_class.iterrows():
            distances = []
            for index_of_centroid, point_in_centroid in centroids.iterrows():
                distance = np.linalg.norm(point_in_data - point_in_centroid)
                distances.append(distance)
                 #I know that the index of the distances will be the same as the index
                 #in the centroid frame.  This is because there can only be as
                    #many distances each point can have that there are centroids
            cluster_assignment = distances.index(min(distances))
            #Have to use iloc and seperate by comma because this is the assignment 
            #operation and not the view operation [] []
            data.iloc[index_of_points, data.shape[1]-1] = cluster_assignment
        
            #We need the means now
        new_centroids = mean(centroids, data)
        print(np.linalg.norm(new_centroids - centroids))
        if np.linalg.norm(new_centroids - centroids) <= epsilon:
            break
        else:
            centroids = new_centroids
       

data = pd.read_csv("values.txt", header = None, delim_whitespace = True)

kMeans(data, 3, .1)




        
