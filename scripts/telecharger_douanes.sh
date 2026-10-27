#!/bin/bash
# Télécharge les relevés départementaux de production des vins (douanes, 2009-2025)
# et les relevés par produit (appellation, 2017-2024).
# À lancer depuis la racine du projet : bash telecharger_douanes.sh
set -e
D=data/raw/douanes
mkdir -p "$D"
B=https://www.douane.gouv.fr/sites/default/files

get () { echo "-> $1"; curl -sSfL -o "$D/$1" "$2"; }

# --- Relevés par département ---
get dept_2009.xls  "$B/openData/files/2009-stats-recolte.xls"
get dept_2010.xls  "$B/openData/files/2010-stats-recolte.xls"
get dept_2011.xls  "$B/openData/files/2011-stats-recolte.xls"
get dept_2012.xls  "$B/openData/files/2012-stats-recolte.xls"
get dept_2013.xls  "$B/openData/files/2013-stats-recolte.xls"
get dept_2014.xls  "$B/openData/files/2014-stats-recolte.xls"
get dept_2015.xls  "$B/openData/files/2015-stats-recolte.xls"
get dept_2016.xls  "$B/openData/files/2016-stats-recolte.xls"
get dept_2017.xls  "$B/openData/files/2017-releve-par-departement-de-la-production-des-vins.xls"
get dept_2018.xls  "$B/uploads/files/2019-06/2018-releve-par-departement-de-la-production-des-vins.xls"
get dept_2019.xlsx "$B/uploads/files/2020-03/2019%20-%20Relev%C3%A9%20par%20d%C3%A9partement%20de%20la%20production%20des%20vins.xlsx"
get dept_2020.xls  "$B/2022-02/21/2020%20-%20Relev%C3%A9%20par%20d%C3%A9partement%20de%20la%20production%20des%20vins%20rectifi%C3%A9.xls"
get dept_2021.xlsx "$B/2024-05/10/2021%20-%20Relev%C3%A9%20par%20d%C3%A9partement%20de%20la%20production%20des%20vins%20d%C3%A9pt%2032%20rectifi%C3%A9.xlsx"
get dept_2022.xlsx "$B/2024-05/10/2022%20-%20Relev%C3%A9%20par%20d%C3%A9partement%20de%20la%20production%20des%20vins%20d%C3%A9pt%2032%20rectifi%C3%A9.xlsx"
get dept_2023.xlsx "$B/2024-07/08/2023%20-%20Relev%C3%A9%20par%20d%C3%A9partement%20de%20la%20production%20des%20vins%20OPENDATA%20rectifi%C3%A9%20au%2008-07-2024.xlsx"
get dept_2024.xlsx "$B/2025-05/25/2024%20-%20Relev%C3%A9%20par%20d%C3%A9partement%20de%20la%20production%20des%20vins%20OPENDATA.xlsx"
get dept_2025.xlsx "$B/2026-06/22/2025%20-%20Relev%C3%A9%20par%20d%C3%A9partement%20de%20la%20production%20des%20vins%20OPENDATA.xlsx"

# --- Relevés par produit (appellation) : contrôle de l'approximation départementale ---
get produit_2017.xls  "$B/openData/files/2017-superficies-et-volumes-en-production-par-produit-declaration-de-recolte-et-de-production-2017-2018.xls"
get produit_2018.xls  "$B/uploads/files/2019-06/2018-superficies-et-volumes-en-production-par-produit-declaration-de-recolte-et-de-production-2018-2019-pour-datadouane.xls"
get produit_2019.xlsx "$B/uploads/files/2020-03/2019%20-%20Superficies%20et%20volumes%20en%20production%20par%20produit%20-%20D%C3%A9claration%20de%20r%C3%A9colte%20et%20de%20production%202019-2020.xlsx"
get produit_2020.xls  "$B/2021-11/08/Copie%20de%20Superficies%20et%20volumes%20d%C3%A9clar%C3%A9s%20en%20production%202020%20OPENDATA.xls"
get produit_2021.xls  "$B/2022-07/11/Superficies%20et%20volumes%20d%C3%A9clar%C3%A9s%20en%20production%202021%20OPENDATA-1_0.xls"
get produit_2022.xlsx "$B/2023-06/20/Copie%20de%20Superficies%20et%20volumes%20d%C3%A9clar%C3%A9s%20en%20production%202022%20OPENDATA.xlsx"
get produit_2023.xlsx "$B/2024-08/12/Superficies%20et%20volumes%20d%C3%A9clar%C3%A9s%20en%20production%202023%20publication%20OPENDATA.xlsx"
get produit_2024.xlsx "$B/2025-05/25/Superficies%20et%20volumes%20d%C3%A9clar%C3%A9s%20en%20production%202024%20publication%20OPENDATA_0.xlsx"

echo "Terminé : $(ls "$D" | wc -l) fichiers dans $D"
