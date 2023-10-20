


# import pandas as pd
# from datetime import datetime
# from flask import Flask, request, jsonify


# # Charger les données du nouveau fichier CSV
# donnees_rugby = pd.read_csv("meteo_rugby_data  copie.csv", parse_dates=["date"])
# cotes_rugby = pd.read_csv("fichier_cotes.csv")

# # Fonction pour prédire le vainqueur d'un match entre deux pays en utilisant les cotes
# def prédire_vainqueur(pays1, pays2, conditions_meteo):
#     # Filtrer les matchs entre les deux pays
#     matches_entre_pays = donnees_rugby[
#         (((donnees_rugby["home_team"] == pays1) & (donnees_rugby["away_team"] == pays2)) |
#          ((donnees_rugby["home_team"] == pays2) & (donnees_rugby["away_team"] == pays1))
#         )]

#     # Si aucun match n'a été joué entre ces deux pays, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe
#     if matches_entre_pays.shape[0] == 0:
#         return "Match nul", 50.0, 50.0

#     # Calculer le nombre de victoires de chaque équipe
#     victoires_pays1 = (
#         ((matches_entre_pays["home_team"] == pays1) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"]))
#         + ((matches_entre_pays["away_team"] == pays1) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"]))
#     ).sum()

#     victoires_pays2 = (
#         ((matches_entre_pays["home_team"] == pays2) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"]))
#         + ((matches_entre_pays["away_team"] == pays2) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"]))
#     ).sum()

#     # Calculer le taux de réussite de chaque équipe
#     total_matches = matches_entre_pays.shape[0]
#     taux_reussite_pays1 = (victoires_pays1 / total_matches) * 100
#     taux_reussite_pays2 = (victoires_pays2 / total_matches) * 100

#     # Utiliser les cotes pour ajuster les taux de réussite
#     cotes_match = cotes_rugby[(cotes_rugby["home_team"] == pays1) & (cotes_rugby["away_team"] == pays2)]
#     if not cotes_match.empty:
#         cote_home = cotes_match["odd_1"].str.replace(',', '.', regex=True).astype(float)
#         cote_away = cotes_match["odd_2"].str.replace(',', '.', regex=True).astype(float)

#         prob_victoire_pays1 = 1 / cote_home
#         prob_victoire_pays2 = 1 / cote_away

#         # Ajuster les taux de réussite en utilisant les probabilités des cotes
#         taux_reussite_pays1 = taux_reussite_pays1 * prob_victoire_pays1
#         taux_reussite_pays2 = taux_reussite_pays2 * prob_victoire_pays2

#     return taux_reussite_pays1, taux_reussite_pays2

# # Exemple d'utilisation avec deux équipes (Angleterre et France) et des conditions météo favorables
# pays1 = "Italy"
# pays2 = "New Zealand"
# conditions_meteo = {"avg_temp_c": 10, "precipitation_mm": 0, "avg_wind_speed_kmh": 20}

# taux_reussite_pays1, taux_reussite_pays2 = prédire_vainqueur(pays1, pays2, conditions_meteo)

# print(f"Taux de réussite pour {pays1}: {taux_reussite_pays1:.2f}%")
# print(f"Taux de réussite pour {pays2}: {taux_reussite_pays2:.2f}%")
# import pandas as pd

 

# # Charger les données du fichier CSV

# donnees_rugby = pd.read_csv("meteo_rugby_data  copie.csv")

 

# # Fonction pour prédire le vainqueur d'un match entre deux pays

# def prédire_vainqueur(pays1, pays2):

#     # Filtrer les matchs entre les deux pays

#     matches_entre_pays = donnees_rugby[((donnees_rugby["home_team"] == pays1) & (donnees_rugby["away_team"] == pays2)) | ((donnees_rugby["home_team"] == pays2) & (donnees_rugby["away_team"] == pays1))]

    

#     # Si aucun match n'a été joué entre ces deux pays, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe

#     if matches_entre_pays.shape[0] == 0:

#         return "Match nul", 50.0, 50.0

    

#     # Calculer le nombre de victoires de chaque équipe

#     victoires_pays1 = ((matches_entre_pays["home_team"] == pays1) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() + ((matches_entre_pays["away_team"] == pays1) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()

    

#     victoires_pays2 = ((matches_entre_pays["home_team"] == pays2) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() + ((matches_entre_pays["away_team"] == pays2) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()

    

#     # Calculer le taux de réussite de chaque équipe

#     total_matches = matches_entre_pays.shape[0]

#     taux_reussite_pays1 = (victoires_pays1 / total_matches) * 100

