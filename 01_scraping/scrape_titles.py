import pandas as pd
import os

# Définir le chemin relatif vers le fichier Excel simulé
input_path = "data/titles_2025_global.xlsx"
output_path = "data/rtitles_2025.csv"


# Vérification de l'existence du fichier
if not os.path.exists(input_path):
    print("❌ Le fichier titles_2025_global.xlsx n'a pas été trouvé dans data/")
else:
    # Charger le fichier Excel
    df_titles = pd.read_excel(input_path)

    # Vérifier les premières lignes
    print("✅ Fichier Excel chargé avec succès. Aperçu :")
    print(df_titles.head())

    # Sauvegarder en CSV pour l'étape de nettoyage
    df_titles.to_csv(output_path, index=False)
    print(f"✅ Fichier sauvegardé dans {output_path}")
