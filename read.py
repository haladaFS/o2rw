import re
import json
from json.decoder import JSONDecodeError

def AddSubjects(hrefCore, subjects):
    for i in subjects:
        #hrefCore += ", <mark>" + i + "</mark>"
        hrefCore += ", (" + i + ")"
    return hrefCore

def AddTags(hrefCore, mark):
    for i in subjects:
        if(i == ''):
            continue
        elif(i == 'zk'):
            hrefCore += " &#128218"
        elif(i == "+"):
            hrefCore += " &#128161"
        elif(i == "pr"):
            hrefCore += " &#128161"
    return hrefCore

myfilename = "database.json"
database = []
listOfSubjects = []

with open("changed.files") as changedFiles:
    changedList = changedFiles.read().splitlines()

with open(myfilename) as f:
    try:
        database = json.load(f)
    except JSONDecodeError:
        pass

with open("subjects.list") as subjectsList:
    listOfSubjects = subjectsList.read().splitlines()

print(changedList)
print(database)
print("\n")
print(listOfSubjects)

#nacte soubor novych a zmenenych souboru z githubu
for i in changedList:
    with open("source_tex/" + i) as myfile:
        head = [next(myfile) for x in range(6)]

    #PREDELAT - prelozeni hlavicky textu
    fname = i[:-4]; print(fname)
    title = re.findall('"([^"]*)"', head[1]); print(title)
    topic = re.findall('"([^"]*)"', head[2]); print(topic)
    subjects = re.findall('"([^"]*)"', head[3]); print(subjects)
    mark = re.findall('"([^"]*)"', head[4]); print(mark)
    author = re.findall('"([^"]*)"', head[5]); print(author)
    print("\n")

    #vygenerovani html odkazu
    hrefCore = "<a href=\"" + fname + ".html\">" + title[0] + "</a>"
    hrefSubj = AddSubjects(hrefCore, subjects)
    hrefMarks = AddTags(hrefCore, mark)
    print(hrefCore)
    print(hrefSubj)
    print(hrefMarks)
    print("\n")

    #PREDELAT - je li soubor v seznamu, smaze stary zaznam a vytvori novy
    if any(fname in sublist for sublist in database):
        print("==== NALEZENO =====")
        index = next(i for i,v in enumerate(database) if fname in v)
        print("Index: ", index)
        del database[index]
        database.append([fname, hrefSubj, hrefMarks, topic, subjects, mark, author])
    #neni li soubor v seznamu, je zapsan
    else:
        print("==== NENALEZENO =====")
        database.append([fname, hrefSubj, hrefMarks, topic, subjects, mark, author])

    print("Subjects: ", subjects)
    for s in subjects:
        if s in listOfSubjects:
            print("Subject found.")
        else:
            print("Subject not found.")
            listOfSubjects.append(s)

    print("\n")

print(database)
print("List of subjects:")
print(listOfSubjects)

###
database.sort(key=lambda x: x[0])
listOfSubjects.sort(key=lambda x: x[0])

print("Database sorted:")
print(database)
print("List of subjects sorted:")
print(listOfSubjects)

### UNPACK DATABASE TO HTML
htmlFile_topics = "articles_topics.html"
htmlFile_subjects = "articles_subjects.html"

### SAVE DATABASE
with open(myfilename, "w") as f:
    json.dump(database, f)

print("==============================List of subjects:")
print(listOfSubjects)

with open("subjects.list", "w") as f:
    for s in listOfSubjects:
        f.write("%s\n" % s)

#print(databas)
databaseMath = []
databaseMechContinuum = []
databaseMechClassical = []
databaseConstruction = []
databaseOthers = []

for i in database:
    if(i[3][0] == 'Matematika'):
        print("Přiřazeno.")
        databaseMath.append(i)
    elif(i[3][0] == 'Mechanika kontinua'):
        print("Přiřazeno.")
        databaseMechContinuum.append(i)
    elif(i[3][0] == 'Mechanika poddajných těles'):
        print("Přiřazeno.")
        databaseMechClassical.append(i)
    elif(i[3][0] == 'Konstruování'):
        print("Přiřazeno.")
        databaseConstruction.append(i)
    elif(i[3][0] == 'Ostatní'):
        print("Přiřazeno.")
        databaseOthers.append(i)
    else:
        print(i[3])
        print(type(i[3]))

def databaseToHtmlFile(name, database):
    with open(name, "w") as f:
        for i in database:
            f.write(i[1])
            f.write("<br>")

databaseToHtmlFile("src_topics/math.html", databaseMath)
databaseToHtmlFile("src_topics/mechcontinuum.html", databaseMechContinuum)
databaseToHtmlFile("src_topics/mechclassical.html", databaseMechClassical)
databaseToHtmlFile("src_topics/construction.html", databaseConstruction)
databaseToHtmlFile("src_topics/other.html", databaseOthers)


for s in listOfSubjects:
    name = "src_subjects/" + s + ".html"
    print(name)
    with open(name, 'w') as f:
        for d in database:
            for t in d[4]:
                if t == s:
                    f.write(d[2])
                    f.write("<br>")

