import pandas as pd
# task1
df=pd.read_csv("imdb_top_1000.csv") # load dataset
print(df.head())       #display 1st 5 rows
print(df.dtypes)       #check data type of each columns
print(df.shape)        # give dimension
print("Missing values: ",df.isna()) # check for missing values return true if values not exist otherwise false


# TASK 2 DATA CLEANING
print(df.drop_duplicates()) # drop duplicate rows
#Fill missing values in the dataset (e.g., replace missing ratings with the mean rating). 
mean_Rating=df["IMDB_Rating"].mean()
df["IMDB_Rating"]=df["IMDB_Rating"].fillna(mean_Rating)
print(df["IMDB_Rating"])

#⦁	Convert the Runtime column (which is in minutes as a string, e.g., "120 min") to an integer. 
newDf=df.replace({
    "Runtime":'[A-Za-z]'
},"",regex=True)
print(newDf.Runtime.dtypes)
newDf["Runtime"]=newDf["Runtime"].astype(int) # convert Runtime into int
print(newDf.Runtime.dtypes) 


# Task 3: Data Filtering & Sorting

#1. Find all movies with an IMDb rating greater than 8.5.

newDf=df[["Series_Title","IMDB_Rating"]][df.IMDB_Rating>8.5]
print(newDf)

# List movies that belong to the Action or Sci-Fi genre.
print(df[["Series_Title","Genre"]][df["Genre"].str.contains("Action|Sci-Fi",case=False,na=False)]) # case= False makes case insensitive and na=false ingonre null values

# Find movies that were released between 2000 and 2015.
print(df[["Series_Title","Released_Year"]][df["Released_Year"]>=2000 & df["Released_Year"]<=2015])  

print(df[["Series_Title","Released_Year"]][
    (df["Released_Year"]>="2000") &
    (df["Released_Year"]<="2015")
    ])                                                                                          
# Sort the dataset based on IMDb rating in descending order
print(df.sort_values(by="IMDB_Rating",ascending=False))

#Data Aggregation & Grouping

# Find the average IMDb rating for each genre.
Genre=df.groupby("Genre").IMDB_Rating.mean()
print(Genre)

#. Determine which year had the most movies released
print(df.groupby("Released_Year")["Series_Title"].count().sort_values(ascending=False).head(1))

# Find the top 5 directors who have directed the most movies in the dataset
print(df.groupby("Director")["Series_Title"].count().sort_values(ascending=False).head())

