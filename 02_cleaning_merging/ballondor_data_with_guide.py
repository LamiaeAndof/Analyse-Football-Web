import pandas as pd

# Charger les données finales
df_data = pd.read_csv("data/raw/ballondor_dataset.csv", sep=";")

# Créer le dictionnaire des colonnes
column_explanations = {
    "Player": "Nom du joueur",
    "Nation": "Nationalité du joueur (code FIFA)",
    "Pos": "Poste : FW (attaquant), MF (milieu), DF (défenseur)",
    "Age": "Âge approximatif (année uniquement)",
    "MP": "Matchs joués",
    "Min": "Minutes jouées",
    "Starts": "Matchs commencés en tant que titulaire",
    "Gls": "Buts marqués",
    "Ast": "Passes décisives",
    "PK": "Penaltys marqués",
    "CrdY": "Cartons jaunes",
    "CrdR": "Cartons rouges",
    "xG": "Expected Goals (buts attendus)",
    "xA": "Expected Assists (passes décisives attendues)",
    "GoalsPer90": "Buts par 90 minutes = Gls / (Min / 90)",
    "xGPer90": "xG par 90 minutes = xG / (Min / 90)",
    "xAPer90": "xA par 90 minutes = xA / (Min / 90)",
    "xGContribution": "(xG + xA) / (Min / 90)",
    "PopularityScore": "Score subjectif de notoriété (1–10)",
    "isStar": "1 si superstar (ex : Mbappé), sinon 0",
    "DomesticTitles": "Trophées nationaux gagnés en 2024–2025",
    "EuropeanTitles": "Trophées européens (UCL, UEL) gagnés",
    "NationalTeamWin": "1 si vainqueur CDM / Euro / Copa America",
    "TeamTitles": "Total des titres (somme des 3 précédents)",
    "FairPlayScore": "Score de fair-play = 10 - (2*CrdR + CrdY)"
}

# Convertir en DataFrame
df_guide = pd.DataFrame(list(column_explanations.items()), columns=["Colonne", "Description"])

# Enregistrer dans un seul fichier Excel avec deux feuilles
with pd.ExcelWriter("data/raw/ballondor_data_with_guide.xlsx") as writer:
    df_data.to_excel(writer, sheet_name="Dataset", index=False)
    df_guide.to_excel(writer, sheet_name="Dictionnaire", index=False)

print("✅ Fichier Excel généré avec succès dans data/raw/ballondor_data_with_guide.xlsx")
