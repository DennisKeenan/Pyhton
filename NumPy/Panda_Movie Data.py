import pandas as Pd

movie=Pd.read_csv("Movie_data.csv",index_col=0)
print(movie) #Print Data
print(movie.describe()) #Print Data Summary 
print(movie["Genre"].describe()) #Print Top Data Summary 
print(movie["Genre"].value_counts().head(10)) #Print Top Tenth Movie Genre
print(movie.corr()) #Print Correlation
print(movie.loc["Prometheus"]) #Print by Location (Slicing)
print(movie.iloc[4:11]) #Print by Index (Slicing)

movie=movie[["Title","Director","Year"]] #Showing Targeted Index
print(movie)

screenshot=(movie[movie["Director"]=="Ridley Scott"]) #Showing Directed Movie
print(screenshot)

print(movie[((movie["Year"]>=2005) and (movie["Year"]<=2010))])
year_subset=(movie[movie["Year"]>=2005])
print(year_subset[year_subset["Year"]<=2010])

