import recomendations as r
import operator

pref= r.loadMovieLens()



AsortPref = sorted(pref['304'].items(),key=operator.itemgetter(1), reverse=True)
BsortPref = sorted(pref['599'].items(),key=operator.itemgetter(1), reverse=True)
CsortPref = sorted(pref['300'].items(),key=operator.itemgetter(1), reverse=True)

Atop3 = dict(AsortPref[:3])
Abottom3 = dict(AsortPref[-3:])
Btop3 = dict(BsortPref[:3])
Bbottom3 = dict(BsortPref[-3:])
Ctop3 = dict(CsortPref[:3])
Cbottom3 = dict(CsortPref[-3:])

print("\tUser 304:\n Favorite")
print(Atop3)
print("Least Fav")
print(Abottom3)

print("\tUser 599:\n Favorite")
print(Btop3)
print("Least Fav")
print(Bbottom3)

print("\tUser 300:\n Favorite")
print(Ctop3)
print("Least Fav")
print(Cbottom3)

