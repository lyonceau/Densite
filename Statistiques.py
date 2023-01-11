#!/usr/bin/python
# -*- coding: utf-8 -*-

from .integrationBd import IntegrationBd
import psycopg2
import matplotlib.pyplot as plt
# import os
# import json
# import pandas as pd


class Statistiques(IntegrationBd):
    """ Second pour contenir quelques fonctions qui seront utilisées dans le fichier principale CheckOptyce.py """

    def temps_ecouler(self, seconde):
        seconds = seconde % (24 * 3600)
        hour = int(seconds // 3600)
        seconds %= 3600
        minutes = int(seconds // 60)
        seconds %= 60
        return f"{hour}h: {minutes}mn : {int(seconds)}sec" if hour > 0 else f"{minutes}mn : {int(seconds)}sec"

    def verification_identifiant_connexion_bd(self):
        """Pour ouvrir le fichier de connexion, permettant de récupérer les informations de connexion à
        la base de données"""

        # Identifiant et mot de passe de l'utilisateur de la base de données.
        identifiant_erronner = False

        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.bd)

            connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Précision de l'erreur : ", error)
            identifiant_erronner = True

        return True if identifiant_erronner else False

    def generateur(self, liste_communes):
        """"""
        chemin = f"{self.fichier}requetes/Selection/stat.sql"
        with open(chemin, 'r') as fd:
            requete = fd.read()
            fd.close()

        requete_complet = (tuple(liste_communes) if len(liste_communes) > 1 else (
            f"('{liste_communes[0]}')" if len(liste_communes) == 1 else ""))
        if requete_complet:
            requete = requete.format(requete_complet)

            resultat = self.connection_bd(requete)
            self.realisation_camembert_stat(resultat, liste_communes)

    def realisation_camembert_stat(self, data_stat, liste_communes):
        """Pour faire de la réprésentation statistique"""

        plt.figure(figsize=(10, 5))
        enregistrement = []
        labels = []
        nom = []
        explode = []
        colors = []

        categorie = ['Territoires artificialisés', 'Territoire agricole', 'Forêts et milieux semi-naturels',
                     'Zones humides', 'Surfaces en eau']
        code_couleur = ["#e6004d", "#ffffa8", "#80ff00", "#a6a6ff", "#00ccf2"]
        for (nom_classe, superficie), exp in zip(data_stat, [0, 0.2, 0, 0, 0]):

            enregistrement.append(superficie)
            labels.append(f"{nom_classe}\n{int(superficie/10000)} hacode_dept")
            explode.append(exp)
            nom.append(nom_classe)

            for couleur, code in zip(categorie, code_couleur):
                if couleur == nom_classe:
                    colors.append(code)
                    break

        ####################################
        labels = labels
        sizes = enregistrement

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=70)  # shadow=True,

        plt.axis('equal')

        titre = ', '.join(liste_communes)

        plt.title(titre, fontname="Times New Roman", size=15, weight='bold')

        plt.savefig('PieChart01.png')
        plt.show()
