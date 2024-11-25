import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(123)
from IPython.display import display


url_usagers_2023 = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2023/20241023-153328/usagers-2023.csv"
usagers_2023 = pd.read_csv(url_usagers_2023, sep = ';')

url_vehicules_2023 = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2023/20241023-153253/vehicules-2023.csv"
vehicules_2023 = pd.read_csv(url_vehicules_2023, sep = ';')

url_lieux_2023 = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2023/20241023-153219/lieux-2023.csv"
lieux_2023 = pd.read_csv(url_lieux_2023, sep = ';')

url_caract_2023 = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2023/20241028-103125/caract-2023.csv"
caract_2023 = pd.read_csv(url_caract_2023, sep = ';')
