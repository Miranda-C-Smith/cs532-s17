#from http://www.wellho.net/mouth/3662_Finding-all-the-unique-lines-in-a-file-using-Python-or-Perl.html

file = open('2uniqueUrls_1000', 'w')

def unique(source):
        sofar = {}
        for val in open(source):
                if not sofar.get(val):
                        yield val.strip()
                        sofar[val] = 1


for lyne in unique("uniqueUrls_1000"):
        file.write(lyne)
        file.write("\n")