#     taux_reussite_pays2 = (victoires_pays2 / total_matches) * 100

    

#     return taux_reussite_pays1, taux_reussite_pays2

 

# # Exemple d'utilisation en utilisant les premières lignes du CSV

# pays1 = "South Africa"

# pays2 = "Italy"

 

# taux_reussite_pays1, taux_reussite_pays2 = prédire_vainqueur(pays1, pays2)

# print(f"Taux de réussite pour {pays1}: {taux_reussite_pays1:.2f}%")

# print(f"Taux de réussite pour {pays2}: {taux_reussite_pays2:.2f}%")

# app = Flask(__name__)


# @app.route('/predict', methods=['POST'])
# def predict():
#     # Obtenir les données de la requête (équipes et conditions météo)
#     data = request.get_json()
#     pays1 = data['pays1']
#     pays2 = data['pays2']
#     conditions_meteo = data['conditions_meteo']
    
#     # Appeler votre fonction de prédiction
#     taux_reussite_pays1, taux_reussite_pays2 = prédire_vainqueur(pays1, pays2, conditions_meteo)

#     # Retourner les résultats au format JSON
#     result = {
#         "taux_reussite_pays1": taux_reussite_pays1,
#         "taux_reussite_pays2": taux_reussite_pays2
#     }
#     return jsonify(result)


# if __name__ == '__main__':
#     app.run(debug=True)


# import pandas as pd

# # Charger les données du fichier CSV
# donnees_rugby = pd.read_csv("meteo_rugby_data  copie.csv")

# # Fonction pour calculer les facteurs d'incertitude basés sur les conditions météo
# def calculer_facteurs_incertitude(conditions_meteo):
#     facteur_temperature = 1.0 - (conditions_meteo["avg_temp_c"] - 10) * 0.02
#     facteur_precipitations = 1.0 - conditions_meteo["precipitation_mm"] * 0.01
#     facteur_vitesse_vent = 1.0 - (conditions_meteo["avg_wind_speed_kmh"] - 10) * 0.01
#     return facteur_temperature, facteur_precipitations, facteur_vitesse_vent

# # Fonction pour prédire le vainqueur d'un match entre deux pays
# def prédire_vainqueur(pays1, pays2, conditions_meteo):
#     # Filtrer les matchs entre les deux pays
#     matches_entre_pays = donnees_rugby[
#         ((donnees_rugby["home_team"] == pays1) & (donnees_rugby["away_team"] == pays2)) |
#         ((donnees_rugby["home_team"] == pays2) & (donnees_rugby["away_team"] == pays1))
#     ]

#     # Si aucun match n'a été joué entre ces deux pays, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe
#     if matches_entre_pays.shape[0] == 0:
#         return "Match nul", 50.0, 50.0

#     # Calculer le nombre de victoires de chaque équipe
#     victoires_pays1 = (
#         ((matches_entre_pays["home_team"] == pays1) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() +
#         ((matches_entre_pays["away_team"] == pays1) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()
#     )

#     victoires_pays2 = (
#         ((matches_entre_pays["home_team"] == pays2) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() +
#         ((matches_entre_pays["away_team"] == pays2) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()
#     )

#     # Calculer le taux de réussite de chaque équipe
#     total_matches = matches_entre_pays.shape[0]
#     taux_reussite_pays1 = (victoires_pays1 / total_matches) * 100
#     taux_reussite_pays2 = (victoires_pays2 / total_matches) * 100

#     # Calculer les facteurs d'incertitude basés sur les conditions météo
#     facteur_temperature, facteur_precipitations, facteur_vitesse_vent = calculer_facteurs_incertitude(conditions_meteo)

#     # Appliquer les facteurs d'incertitude aux taux de réussite
#     taux_reussite_pays1 *= facteur_temperature * facteur_precipitations * facteur_vitesse_vent
#     taux_reussite_pays2 *= facteur_temperature * facteur_precipitations * facteur_vitesse_vent

#     return taux_reussite_pays1, taux_reussite_pays2

# # Exemple d'utilisation avec deux équipes (Angleterre et France) et des conditions météo
# pays1 = "New Zealand"
# pays2 = "Italy"
# conditions_meteo = {"avg_temp_c": 5, "precipitation_mm": 2, "avg_wind_speed_kmh": 15}

# taux_reussite_pays1, taux_reussite_pays2 = prédire_vainqueur(pays1, pays2, conditions_meteo)

# print(f"Taux de réussite pour {pays1}: {taux_reussite_pays1:.2f}%")
# print(f"Taux de réussite pour {pays2}: {taux_reussite_pays2:.2f}%")


