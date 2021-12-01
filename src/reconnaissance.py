from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    numero=0
    sim_max=0
    im_loc = image.localisation()
    for i in range (0,len(liste_modeles)):
        H = liste_modeles[i].H
        W = liste_modeles[i].W
        im_loc = im_loc.resize(H, W)
        sim = im_loc.similitude(liste_modeles[i])
        if sim > sim_max :
            sim_max = sim
            numero = i
    return numero
