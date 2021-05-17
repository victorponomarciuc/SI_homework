# #1 Ce valoare o sa contina variabila a după execuția codului ?
a = 10
a += len(str(a))
a = str(a)
print(a)
# 12

# #2 Codul de mai jos conține o eroare, modificați codul astfel încît programul să funcționze
# #corect.
c = "In padurea cu alune aveau casa " + ' 2 ' + "pitici"
print(c)

# #3 Ce valoare o sa contina variabila a dupa executia codului ?
a = 10
a + 1
print(a)
# 11

# #4 Codul de mai jos contine o erroare, Modificati codul ca nu apara erroare?
a = int(input('introduceti numarul: '))
a += 1
print(a)

#5 Scrieți un program care primește la input numele fisierului (text.txt,
#program.java) si intoarce extesia lui (txt, java). Puteti sa folositi functia split()
numeFisier1 = input('introduceti numele fisierului si extensia: ')
numeFisier2 = input('introduceti numele fisierului si extensia: ')
extensia1 = numeFisier1.split('.', 1)
extensia2 = numeFisier2.split('.', 1)
print("extensia fisierului este: " + extensia1[1] + " , " +  extensia2[1])

#6 Fie următoarea listă: a = ['a', 'b', 'c', 'd']
# 6.1
# Ce valoare are expresia a[int(int('3' * 2) // 11)] ?

# 6.2
# Adaugati o valoare nouă în lista a pe prima poziție.

# 6.3
# Ștergeți ultimele 2 valori din lista.

# 6.4
# Ordonati lista a descrescator

# 6.5
# Creați o listă nouă b care sa conțină toate elementele din lista a cu
# excepția primelor 2 elemente.

l = ['a', 'b', 'c', 'd'] # d

l.insert(0, 'n')

l.remove('c')
l.remove('d')

l.sort(reverse = True)
print(l)
# ['n', 'b', 'a']
c = l[2]

#7 Scrieți un program care afișează toate elementele din un invetar si calculează
#suma lor.
inventar = {'scaune': 14, 'mese': 22}
sm = inventar['scaune'] + inventar['mese']
print(sm)
