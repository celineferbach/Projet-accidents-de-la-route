# Etude de l'impact de différents paramètres sur la gravité des accidents de la route

En France, plus de 50 000 accidents corporels sont recensés chaque année par l’Observatoire national interministériel de la sécurité routière (ONISR). On dénombre ainsi environ 3500 tués chaque année, soit près de 10 par jour, et 73000 blessés ( 200 par jour ). 
Notre projet s'appuie sur les bases de données annuelles des accidents corporels de la circulation routière publiées par le Ministère de l'Intérieur sur datagouv.fr. Si cette base de données ne permet pas d'avoir accès à certaines données spécifiques relatives aux usagers et aux véhicules et à leur comportement comme la consommation d'alcool ou de stupéfiants, puisque leur divulgation porterait atteinte à la protection de la vie privée des personnes impliquées, elle permet cependant d'observer un ensemble de paramètres généraux comme la localisation précise, la météo au moment de l'accident, la gravité des blessures de chaque victime, etc. 
Nous avons donc décidé de nous intéresser à l'étude de certains de ces paramètres, comme par exemple la localisation des accidents et la gravité des blessures des personnes physiques impliquées. Serait-il possible de prédire la gravité d'un accident à partir de paramètres faciles à obtenir pour les secours ( localisation, météo, types de véhicules impliqués, etc ), afin d'optimiser la répartition des moyens nécessaires au secours des victimes et la préparation du personnel déployé sur place ? 

# Bases de données utilisées

Pour cela, nous avons utilisé 4 bases de données principales :
- La base de données annuelle des accidents corporels de la circulation routière en 2023 publiée par le Ministère de l'Intérieur obtenue à partir de l'API de DataGouv;
- Une base de correspondance département région;
- Un géodataframe qui aidera pour les représentations cartographiques, obtenu à partir de cartiflette;
- Une base de données météorologiques pour l'année 2023 sur les départements d'Ile-de-France ( 75, 77, 78, 91, 92, 93, 94, 95 ) obtenue à partir de l'API de Data Gouv.

# Plan

Notre projet se divise en 5 parties :
### I. Importation des bases de données
### II. Traitement des données
  Traitement de la base des usagers, des véhicules, des lieux, des caractéristiques, de la correspondance départements-régions, du géodataframe, des données météorologiques
### III. Analyse des données
  Distribution du nombre de victimes en fonction de la gravité de l'accident, distribution de la gravité pour différentes vitesses maximales autorisées
  Nombre d'accidents en fonction de la météo
### IV. Analyse cartographique
  Localisation des accidents par région
  Analyse cartographique de la gravité
### V. Modélisation
  