# import pandas as pd

# # Charger les données du fichier CSV
# donnees_rugby = pd.read_csv("meteo_rugby_data  copie.csv")

# # Fonction pour calculer les facteurs d'incertitude basés sur les conditions météo
# def calculer_facteurs_incertitude(conditions_meteo):
#     facteur_temperature = 1.0 - (conditions_meteo["avg_temp_c"] - 10) * 0.02
#     facteur_precipitations = 1.0 - conditions_meteo["precipitation_mm"] * 0.01
#     facteur_vitesse_vent = 1.0 - (conditions_meteo["avg_wind_speed_kmh"] - 10) * 0.01
#     return facteur_temperature, facteur_precipitations, facteur_vitesse_vent

# # Fonction pour prédire le vainqueur d'un match entre deux pays
# def prédire_vainqueur(pays1, pays2, conditions_meteo):
#     # Filtrer les matchs entre les deux pays
#     matches_entre_pays = donnees_rugby[
#         ((donnees_rugby["home_team"] == pays1) & (donnees_rugby["away_team"] == pays2)) |
#         ((donnees_rugby["home_team"] == pays2) & (donnees_rugby["away_team"] == pays1))
#     ]

#     # Si aucun match n'a été joué entre ces deux pays, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe
#     if matches_entre_pays.shape[0] == 0:
#         return "Match nul", 50.0, 50.0

#     # Calculer le nombre de victoires de chaque équipe
#     victoires_pays1 = (
#         ((matches_entre_pays["home_team"] == pays1) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() +
#         ((matches_entre_pays["away_team"] == pays1) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()
#     )

#     victoires_pays2 = (
#         ((matches_entre_pays["home_team"] == pays2) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() +
#         ((matches_entre_pays["away_team"] == pays2) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()
#     )

#     # Calculer le taux de réussite initial de chaque équipe (50% chacun)
#     taux_reussite_initial = 50.0

#     # Calculer les facteurs d'incertitude basés sur les conditions météo
#     facteur_temperature, facteur_precipitations, facteur_vitesse_vent = calculer_facteurs_incertitude(conditions_meteo)

#     # Appliquer les facteurs d'incertitude aux taux de réussite des deux équipes
#     taux_reussite_pays1 = taux_reussite_initial + (taux_reussite_pays1 - taux_reussite_initial) * facteur_temperature * facteur_precipitations * facteur_vitesse_vent
#     taux_reussite_pays2 = 100.0 - taux_reussite_pays1

#     return taux_reussite_pays1, taux_reussite_pays2

# # Exemple d'utilisation avec deux équipes (Angleterre et France) et des conditions météo
# pays1 = "Italy"
# pays2 = "France"
# conditions_meteo = {"avg_temp_c": 5, "precipitation_mm": 2, "avg_wind_speed_kmh": 15}

# taux_reussite_pays1, taux_reussite_pays2 = prédire_vainqueur(pays1, pays2, conditions_meteo)

# print(f"Taux de réussite pour {pays1}: {taux_reussite_pays1:.2f}%")
# print(f"Taux de réussite pour {pays2}: {taux_reussite_pays2:.2f}%")


# import pandas as pd

 

# # Charger les données du fichier CSV

# donnees_rugby = pd.read_csv("rugby_filtered_dataset copie.csv")

 

# # Fonction pour prédire le vainqueur d'un match entre deux pays

# def prédire_vainqueur(pays1, pays2):

#     # Filtrer les matchs entre les deux pays

#     matches_entre_pays = donnees_rugby[((donnees_rugby["home_team"] == pays1) & (donnees_rugby["away_team"] == pays2)) | ((donnees_rugby["home_team"] == pays2) & (donnees_rugby["away_team"] == pays1))]

    

#     # Si aucun match n'a été joué entre ces deux pays, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe

#     if matches_entre_pays.shape[0] == 0:

#         return "Match nul", 50.0, 50.0

    

#     # Calculer le nombre de victoires de chaque équipe

#     victoires_pays1 = ((matches_entre_pays["home_team"] == pays1) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() + ((matches_entre_pays["away_team"] == pays1) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()

    

#     victoires_pays2 = ((matches_entre_pays["home_team"] == pays2) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() + ((matches_entre_pays["away_team"] == pays2) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()

    

#     # Calculer le taux de réussite de chaque équipe

#     total_matches = matches_entre_pays.shape[0]

#     taux_reussite_pays1 = (victoires_pays1 / total_matches) * 100

#     taux_reussite_pays2 = (victoires_pays2 / total_matches) * 100

    

