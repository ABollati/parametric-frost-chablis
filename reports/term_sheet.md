# Term sheet — Couverture paramétrique gel de printemps

**Proposition indicative, non engageante — Document d'étude (assuré fictif)**
Référence : CHB-GEL-2027 · Date d'émission : 26 octobre 2026 · Offre valable jusqu'au 1er mars 2027

---

## 1. Parties

| | |
|---|---|
| **Assuré** | Coopérative viticole du Chablisien (fictive) |
| **Assureur** | [Assureur paramétrique — à désigner] |
| **Intermédiaire** | [Courtier — le cas échéant] |
| **Nature du contrat** | Assurance indicielle (paramétrique) : l'indemnité dépend uniquement de la valeur de l'indice, sans expertise des dommages ni preuve de perte |

## 2. Période et objet de la couverture

| | |
|---|---|
| **Année de couverture** | 2027 |
| **Période de risque** | Du 1er avril 2027 au 15 mai 2027 inclus (45 jours) |
| **Risque couvert** | Gel de printemps sur le vignoble, mesuré par l'indice défini à l'article 3 |

## 3. Indice

| | |
|---|---|
| **Variable** | Température minimale quotidienne sous abri, champ **TN** des données quotidiennes publiées par Météo-France, selon la définition de Météo-France |
| **Station de référence** | CHABLIS (Météo-France n° 89068001), Yonne |
| **Indice** | $`Z`$ = valeur la plus basse de TN relevée à la station de référence sur la période de risque |
| **Précision** | Valeurs exprimées au dixième de degré Celsius, telles que publiées ; aucun arrondi supplémentaire |
| **Données retenues** | Valeurs disponibles à la **date de figement**, à fixer d'après le délai de validation des données quotidiennes par Météo-France. Toute révision ultérieure est sans effet sur le règlement |

## 4. Données manquantes et station de secours

| | |
|---|---|
| **Station de secours** | **À désigner** avant la prise d'effet, parmi les stations Météo-France voisines, selon : distance et altitude proches de Chablis ; corrélation de TN avec Chablis les nuits de gel ; historique long et continu ; pérennité de la station |
| **Jours manquants** | Si TN est manquante ou invalidée à la station de référence pour un jour de la période, elle est remplacée par la valeur de la station de secours, corrigée de l'écart moyen entre les deux stations (relation calibrée avant la prise d'effet et annexée au contrat) |
| **Seuil d'invalidité** | Si plus de 5 jours sont manquants à la station de référence, ou si celle-ci est déplacée, fermée ou modifiée pendant la période, l'indice est calculé intégralement sur la station de secours, avec la même correction |
| **Défaillance des deux stations** | Recours à un agent de calcul indépendant désigné au contrat, sur la base des stations Météo-France les plus proches |

## 5. Structure de paiement

| | |
|---|---|
| **Seuil de déclenchement** $`z_1`$ | **−4,7 °C** |
| **Seuil de sortie** $`z_2`$ | **−6,0 °C** |
| **Limite** $`\ell`$ | **2 000 000 €** par année de couverture |
| **Indemnité** | $`I = \ell \times \min\left(1,\ \max\left(0,\ \dfrac{z_1 - Z}{z_1 - z_2}\right)\right)`$ |

Lecture : rien n'est payé si $`Z \ge -4{,}7`$ °C ; le paiement croît linéairement de 0 à la limite entre −4,7 et −6,0 °C, soit **153 846 € par dixième de degré** ; la limite est versée intégralement si $`Z \le -6{,}0`$ °C.

**Exemples**

| Indice $`Z`$ | Indemnité |
|---|---|
| −4,5 °C | 0 € |
| −4,9 °C (niveau observé en 2021) | 307 692 € |
| −5,3 °C | 923 077 € |
| −6,0 °C ou moins | 2 000 000 € |

Un seul paiement au plus par année de couverture.

## 6. Prime

| | |
|---|---|
| **Prime commerciale** | **195 000 €** hors taxes, taxes applicables en sus |
| **Taux sur limite** (*rate on line*) | 9,75 % |
| **Échéance** | Payable en totalité avant le 1er avril 2027 ; la garantie ne prend effet qu'à réception de la prime |

## 7. Règlement

| | |
|---|---|
| **Calcul** | Par l'assureur, à partir des données figées à la date de figement ; calcul communiqué à l'assuré avec les valeurs quotidiennes utilisées |
| **Délai de paiement** | 30 jours après la date de figement |
| **Contestation** | Dans les 30 jours suivant la communication du calcul ; seules les erreurs de calcul ou de transcription des données peuvent être contestées |

## 8. Points d'attention pour l'assuré

- **Risque de base.** L'indemnité dépend de la température mesurée à la station, pas des pertes réelles. Un gel peut causer des pertes sans déclencher de paiement (gel localisé, gel sur les coteaux plus doux que la station), et un paiement peut intervenir sans perte. Les pertes dues à la grêle, aux maladies ou à la sécheresse ne sont pas couvertes.
- **Couverture partielle d'un gel de type 2021.** Avec cette structure, un indice de −4,9 °C comme en 2021 donne lieu à environ 15 % de la limite. C'est la meilleure couverture de ce scénario compatible avec le budget : la couvrir davantage suppose une limite plus faible ou un budget plus élevé.

## 9. Conditions préalables à l'émission

- Désignation de la station de secours, calibration et annexion de sa relation avec la station de référence.
- Fixation de la date de figement des données.
- Validation du tarif par le comité de souscription.
- Rédaction du contrat définitif (*policy wording*) ; en cas de divergence, le contrat définitif prévaut sur la présente term sheet.
