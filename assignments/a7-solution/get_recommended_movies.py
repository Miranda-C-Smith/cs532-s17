import recomendations as r

pref= r.loadMovieLens()
sub_me = '304'

rankings = r.getRecommendations(pref, sub_me)

print("RECOMMENDATIONS")
for movie in rankings[:5]:
    print(movie[1])
print("HATED MOVIES")
for movie in rankings[-5:]:
    print(movie[1])
