
# Fonction pour charger les donnees

def recuperer_donnees(dataset_id, fichier_csv, separateur):
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
        df = pd.read_csv(fichier_csv, sep = separateur)
        return df
    else:
        print("La requête a échoué. Code d'état:", response.status_code)
        return None

