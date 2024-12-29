import requests
import pandas as pd
import gzip
import io

# Fonction pour charger les donnees
def recuperer_donnees(dataset_id, fichier_csv, sep):
    """
    Cette fonction télécharge les données d'un fichier CSV à partir d'une URL et les charge dans un DataFrame pandas.
    
    Paramètres:
    dataset_id (str): idetifiant du fichier CSV.
    fichier_csv (str): Le nom du fichier CSV à enregistrer localement.
    
    Retourne:
    DataFrame: Un DataFrame pandas contenant les données du fichier CSV.
    """

    # URL de base pour accéder à l'API
    base_api = "https://www.data.gouv.fr/api/1/"

    # Chemin pour accéder aux enregistrements du dataset
    key_api = "datasets/r/"

    # Construction de l'URL complète
    url = f"{base_api}{key_api}{dataset_id}"


    response = requests.get(url)
    if response.status_code == 200:
        with open(fichier_csv, 'wb') as file:
            file.write(response.content)
        print("Le fichier a été téléchargé avec succès.")
        df = pd.read_csv(fichier_csv, sep = sep)
        return df
    else:
        print("La requête a échoué. Code d'état:", response.status_code)
        return None

#Fonction pour récupérer les données d'un fichier csv.gz ( pour les données météorologiques )
def recuperer_donnees_gz(dataset_id, fichier_csv, sep):
    import gzip
    import io
    """
    Cette fonction télécharge les données d'un fichier CSV.GZ à partir d'une URL et les charge dans un DataFrame pandas.
    
    Paramètres:
    dataset_id (str): identifiant du fichier CSV.GZ.
    fichier_csv (str): Le nom du fichier CSV.GZ à enregistrer localement.
    sep ( str ) : le séparateur à utiliser
    
    Retourne:
    DataFrame: Un DataFrame pandas contenant les données du fichier CSV.
    """

    # URL de base pour accéder à l'API
    base_api = "https://www.data.gouv.fr/api/1/"

    # Chemin pour accéder aux enregistrements du dataset
    key_api = "datasets/r/"

    # Construction de l'URL complète
    url = f"{base_api}{key_api}{dataset_id}"


    response = requests.get(url)
    response.raise_for_status()
    with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gz:
        df = pd.read_csv(gz, sep = sep)
    
    return df

# Fonction pour labeliser les variables d'un dataframe
def labeliser_variables(df, mapping_dict):
    """
    Labelise les variables d'un DataFrame en utilisant un dictionnaire de correspondance.
    
    Parameters:
    df (pd.DataFrame): DataFrame contenant les variables à labeliser.
    mapping_dict (dict): Dictionnaire de correspondance où chaque clé est le nom de la colonne
                         et la valeur est un dictionnaire de mappage des valeurs.
    
    Returns:
    pd.DataFrame: DataFrame avec les variables labelisées.
    """

    for col, map_dict in mapping_dict.items():
        if col in df.columns:
            df[col] = df[col].map(map_dict)
    return df


