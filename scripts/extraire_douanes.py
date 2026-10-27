"""Extraction des rendements viticoles depuis les fichiers des douanes (DGDDI, déclarations de récolte).

Entrées  (data/raw/douanes/, téléchargées par telecharger_douanes.sh) :
  - dept_AAAA.xls(x)    : « Production AAAA des vins par département », 2009-2025
  - produit_AAAA.xls(x) : « Superficies et volumes en production par produit », 2017-2024

Sorties (data/processed/) :
  - douanes_yonne_aop_2009_2025.csv          : surface, volumes et rendement AOP de l'Yonne
  - douanes_chablis_appellations_2017_2024.csv : appellations Chablis (toutes) et Chablis village

Usage : python scripts/extraire_douanes.py [--out DOSSIER]
Dépendances : pandas, xlrd (.xls), openpyxl (.xlsx)
"""
import argparse
import glob
import warnings
from pathlib import Path

import pandas as pd

warnings.filterwarnings("ignore", message="Cannot parse header or footer")

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "douanes"

# ---------------------------------------------------------------------------
# 1. Fichiers départementaux : position des colonnes dans la ligne « 89 YONNE »
#    (vérifiée sur les en-têtes de chaque format de fichier)
# ---------------------------------------------------------------------------
# 2009      : col 3 surface AOC | 7 blancs | 8 rouges ou rosés (confondus)
# 2010-2011 : col 3 surface AOP | 6 blancs | 7 rouges ou rosés (confondus)
# 2012-2013 : col 3 surface AOP | 7 blanc  | 8 rouge | 9 rosé            (pas de VSI/VCI)
# 2014-2025 : col 3 surface AOP | 7 blanc  | 8 rouge | 9 rosé | 10 VSI/VCI
#   (le fichier 2015 a une colonne « VCI » supplémentaire en col 14, côté IGP : ignorée)

def colonnes_dept(annee):
    if annee == 2009:
        return {"surface": 3, "blanc": 7, "rouge": 8, "rose": None, "vsi_vci": None}
    if annee in (2010, 2011):
        return {"surface": 3, "blanc": 6, "rouge": 7, "rose": None, "vsi_vci": None}
    if annee in (2012, 2013):
        return {"surface": 3, "blanc": 7, "rouge": 8, "rose": 9, "vsi_vci": None}
    return {"surface": 3, "blanc": 7, "rouge": 8, "rose": 9, "vsi_vci": 10}


def lire(fichier):
    return pd.read_excel(fichier, header=None, dtype=object)


def verifier_en_tetes(brut, cols, fichier):
    """Contrôle que chaque colonne utilisée porte le bon libellé dans l'en-tête."""
    premiere = brut.index[brut.apply(lambda r: r.astype(str).str.contains("AIN").any(), axis=1)][0]
    for nom, c in cols.items():
        if c is None:
            continue
        texte = " ".join(str(x) for x in brut.iloc[:premiere, c] if pd.notna(x)).upper()
        attendus = {"surface": ("A.O", "AOP"), "blanc": ("BLANC",), "rouge": ("ROUGE",),
                    "rose": ("ROS",), "vsi_vci": ("VSI",)}[nom]
        assert any(a in texte for a in attendus), f"{fichier}: colonne {c} ({nom}) inattendue : {texte[:80]}"


def extraire_yonne():
    lignes = []
    for annee in range(2009, 2026):
        fichier = Path(glob.glob(str(RAW / f"dept_{annee}.*"))[0])
        brut = lire(fichier)
        cols = colonnes_dept(annee)
        verifier_en_tetes(brut, cols, fichier.name)
        yonne = brut[brut.apply(lambda r: r.astype(str).str.contains("YONNE", case=False).any(), axis=1)]
        assert len(yonne) == 1, f"{fichier.name}: {len(yonne)} lignes Yonne"
        v = yonne.iloc[0]
        val = lambda c: float(v[c]) if c is not None and pd.notna(v[c]) else None
        blanc, rouge, rose, vci = val(cols["blanc"]), val(cols["rouge"]), val(cols["rose"]), val(cols["vsi_vci"])
        surface = val(cols["surface"])
        recolte = sum(x for x in (blanc, rouge, rose, vci) if x is not None)
        lignes.append({
            "annee": annee, "fichier": fichier.name, "surface_aop_ha": surface,
            "aop_blanc_hl": blanc, "aop_rouge_hl": rouge, "aop_rose_hl": rose, "aop_vsi_vci_hl": vci,
            "rouge_et_rose_confondus": cols["rose"] is None,
            "recolte_aop_hl": recolte,
            "rendement_aop_hl_ha": recolte / surface,
            "part_rouge_rose": (rouge + (rose or 0)) / (blanc + rouge + (rose or 0)),   # hors VSI/VCI
            "part_vci": vci / recolte if vci is not None else None,
        })
    return pd.DataFrame(lignes)


# ---------------------------------------------------------------------------
# 2. Fichiers par produit : toutes les lignes AOP dont le libellé contient « chablis »
#    (Chablis, Petit Chablis, premiers et grands crus). Les lignes confidentialisées
#    (surface ou volume masqués) sont exclues et comptées.
# ---------------------------------------------------------------------------
def extraire_chablis():
    lignes = []
    for annee in range(2017, 2025):
        fichier = Path(glob.glob(str(RAW / f"produit_{annee}.*"))[0])
        brut = lire(fichier)
        en_tete = brut.index[brut[0].astype(str).str.strip() == "Segmentation"][0]
        assert "Volumes totaux produits" in str(brut.iloc[en_tete, 4])
        t = brut.iloc[en_tete + 1:, :5].copy()
        t.columns = ["segment", "code", "libelle", "surface", "volume"]
        t = t[(t["segment"].astype(str).str.strip() == "AOP")
              & t["libelle"].astype(str).str.contains("chablis", case=False)]
        s = pd.to_numeric(t["surface"], errors="coerce")
        v = pd.to_numeric(t["volume"], errors="coerce")
        ok = s.notna() & v.notna()
        village = t[t["libelle"].astype(str).str.strip().str.lower() == "chablis"]
        assert len(village) == 1, f"{fichier.name}: {len(village)} lignes « Chablis »"
        lignes.append({
            "annee": annee,
            "chablis_toutes_app_surface_ha": s[ok].sum(),
            "chablis_toutes_app_volume_hl": v[ok].sum(),
            "chablis_toutes_app_rdt": v[ok].sum() / s[ok].sum(),
            "n_lignes_confidentielles": int((~ok).sum()),
            "chablis_village_rdt": float(village["volume"].iloc[0]) / float(village["surface"].iloc[0]),
        })
    return pd.DataFrame(lignes)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(ROOT / "data" / "processed"))
    out = Path(p.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    yonne = extraire_yonne()
    chablis = extraire_chablis()
    yonne.to_csv(out / "douanes_yonne_aop_2009_2025.csv", index=False)
    chablis.to_csv(out / "douanes_chablis_appellations_2017_2024.csv", index=False)
    print(yonne[["annee", "surface_aop_ha", "recolte_aop_hl", "rendement_aop_hl_ha"]].round(1).to_string(index=False))
    print(f"\nÉcrit dans {out}")