#     return taux_reussite_pays1, taux_reussite_pays2

 

# # Exemple d'utilisation en utilisant les premières lignes du CSV

# pays1 = "South Africa"

# pays2 = "England"

 

# taux_reussite_pays1, taux_reussite_pays2 = prédire_vainqueur(pays1, pays2)

# print(f"Taux de réussite pour {pays1}: {taux_reussite_pays1:.2f}%")

# print(f"Taux de réussite pour {pays2}: {taux_reussite_pays2:.2f}%")



# import pandas as pd

# # Charger les données du fichier CSV
# donnees_rugby = pd.read_csv("rugby_filtered_dataset copie.csv")

# # Fonction pour prédire le vainqueur d'un match entre deux pays
# def prédire_vainqueur(pays1, pays2):
#     # Filtrer les matchs entre les deux pays
#     matches_entre_pays = donnees_rugby[((donnees_rugby["home_team"] == pays1) & (donnees_rugby["away_team"] == pays2)) | ((donnees_rugby["home_team"] == pays2) & (donnees_rugby["away_team"] == pays1))]

#     # Si aucun match n'a été joué entre ces deux pays, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe
#     if matches_entre_pays.shape[0] == 0:
#         return "Match nul", 50.0, 50.0

#     # Calculer le nombre de victoires de chaque équipe
#     victoires_pays1 = ((matches_entre_pays["home_team"] == pays1) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() + ((matches_entre_pays["away_team"] == pays1) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()

#     victoires_pays2 = ((matches_entre_pays["home_team"] == pays2) & (matches_entre_pays["home_score"] > matches_entre_pays["away_score"])).sum() + ((matches_entre_pays["away_team"] == pays2) & (matches_entre_pays["away_score"] > matches_entre_pays["home_score"])).sum()

#     # Calculer le taux de réussite de chaque équipe
#     total_matches = matches_entre_pays.shape[0]
    
#     # Ajouter un avantage pour l'équipe à domicile
#     taux_reussite_pays1 = ((victoires_pays1 / total_matches) * 100) + 5  # Par exemple, donnez 5% d'avantage à l'équipe à domicile
#     taux_reussite_pays2 = (victoires_pays2 / total_matches) * 100

#     return taux_reussite_pays1, taux_reussite_pays2

# # Exemple d'utilisation en utilisant les premières lignes du CSV
# pays1 = "France"
# pays2 = "Italy"

# taux_reussite_pays1, taux_reussite_pays2 = prédire_vainqueur(pays1, pays2)

# print(f"Taux de réussite pour {pays1}: {taux_reussite_pays1:.2f}%")
# print(f"Taux de réussite pour {pays2}: {taux_reussite_pays2:.2f}%")


# import pandas as pd
# from datetime import datetime

# # Charger les données du fichier CSV
# donnees_rugby = pd.read_csv("rugby_filtered_dataset copie.csv")

# # Définir la date limite pour les données des 5 dernières années
# date_limite = datetime.now().year - 5

# # Fonction pour calculer la pondération en fonction de l'année
# def calculer_pondération(date):
#     annee = date.year
#     if annee >= date_limite:
#         # Donner un poids plus élevé aux matchs récents
#         return 1.0
#     else:
#         # Donner un poids décroissant aux matchs plus anciens
#         poids = 1.0 - (date_limite - annee) * 0.1  # Par exemple, réduire le poids de 0.1 chaque année plus ancienne
#         return max(poids, 0.1)  # Assurez-vous que le poids minimal est de 0.1

# # Fonction pour prédire le vainqueur d'un match entre deux pays
# def prédire_vainqueur(pays1, pays2):
#     # Filtrer les matchs entre les deux pays
#     matches_entre_pays = donnees_rugby[((donnees_rugby["home_team"] == pays1) & (donnees_rugby["away_team"] == pays2)) | ((donnees_rugby["home_team"] == pays2) & (donnees_rugby["away_team"] == pays1))]

#     # Si aucun match n'a été joué entre ces deux pays, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe
#     if matches_entre_pays.shape[0] == 0:
#         return "Match nul", 50.0, 50.0

#     # Initialiser les totaux pour le calcul de la pondération
#     total_pondération = 0
#     taux_reussite_pays1_pondéré = 0
#     taux_reussite_pays2_pondéré = 0

#     for index, match in matches_entre_pays.iterrows():
#         date_match = datetime.strptime(match["date"], "%Y-%m-%d")
#         poids = calculer_pondération(date_match)
#         total_pondération += poids

