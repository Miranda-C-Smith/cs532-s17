import recomendations as r

pref= r.loadMovieLens()

fav_movie = "Pulp Fiction (1994)"
wor_movie = "My Best Friend's Wedding (1997)"

similar_movies = r.calculateSimilarItems(pref, 5)
diff_movies = r.calculateDiffItems(pref,5)

print(fav_movie)
print("\nMost Correlated")
for movie in similar_movies[fav_movie]:
    print(movie[1])
print("\nLeast Correlated")
for movie in diff_movies[fav_movie]:
    print(movie[1])
print("\n" + wor_movie)
print("\nMost Correlated")
for movie in similar_movies[wor_movie]:
    print(movie[1])
print("\nLeast Correlated")
for movie in diff_movies[wor_movie]:
    print(movie[1])

