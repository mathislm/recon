#!/home/absolut/Documents/Prog/Python-3.5.2/
# -*-coding:Utf-8 -*
import math as mt

def arctan(y,x):
	"""
	renvois un arctan entre 0 et 2pi
	"""
	return (mt.atan2(y,x))


def scalaire(u,v):
	"""
	return le scalaire de u par v
	"""
	angle1 = mt.atan2(u[1], u[0])
	angle2 = mt.atan2(v[1], v[0])
	angle = angle2 - angle1
	scalaire = mt.cos(angle)*module(u)
	return (scalaire)

def module(vecteur):
	"""
	calcule le module d'un vecteur
	"""
	return mt.sqrt(puissance(vecteur[0],2) + puissance(vecteur[1],2))

def found(tab,x):
	"""
	trouve un element x dans un tableau tab
	"""
	n = len(tab)
	found = False
	i = 0
	while i < n and found == False:
		if tab[i] == x:
			found = True
		i += 1
	return (found, i-1)

def tri_insertion(tab):
	"""
	tri un tableau tab avec la methode de tri par insertion
	"""
	n = len(tab)
	for i in range (1,n):
		tempo = tab[i] 
		j = i
		while j>0 and tab[j-1]>tempo:
			tab[j] = tab[j-1]
			j = j-1
			tab[j] = tempo
	return tab

def absolue(x):
	"""
	return la valeur absolue d'un nombre reel x
	"""
	if x > 0:
		return x
	else:
		return -x

def puissance(x,n):
	"""
	un nombre !entier! x à la puissance n
	"""
	resultat = 1
	for i in range (0,n,1):
		resultat = resultat * x
	return resultat

def pgp (x,p):
	"""
	la plus grande puissance entiere de p pour obtenir un nombre x
	fait avec des log
	"""
	pgp = int(mt.log(x)/mt.log(p))
	return pgp


def racine(x,n):
	"""
	estimation racine carré d'un nombre x avec n iteration
	plus n est grand, plus la valeur est precise
	conseil pour n : 10
	"""
	u =1.
	for i in range (0,n,1):
		u = float((u+(x/u))/2)
	return u

def fac(valeur):
	"""
	return la factoriel d'un nombre valeur
	"""
	i = 0
	result = 1
	while i <valeur:
		result =(i+1)*result
		i += 1
	return result

def somme(tb,j=0,n='none'):
	"""
	Fait la somme de tout les elements d'un tableau tb
	option : j = debut de la somme
		 n = fin de la somme
	"""
	som = 0
	if n == 'none':
		n = len(tb)
	for i in range (j,n,1):
		som = som + tb[i]
	return som

def moyenne(tb,i=0,n="none"):
	"""
	Fait la moyenne d'un tableau tb
	option : j = debut de la somme
                 n = fin de la somme
	"""
	if n == 'none':
		n = len(tb)
	moy = float(somme(tb,i,n))/(n-i)
	return moy

def variance(tb):
	"""
	return la variance d'un tableau tb
	"""
	n = len(tb)
	moyen = moyenne(tb)
	variance = 0
	for i in range (0,n,1):
		variance = variance + (tb[i] - moyen)**2
	variance = variance/n
	return variance

def ecart_type(tb):
	"""
	Donne l'ecart-type d'un tableau tb
	"""
	return racine(variance(tb),10)

def maxi(tb):
	"""
	Donner le maximun d'un tableau tb
	"""
	n = len(tb)
	maxi = tb[0]
	for i in range (1,n,1):
		if (tb[i] > maxi):
			maxi = tb[i]
	return maxi

def mini(tb):
	"""
	Donner le minimun d'un tableau tb
	"""
	n = len(tb)
	mini = tb[0]
	for i in range (1,n,1):
		if (tb[i] < mini):
			mini = tb[i]
	return mini

def occurences(tb,x):
	"""
	Donner l'occurence d'un element d'un element x dans un tableau tb
	"""
	n = len(tb)
	occurences = 0
	for i in range (0,n,1) :
		if tb[i] == x:
			occurences = occurences +1
	return occurences

def majoritaire(tb):
	"""
	Donner l'element majoritaire d'un tableau tb
	le return donne son existance puis sa valeur
	"""
	n = len(tb)
	existe = False
	i = 0
	majoritaire = 'None'
	while existe == False and i < n/2 :
		if occurences(tb,tb[i]) > n/2:
			majoritaire = tb[i]
			existe = True
		i += 1
	return existe,majoritaire


