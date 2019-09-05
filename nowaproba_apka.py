import csv
def make_dict():
    slownik = {}
    path=open('C:/Users/HP/Documents\gatunki.csv','r')
    for line in path:
        if len(line) > 1:
            z = line.split()
            if z[0] != '':
                slownik[z[0]] = z[1:len(z)]
    return slownik
print (make_dict())

listapozywek=list(make_dict().items())
def wybor(y):
  for i in(range(len(y))):
    print('Wybierz ', i+1, 'jeśli interesuje Cię ',y[i])
  x=int(input(':'))-1
  while x<0 or x>=len(y):
    x=int(input('Wybrałeś złą pożywkę. Wpisz jeszcze raz: '))
  return(x)
W=wybor(listapozywek)

'''barwa = ['różowa', 'niebieska', 'jasnoniebieska', 'niebiesko-zielona', 'metaliczno zielona', 'zielona', 'żółta','czarna','fioletowa']
hemoliza = ['Alfa-hemoliza', 'Beta-hemoliza']
wzrost = ['wzrost', 'brak wzrostu', 'mgławicowy']
odbarwienie_podloza = ['brązowe', 'zielone', 'żółte']
def charakterystyka_kolonii(b,h,w,o):
  wybory=[]
  for i in range(len(b)):
    for j in range(len(h)):
      for k in range(len(w)):
        for l in range(len(o)):
                    print(o[l], w[k], h[j], b[i])
                    wybory.append([o[l],w[k],h[j],b[i]])
charakterystyka_kolonii(barwa, hemoliza, wzrost, odbarwienie_podloza)
print('Wpisz wartość zaobserwowanej charakterystyki: ')
            
#print('koniec, wyrałeś %s' %W)
'''
