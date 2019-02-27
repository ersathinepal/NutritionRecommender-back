import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.datasets.samples_generator import (make_blobs,
                                                make_circles,
                                                make_moons)
import  seaborn as sns
food_df = pd.read_csv("data/nndb_flat.csv")
food_df2 = food_df.iloc[:,0:13]
food_df2 = food_df2.dropna(axis = 'columns', how ='any')
food_df3=food_df2.drop(['ShortDescrip'], axis=1)
print(food_df3.head(3))
from sklearn.metrics import silhouette_samples, silhouette_score
plt.figure(figsize =(6,6))
plt.scatter(food_df3.iloc[:,0],food_df3.iloc[:,1])
plt.xlabel('Energy_kcal')
plt.ylabel('Descrip')
plt.title('Visulization of food vs energy')

def handle_non_numerical_data(food_df3):
    columns =food_df3.columns.values#for all columns
    
    for column in columns:
        text_digit_vals ={}#suruma text digit value empty pathako
        
        def convert_to_int(val):#textlai int ma convert garne fun banako
            return text_digit_vals[val]
        #nnumber ho ki haina check gareko
        if food_df3[column].dtype != np.int64 and food_df3[column].dtype!= np.float64:
            column_contents = food_df3[column].values.tolist()
            unique_elements = set(column_contents)
            x =0
            
            for unique in unique_elements:  #number ho bhane unique element lag abhneeko
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1
            
            food_df3[column] = list(map(convert_to_int, food_df3[column]))
            
    return food_df3

food_df3 = handle_non_numerical_data(food_df3)
print(food_df3)

plt.figure(figsize =(6,6))
plt.scatter(food_df3.iloc[:,0],food_df3.iloc[:,1])
plt.xlabel('Energy_kcal')
plt.ylabel('Descrip')
plt.title('Visulization of food vs energy')
X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=50);

#run local implementaion of kmeans
kmeans = KMeans(n_clusters=6, max_iter =100)
kmeans.fit(X)
y_means = kmeans.predict(X)
print(y_means)

#visulization of data
plt.scatter(X[:,0],X[:,1],c=y_means,s = 50,cmap ='viridis')
centers =kmeans.cluster_centers_
print(centers)

plt.scatter(centers[:,0],centers[:,1],c ='blue',s =200, alpha =0.5)

plt.scatter(X[:, 0], X[:, 1], c=y_means, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)








