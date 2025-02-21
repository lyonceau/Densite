"""
/***************************************************************************
 DensiteOCS
                                 A QGIS plugin
 Un chargé de mission souhaite connaître la surface et le pourcentage de différentes classes d'occupation des sols sur différents types de territoire de son département des Hautes-Pyrénées (65).
Pour cela on va utiliser une base de données fournie par le CESBIO sur le dernier millésime disponible et on synthétisera l'information sur 7 classes d'OCS.
L'utilisateur doit pouvoir indiquer un territoire (à savoir une commune ou un EPCI) sur lequel il veut obtenir ces informations agrégées.

 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-12-29
        copyright            : (C) 2022 by SOUMARE Abdoulayi
        email                : abdoulayisoumare@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


class Initiatlisation:
    """ Second pour contenir quelques fonctions qui seront utilisées dans le fichier principale CheckOptyce.py """

    def __init__(self) -> None:
        """Le constructeur de ma classe
        Il prend pour attribut de classe les *** """

    def name(self) -> str:
        """Le nom de l'outil"""
        return u"Densité"

    def version(self) -> str:
        """La version de l'outil"""
        return "0.1"

    def description(self) -> str:
        """Description de l'outil"""
        return """Un chargé de mission souhaite connaître la surface et le pourcentage de différentes 
        classes d'occupation des sols sur différents types de territoire de son département des Hautes-Pyrénées (65).\n
        Pour cela on va utiliser une base de données fournie par le CESBIO sur le dernier millésime disponible et on 
        synthétisera l'information sur 7 classes d'OCS.\n
        L'utilisateur doit pouvoir indiquer un territoire (à savoir une commune ou un EPCI) sur lequel il veut obtenir ces informations agrégées.
        """

    def qgisMinimumVersion(self) -> str:
        return "3.0"

    def experimental(self) -> bool:
        """S'il s'agit d'un plugin expériemental"""
        return False

    def author(self) -> str:
        """Le Nom des auteurs"""
        return u"SOUMARE Abdoulayi"

    def author_name(self) -> str:
        """Renvoie au nom des auteurs"""
        return self.author()

    def email(self) -> str:
        return "abdoulayisoumare at gmail dot com"

    def icon(self) -> str:
        return "images/icon.png"


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DensiteOCS class from file DensiteOCS.
    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .densite import DensiteOCS
    return DensiteOCS(iface)
