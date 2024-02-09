import os
import pandas as pd
from datetime import datetime
from app.models import ODS

def run():
    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("data/clubs-data-2021.csv", delimiter=";")

    # Tronquer la table Club
    ODS.objects.all().delete()

    Clubs = []
    # Parcourir les lignes du DataFrame et insérer dans la table Club
    for index, row in df.iterrows():
        # Ajouter d'autres champs selon vos besoins
        obj = ODS(
            code_commune=row['Code Commune'],
            commune=row['Commune'],
            code_qpv=row['Code QPV'],
            name_qpv=row['Nom QPV'],
            department=row['Département'],
            region=row['Région'],
            statut_geo=row['Statut géo'],
            code_fede=row['Code'],
            federation=row['Fédération'],
            clubs=row['Clubs'],
            epa=row['EPA'],
            total=row['Total'],
            date=datetime.now()
        )
        Clubs.append(obj)

    ODS.objects.bulk_create(Clubs)

if __name__ == "__main__":
    run()