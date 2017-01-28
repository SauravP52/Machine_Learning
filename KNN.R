#Implementation of K-Nearest Algorithm using R 
#===========================================================#
##Importing the iris dataset into the system and randomly ordering the element of iris dataset using a sampler
data=iris
data=data[sample(nrow(iris)),]

#===========================================================#
#Slice the data into two sets train_data for training the algorithm and test_data for testing purpose
train_data=data[1:135,]
test_data=data[136:nrow(data),]

#===========================================================#
#We now create a vector to store the score of the algorithm 
score=vector(length = 135)
prediction_score=0

#===========================================================#
#This is the value for K in the KNN Algorithm 
k=3

#===========================================================#
#The loop structure is as follows :-An outer loop across all the elements of test_data and an inner 
#loop runs through the entire element of the train_dataset and the score element stores
#the value of the distace between the two vector train_data[i,] and test_data[i,]

#===========================================================#
for(i in 1:15){
  for(j in 1:135){
    score[j]=dist(rbind(train_data[j,1:4],test_data[i,1:4]))
  }

#===========================================================#
#Now we require the score of the top k entries , keep them in train_datareq, and count the frequency
#instances of each classification by using a as.data.frame() and max() function
train_data=train_data[order(score),]
train_datareq=train_data[1:k,]
z=as.data.frame(table(train_data[1:k,5]))

#===========================================================#
#The model is awarded a score if the prediction (which occurs as the max frequency of classes the z matrix)
#corresponds to the actual test_value

if (z[which(z[1:nrow(z),2]==max(z[1:nrow(z),2])),1]==test_data[i,5]){
  prediction_score=prediction_score+1
  }
}               

#===========================================================#
#Next we show the score of the hypothesis in percentages..
print((prediction_score/15)*100)
