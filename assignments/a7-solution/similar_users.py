import recomendations as r

pref= r.loadMovieLens()
sub_me = '304'

similar_users = r.topMatches(pref,sub_me)
diff_users =  r.bottomMatches(pref,sub_me)
print("Top Matches:")
for item in similar_users:
    print(item[1])
print("Bottom Matches:")
for item in diff_users:
    print(item[1])