#         # Calculer le nombre de victoires de chaque équipe
#         victoires_pays1 = 0
#         victoires_pays2 = 0
#         if match["home_team"] == pays1:
#             if match["home_score"] > match["away_score"]:
#                 victoires_pays1 = 1
#             else:
#                 victoires_pays2 = 1
#         else:
#             if match["away_score"] > match["home_score"]:
#                 victoires_pays1 = 1
#             else:
#                 victoires_pays2 = 1

#         # Mettre à jour les taux de réussite pondérés
#         taux_reussite_pays1_pondéré += (victoires_pays1 / 100) * poids
#         taux_reussite_pays2_pondéré += (victoires_pays2 / 100) * poids

#     taux_reussite_pays1 = (taux_reussite_pays1_pondéré / total_pondération) * 100
#     taux_reussite_pays2 = (taux_reussite_pays2_pondéré / total_pondération) * 100

#     return taux_reussite_pays1, taux_reussite_pays2

# # Exemple d'utilisation en utilisant les premières lignes du CSV
# pays1 = "South Africa"
# pays2 = "New Zealand"

# taux_reussite_pays1, taux_reussite_pays2 = prédire_vainqueur(pays1, pays2)

# print(f"Taux de réussite pour {pays1}: {taux_reussite_pays1:.2f}")
# print(f"Taux de réussite pour {pays2}: {taux_reussite_pays2:.2f}")


import pandas as pd
from datetime import datetime

# Charger les données du fichier CSV
donnees_rugby = pd.read_csv("rugby_filtered_dataset copie.csv")

# Définir la date limite pour les données des 5 dernières années
date_limite = datetime.now().year - 5

# Fonction pour calculer la pondération en fonction de l'année
def calculer_pondération(date):
    annee = date.year
    if annee >= date_limite:
        # Donner un poids plus élevé aux matchs récents
        return 1.0
    else:
        # Donner un poids décroissant aux matchs plus anciens
        poids = 1.0 - (date_limite - annee) * 0.1  # Par exemple, réduire le poids de 0.1 chaque année plus ancienne
        return max(poids, 0.1)  # Assurez-vous que le poids minimal est de 0.1

# Fonction pour prédire le vainqueur d'un match entre l'équipe à domicile et l'équipe à l'extérieur
def prédire_vainqueur(domicile, extérieur):
    # if domicile == extérieur:
    #     return "Erreur : Les équipes domicile et extérieur sont identiques"
    # Filtrer les matchs entre l'équipe à domicile et l'équipe à l'extérieur
    matches_entre_pays = donnees_rugby[((donnees_rugby["home_team"] == domicile) & (donnees_rugby["away_team"] == extérieur)) | ((donnees_rugby["home_team"] == extérieur) & (donnees_rugby["away_team"] == domicile))]

    # Si aucun match n'a été joué entre ces deux équipes, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe
    if matches_entre_pays.shape[0] == 0:
        return "Match nul", 50.0, 50.0

    # Initialiser les totaux pour le calcul de la pondération
    total_pondération = 0
    taux_reussite_domicile_pondéré = 0
    taux_reussite_extérieur_pondéré = 0

    for index, match in matches_entre_pays.iterrows():
        date_match = datetime.strptime(match["date"], "%Y-%m-%d")
        poids = calculer_pondération(date_match)
        total_pondération += poids

        # Calculer le nombre de victoires de chaque équipe
        victoires_domicile = 0
        victoires_extérieur = 0
        if match["home_team"] == domicile:
            if match["home_score"] > match["away_score"]:
                victoires_domicile = 1
            else:
                victoires_extérieur = 1
        else:
            if match["away_score"] > match["home_score"]:
                victoires_domicile = 1
            else:
                victoires_extérieur = 1

        # Mettre à jour les taux de réussite pondérés
        taux_reussite_domicile_pondéré += (victoires_domicile / 100) * poids
        taux_reussite_extérieur_pondéré += (victoires_extérieur / 100) * poids

    taux_reussite_domicile = (taux_reussite_domicile_pondéré / total_pondération) * 100
    taux_reussite_extérieur = (taux_reussite_extérieur_pondéré / total_pondération) * 100

    return taux_reussite_domicile, taux_reussite_extérieur

# Exemple d'utilisation en utilisant les premières lignes du CSV
# domicile = "England"
# extérieur = "France"

# taux_reussite_domicile, taux_reussite_extérieur = prédire_vainqueur(domicile, extérieur)

# print(f"Taux de réussite pour l'équipe à domicile ({domicile}): {taux_reussite_domicile:.2f}")
# print(f"Taux de réussite pour l'équipe à l'extérieur ({extérieur}): {taux_reussite_extérieur:.2f}")
