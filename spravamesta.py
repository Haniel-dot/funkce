from utulek import pridej_zvire
from nemocnice import vypis_pacienty
from radnice import pozdravit_obcana

nazev=input("Zadejte nazev budovy, kterou chcete spravovat")
if nazev =="nemocnice":
    print("Spravujete nemocnici")
    vypis_pacienty()

elif nazev=="utulek":
    print("Spravujete utulek")
    nazev_zvirete=input("Zadejte nazev zvirete")
    pridej_zvire(nazev_zvirete)

elif nazev=="radnice":
    print("Spravujete radnici")
    jmeno=input("zadjete vase jmeno")
    pozdravit_obcana(jmeno)
else:
    print("Takovou budovu nevlastnime")


