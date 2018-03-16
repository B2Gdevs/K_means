import pandas as pd
import math
import numpy as np

#first we need to generate k number of random points in the dataframe
#these centroids will be in there own dataframe
#The clusters will just be the index of the centroid
#def generate_centroids does this

#second we need to get the distance between the points in the centroid_frame 
#and the initial dataframe

#to get the mean of the cluster will will just throw away all portions of a
#copied dataframe that do not have the cluster number and then say 
#dataframe.mean() and put in to the centroid_frame
#def get_centroid_means does this.

#the only way to get the convergeance I can think of is if we get the
#mean of the clusters and check the difference between each previous
#centroid to its current centroid and if it is less than a certain threshold
#maybe 0.1 then stop the looping.

def generate_centroids(inital_dataframe, k):
    df = inital_dataframe.iloc[:, 0:inital_dataframe.shape[1]-1]
    centroid_frame = pd.DataFrame(np.random.randint(df.values.min(),df.values.max(),size=(k, inital_dataframe.shape[1])))
    
    return centroid_frame
    
def distance_between_two_points(point1, point2):
    distance = np.linalg.norm(point1 - point2)
    print("distances " + str(distance))
#==============================================================================
#     if distance == 1.0:
#         print("the point that is causign 1.0 is")
#         print(point1)
#         print(" and ")
#         print(point2)
#==============================================================================
    return distance
    
def get_centroid_means(centroid_frame, initial_frame):
    for i in range(0, centroid_frame.shape[0]):
        #This is a boolean way to get only the values from the real frame for each cluster
        df = initial_frame[initial_frame[initial_frame.columns[-1]] == i]
#==============================================================================
#         print(centroid_frame)
#         df.append(centroid_frame.iloc[i])
#         print("the values in thew boolean frame")
#         print(df)
#==============================================================================
        #when we have those values we can take the mean and put them in the centroids location
        centroid_frame.iloc[i] = df.mean()
        
#==============================================================================
#     print("the frame in means")    
#     print(centroid_frame)
#     
#==============================================================================
    return centroid_frame
    
def get_max_difference_between_previous_centroids_and_current_centroids(previous, current):
    difference = 0

    for i in range(0, current.shape[0]):
        difference += previous.iloc[i] - current.iloc[i]
#==============================================================================
#         print(difference)
#     print("yo")
#     print(type(difference[0]))
#==============================================================================
    return abs(difference[0])
    
def k_means(initial_dataframe, k):
    
    centroid_frame = generate_centroids(initial_dataframe, k)
    
    #return centroid_frame
    initial_dataframe['cluster'] = np.NaN
    
    frame_without_classes = initial_dataframe.iloc[:,0:(initial_dataframe.shape[1]-1)]
    print(centroid_frame)
    i = 0
    while True:
        
        for index_of_frame, point1 in frame_without_classes.iterrows():

            distances = []

            for index_of_cluster, point2 in centroid_frame.iterrows():
                distances.append(distance_between_two_points(point1, point2))
                
            index = distances.index(min(distances))
            #print("indices" +str(index))
            initial_dataframe.iloc[index, initial_dataframe.shape[1]-1] = index_of_cluster

        
        if i < 4:
            print(centroid_frame)
            print(initial_dataframe)
        current_frame = centroid_frame.copy(deep=True)
        
        #Freaking needed the cluster classifications!!!!! took forever to find
        #another problem found here.  There will be be no difference between
        #the initial fram eand the mean one in the beginning.  We need
        #to figure out how make them different in the clusters.
#==============================================================================
#         print("current frame is:" )
#         print(current_frame)
#==============================================================================
        current_frame = get_centroid_means(centroid_frame, initial_dataframe)
        
#==============================================================================
#         print("\n\n the frame is now")
#         print(current_frame)
#==============================================================================
        
        #now this is giving us distance of things.  It seems it is never changing however
        #we are not breaking because of something.
        i +=1
        biggest_centroid_move = get_max_difference_between_previous_centroids_and_current_centroids(centroid_frame, current_frame)
        #centroid_frame = current_frame
#==============================================================================
#         print("the centroid are now ")
#         print(centroid_frame)
#         print(biggest_centroid_move)
#==============================================================================
        
        if i >= 7:
            if biggest_centroid_move < .1:
                print("end")
                break
            
            
    return initial_dataframe

data = pd.read_csv("iris.csv", header = None)

#==============================================================================
# data.mean()
# data.sum()
# data.values[0]
# f = data.iloc[:, 0:]
# data.values.max()
# data.iloc[0]
# 
# distance_between_two_points(data.iloc[0], data.iloc[1])
#     
# centroid_frame = generate_centroids(data, 6);
# centroid_frame.columns[-1]
# df = centroid_frame.drop(centroid_frame[centroid_frame[centroid_frame.columns[-1]] < 50])
# 
# data['class'] = 1
# data.columns[-1]
# frame_without_classes = data.iloc[:,0:(data.shape[1]-1)]
# data.iloc[0][-1] =2
# d = get_centroid_means(centroid_frame, data)
# 
# data.subtract(data, fill_value = 0)
# 
#==============================================================================
#data['cluster'] =  0
frame = k_means(data, 3)
#==============================================================================
# centroid = generate_centroids(data, 3)
# frame = data.iloc[:, 0:data.shape[1]-1]
# mean = frame.mean()
# data.iloc[0] = frame.mean()
#==============================================================================
#meansdzfghhsdfjgsodfihug = get_centroid_means(centroid, data)

#==============================================================================
# copy = data.copy(deep=True)
#==============================================================================

#centroid = generate_centroids(data, 3)
#data.iloc[1, data.shape[1]-1] = 2
#==============================================================================
# for index, row in data.iterrows():
#      print(row[0])
#==============================================================================

