from random import randint
print("LE JEU DU CHAMEAU !")
print("Vous avez volé un chameau pour traverser le grand désert.")
print("Les natifs veulent le récupérer.")
print("Votre objectif est de survivre à la traversée de 300 km sans être attrapé(e).")

KM_VOYAGE = 300
KM_NORM_MIN = 10
KM_NORM_MAX = 15
KM_RAP_MIN = 20
KM_RAP_MAX = 25
AVANTAGE_VOYAGEUR = 20
GOURDE_PLEINE = 12
MORT_SOIF = 4
MORT_FATIGUE = 4
DIF_AIDE = 3
AVANCE_NATIFS = 4

km_voyageur = 0
km_natifs = km_voyageur - AVANTAGE_VOYAGEUR
gourde = GOURDE_PLEINE // 2
soif = 0
fatigue = 0
choix = ""

def afficherMenu(tempete):
    print("\nO P T I O N S :")
    if tempete == False :
        print("1. Boire")
        print("2. Avancer normalement")
        print("3. Avancer à toute vitesse")
        print("4. Repos")
        print("5. Espérer de l'aide")
        print("T. Terminer la partie \n")
    else :
        print("6. Attendre le prochain tour")
        print("T. Terminer la partie \n")

def boire(gourde, soif):
    if gourde == 0:
        print("Votre gourde est vide !")
        return gourde, soif
    else :
        soif = 0
        gourde -= 1
        print("Vous avez bu une gorgée. Il vous reste",gourde,"gorgée")
        return gourde, soif

def avancenormal(fatigue, km_voyageur):
    fatigue += 1
    km_voyageur += randint(KM_NORM_MIN,KM_NORM_MAX)
    return fatigue, km_voyageur

def avancerapide(fatigue, km_voyageur):
    fatigue += 2
    km_voyageur += randint(KM_RAP_MIN, KM_RAP_MAX)
    return fatigue, km_voyageur

def repos():
    print("Votre chameau s'est bien reposé")
    return 0

def aide(gourde):
    nb = randint(0,DIF_AIDE)
    if nb == 0 :
        print("Vous avez trouvé de l'aide")
        if gourde >= GOURDE_PLEINE:
            return "Votre gourde est déjà pleine"
        elif gourde+3 <= GOURDE_PLEINE :
            gourde += 3
        elif gourde+2 <= GOURDE_PLEINE :
            gourde += 2
        elif gourde+1 <= GOURDE_PLEINE :
            gourde += 1
        print("Quelques gorgées ont été ajoutées à votre gourde")
        return gourde
    else :
        return "Vous n'avez pas trouvé de l'aide"

def avancejoueur(km_voyageur):
    if km_voyageur >= KM_VOYAGE :
        print("Félicitations, vous avez parcouru les "+ str(KM_VOYAGE) + " km")
        return False
    else :
        print("Vous avez parcouru un total de " + str(km_voyageur) + " km jusqu'ici")
        return True
    
def avancenatifs(km_natifs):
    nb = randint(0, AVANCE_NATIFS)
    if nb == 0 :
        nb, km_natifs = avancerapide(2, km_natifs)
    elif nb == 1 :
        nb, km_natifs = avancenormal(1, km_natifs)
    elif km_natifs >= km_voyageur:
        print("Les natifs vont ont attrapé")
        return False, 0
    print("Les natifs sont à",km_natifs-km_voyageur,"km derrière vous")
    return True, km_natifs

def soife(soif):
    soif += 1
    if soif >= MORT_SOIF :
        print("Vous etes mort de soif !")
        return False, 0
    elif soif == 0 :
        print("Vous n'avez pas soif !")
    elif soif == 1 :
        print("Vous avez un peu soif")
    elif soif == 2 :
        print("Vous avez beaucoup soif !")
    elif soif == 3 :
        print("Vous allez mourir de soif !")
    return True, soif
    
def fatiguer():
    if fatigue > MORT_FATIGUE :
        print("Vous etes mort de fatigue")
        return False
    elif fatigue == 0 :
        print("Le chameau est en bonne forme.")
    elif fatigue == 1 :
        print("Le chameau est un peu fatigué.")
    elif fatigue == 2 :
        print("Le chameau est très fatigué !")
    elif fatigue == 3 :
        print("Le chameau va mourir de fatigue !!")
    return True

def evenement(gourde):
    nb = randint(0,1)
    if nb == 0 :
        print("Vous avez trouvé un oasis.\nVotre gourde est remplie")
        gourde = GOURDE_PLEINE
        return False, gourde
    elif nb == 1 :
        print("Une tempête s'abbat sur vous.\nVous ne pouvez ni boire, ni reposer votre chameau, ni trouver de l'aide pendant ce prochain tour")
        return True, gourde
    
def jeux(km_voyageur, km_natifs, gourde, soif, fatigue, choix) :
    boucle = True
    tempete = False
    while boucle :
        afficherMenu(tempete)
        choix = input("Qu'allez-vous faire ? : ")
        print()
        if choix == "1" and tempete == False:
            gourde, soif = boire(gourde, soif)
            valide = True
            
        elif choix == "2" and tempete == False:
            fatigue, km_voyageur = avancenormal(fatigue, km_voyageur)
            valide = True
            
        elif choix == "3" and tempete == False:
            fatigue, km_voyageur = avancerapide(fatigue, km_voyageur)
            valide = True
            
        elif choix == "4" and tempete == False:
            fatigue = repos()
            valide = True
            
        elif choix == "5" and tempete == False:
            gourde = aide(gourde)
            valide = True
         
        elif choix == "6" and tempete == True :
            pass
        
        elif choix == "T":
            print("Vous venez d'arrêter la partie")
            break
        
        else :
            print("Option Invalide")
            valide = False
            
        if valide or tempete == True:
            boucle = avancejoueur(km_voyageur)
            if boucle == False :
                break
            else :
                boucle, km_natifs = avancenatifs(km_natifs)
            if boucle == False :
                break
            else :
                boucle, soif = soife(soif)
            if boucle == False :
                break
            else :
                print("Votre gourde contient",gourde,"gorgées d'eau")
                fatigue += 1
                boucle = fatiguer()
        tempete, gourde = evenement(gourde)
jeux(km_voyageur, km_natifs, gourde, soif, fatigue, choix)
if choix != "T" :
    recommencer = input("Voulez vous recommencer ? O pour Oui et N pour Non")
    if recommencer == "O":
        jeux(0,km_voyageur - AVANTAGE_VOYAGEUR, GOURDE_PLEINE // 2, 0, 0, "")