# Note technique — Couverture paramétrique gel de printemps, vignoble de Chablis

*Document d'étude. Assuré fictif, données publiques réelles. Code : notebooks `01` à `04` du dépôt.*

## Résumé

Une coopérative du Chablisien demande une couverture contre le gel de printemps : limite 2 M€, budget de prime 200 k€, avec l'objectif de couvrir un gel comparable à celui de 2021. L'indice retenu est la température minimale sous abri la plus basse à la station Météo-France de Chablis, du 1er avril au 15 mai.

- **Le mandat est tendu.** Avec un chargement de sécurité et des frais, une seule des 9 hypothèses de chargement testées tient dans le budget, la plus favorable au client. La structure proposée (déclenchement −4,7 °C, sortie −6,0 °C) coûte 195 k€ mais ne verse qu'environ 15 % de la limite pour un gel de type 2021.
- **Le prix est très incertain.** Avec 64 années d'historique, l'intervalle de confiance à 95 % de la prime commerciale va de 65 à 341 k€.
- **Le risque de base n'est pas mesurable avec les données disponibles** : 14 années de rendements, 4 années de perte, des causes de perte mêlées.

**Recommandation** : coter la structure à 195 k€ en présentant au client le compromis entre limite, budget et couverture de 2021, et en l'informant explicitement du risque de base.

## 1. Mandat et indice

| | |
|---|---|
| Limite $`\ell`$ | 2 M€ par an |
| Budget | 200 k€ de **prime commerciale** (prix payé par le client) |
| Paiement | Linéaire entre un seuil de déclenchement $`z_1`$ et un seuil de sortie $`z_2`$ |
| Objectif | Couvrir les gels sévères, en particulier un gel de type 2021 |

**Indice.** $`Z_t = \min_j TN_{t,j}`$, où $`TN`$ est la température minimale quotidienne sous abri à la station de Chablis (89068001), pour $`j`$ du 1er avril au 15 mai.

L'indice a été fixé avant toute tarification, pour ne pas le choisir en fonction du prix obtenu. La fenêtre encadre le débourrement du Chardonnay, estimé en médiane au 13 avril par un modèle de degrés-jours en base 5 °C (GDD5 ; García de Cortázar-Atauri et al., 2009). L'indice reste simple et vérifiable par le client.

**Paiement.**
```math
I = \ell \cdot \min\left(1, \frac{(z_1 - Z)^+}{z_1 - z_2}\right)
```

## 2. Données

- **Températures** : Météo-France, données quotidiennes de l'Yonne, 1963–2026, soit 64 années complètes sur la fenêtre, toutes de code qualité 1.
  - TN est la seule variable disponible sur toute la période : TN50 n'a jamais été mesurée à Chablis, et TNSOL ne l'est que de 1993 à 2008.
  - L'indice moyen vaut −3,0 °C (écart-type 1,5 °C, minimum −6,0 °C).
- **Rendements** : douanes, rendements AOP de l'Yonne, 2009–2025. Ils servent d'approximation de ceux de la coopérative : les appellations Chablis représentent environ 70 % de la surface AOP du département, et les deux séries évoluent ensemble sur les années communes.
- **Perte** : taux de perte d'au moins 20 % par rapport à la moyenne des 3 années précédentes, soit 14 années (2012–2025). La moyenne olympique (5 années sans la plus haute ni la plus basse) sert de variante : 12 années.

## 3. Tarification

### 3.1 Méthode

La prime pure est l'espérance du paiement. Pour un paiement linéaire, elle s'écrit :

```math
\pi_{\text{pure}} = \mathbb{E}[I] = \frac{\ell}{z_1 - z_2}\int_{z_2}^{z_1} F(z)\,dz
```

où $`F`$ est la fonction de répartition de $`Z`$. Avec la loi empirique, cette intégrale est égale à la moyenne des paiements rejoués sur les 64 années (*burning cost*). Les deux calculs sont vérifiés égaux dans le code.

Le budget porte sur la prime commerciale :

```math
P_{\text{comm}} = \frac{\mathbb{E}[I] + \alpha\,\sigma(I)}{1 - f}
```

- Le chargement de sécurité suit le principe de l'écart-type (Kaas et al., chap. 5).
- $`f`$ représente les frais et le courtage, en part de la prime commerciale.
- Aucune valeur de marché de $`\alpha`$ ou de $`f`$ n'ayant pu être sourcée, on teste une grille d'hypothèses : $`\alpha \in \{0{,}1 ; 0{,}2 ; 0{,}3\}`$, $`f \in \{10 ; 20 ; 30\,\%\}`$.

**Choix de la structure.** Pour chaque couple $`(\alpha, f)`$, on balaye $`z_1`$ et $`z_2`$ au pas de 0,1 °C, sous trois contraintes :
- $`P_{\text{comm}} \le 200`$ k€ ;
- 2021 déclenche un paiement ;
- $`z_2 \ge -6{,}0`$ °C, la valeur la plus froide observée.

On retient la structure qui paie la plus grande part de la limite en 2021.

### 3.2 Résultats

Une seule hypothèse sur 9 est faisable : $`\alpha = 0{,}1`$, $`f = 10\,\%`$, la plus basse de la grille. Pour les autres, la prime commerciale minimale atteignable, parmi les structures qui paient 2021, dépasse le budget : de 206 k€ ($`\alpha = 0{,}1`$, $`f = 20\,\%`$) à 356 k€ ($`\alpha = 0{,}3`$, $`f = 30\,\%`$).

La cause est la forme du risque : le paiement est rare et massif, et son écart-type vaut environ 3 fois sa moyenne. Même un petit $`\alpha`$ pèse donc lourd.

**Structure retenue : $`z_1 = -4{,}7`$ °C, $`z_2 = -6{,}0`$ °C.**

| | |
|---|---|
| Fréquence de paiement | 8 années sur 64 (12,5 %) |
| Paiement pour un gel de type 2021 ($`Z = -4{,}9`$ °C) | 308 k€, soit 15 % de la limite |
| Années payées à la limite | 1973 et 1996 ($`Z = -6{,}0`$ °C) ; 2022 payée à 1,85 M€ |

### 3.3 Contrôle par une loi des valeurs extrêmes (GEV)

On ajuste une loi GEV sur $`-Z`$ par maximum de vraisemblance. Paramètre de forme : $`\hat\xi = -0{,}25`$. Une valeur négative implique une borne basse, estimée à −8,0 °C.

L'adéquation n'est pas rejetée. Les p-valeurs sont obtenues par bootstrap paramétrique, avec réajustement de la loi à chaque tirage et 500 tirages :
- Kolmogorov-Smirnov : $`p = 0{,}66`$ ;
- Anderson-Darling : $`p = 0{,}41`$.

Avec 64 points, ces tests ont toutefois peu de puissance. Dans la zone utile, la GEV donne une probabilité plus faible que la loi empirique : $`P(Z \le -4{,}9)`$ vaut 0,091 contre 0,125.

### 3.4 Incertitude sur la prime

Intervalles à 95 % par bootstrap percentile (Efron, 1979 ; Efron et Tibshirani, 1993). Pour la loi empirique, on rééchantillonne les 64 années, avec 5 000 tirages. Pour la GEV, on simule puis on réajuste, avec 500 tirages.

| Prime (k€) | Pure | Commerciale |
|---|---|---|
| Loi empirique | 132 [38 ; 248] | 195 [65 ; 341] |
| GEV | 110 [24 ; 177] | 164 [42 ; 253] |

- **L'incertitude d'estimation domine.** L'intervalle couvre un facteur de 5 à 6, alors que l'écart entre les deux lois n'est que de 22 k€ sur la prime pure.
- **Le budget est respecté en estimation centrale, pas avec assurance.** La prime commerciale dépasse 200 k€ dans 44 % des réplications bootstrap pour la loi empirique, et dans 19 % pour la GEV.
- Ces intervalles supposent des années indépendantes et de même loi.

## 4. Risque de base

On compare, sur les 14 années, les paiements de la structure retenue aux pertes de rendement :

| | Paiement | Pas de paiement |
|---|---|---|
| **Perte** | 1 (2021) | 3 (2013, 2016, 2024) |
| **Pas de perte** | 2 (2012, 2022) | 8 |

Les deux probabilités d'erreur, avec des intervalles exacts de Clopper-Pearson à 95 % (Clopper et Pearson, 1934) :
- $`q = P(\text{pas de paiement} \mid \text{perte}) = 3/4`$, intervalle [19 % ; 99 %] ;
- $`r = P(\text{pas de perte} \mid \text{paiement}) = 2/3`$, intervalle [9 % ; 99 %].

Avec la moyenne olympique, on obtient $`q = 2/3`$ et $`r = 1/2`$.

**Lecture.**
- Les estimations sont mauvaises, mais elles reposent sur 4 pertes et 3 paiements. Les intervalles couvrent presque tout [0 ; 1] : on ne peut conclure ni que l'indice est mauvais, ni qu'il est bon.
- Ces intervalles supposent des années indépendantes et une probabilité d'erreur constante. Deux éléments rendent ces hypothèses approximatives : les causes de perte sont mêlées, et la référence glissante lie les années entre elles. Cela ne fait que renforcer la conclusion.

**Origine des erreurs** (annexe `04`).
- Aucune station voisine (jusqu'à 45 km), ni aucune mesure plus proche du sol, ne classe 2016 et 2024 parmi les années froides. Le capteur n'est donc pas en cause.
- En 2024, la perte combine gel modéré, grêle du 1er mai et mildiou (Agri Bourgogne ; BIVB cité par Réussir ; DRAAF).
- 2016 et 2024 sont des années de pertes mêlées. En 2016 : gel fin avril (environ 20 % du vignoble de Chablis touché) puis grêle le 13 mai (environ 400 ha, près de 10 % du vignoble) (Decanter ; macommune.info). En 2024 : gel modéré, grêle du 1er mai et mildiou. Dans les deux cas, les dégâts de gel ont suivi un minimum sous abri d'environ −1,5 °C seulement à Chablis. Hypothèse : la sensibilité de la vigne dépend de son stade, ce qu'un seuil fixe sur une fenêtre fixe ne capte pas.
- La seule perte payée, 2021, est bien attribuée au gel : le président du BIVB évoque « -50% dans le Chablis » et dit ne « pas connaître d'endroit qui ait échappé au gel » (L'Info Durable, 24/09/2021). L'indice atteint −4,9 °C le 6 avril 2021.
- Les deux paiements sans perte correspondent à des gelées du 4 avril (2022) et du 17 avril (2012), autour du débourrement médian estimé. Sans estimation du débourrement de ces deux années, on ne peut pas conclure qu'elles sont survenues avant.

## 5. Recommandation

1. **Coter** la structure −4,7 / −6,0 °C à 195 k€. Cette cotation n'est possible qu'avec les hypothèses de chargement les plus basses, ce qui laisse peu de marge face à l'incertitude sur la prime.
2. **Présenter au client le compromis.** Dans le budget, un gel de type 2021 n'est couvert qu'à 15 %. Le couvrir mieux suppose une limite plus faible ou un budget plus élevé.
3. **Informer le client du risque de base.** Sur l'historique, l'indice n'a payé qu'une perte sur quatre, et il ne couvre ni la grêle, ni les maladies, ni les gels peu intenses sur une vigne débourrée.
4. **Avant émission** : désigner la station de secours et la calibrer, puis fixer la date de figement des données (voir la *term sheet*).

## 6. Ce que ce modèle ne sait pas

- **Stationnarité.** La tarification suppose que les 64 années suivent la même loi. C'est à tester par une GEV à paramètre de position dépendant du temps.
- **Phénologie.** Un indice calculé après un débourrement estimé par degrés-jours, ou une fenêtre ouverte au 15 mars, pourrait mieux suivre la sensibilité de la vigne. Ce n'est pas calibrable de façon fiable sur 14 années de pertes.
- **Représentativité de la station.** La station est en fond de vallée et compte parmi les plus froides du réseau les années de gel. Elle surestime probablement le froid subi sur les coteaux, ce qui augmente les paiements sans perte.
- **Chargements.** $`\alpha`$ et $`f`$ sont des hypothèses. Une approche par le coût du capital donnerait un chargement fondé sur le capital immobilisé.
- **Accumulation.** Pour un portefeuille de plusieurs vignobles, il faudrait étudier la corrélation des déclenchements entre stations.
- **Approche bayésienne.** Une loi a priori sur $`\xi`$, tirée de la littérature sur les extrêmes de température, intégrerait l'incertitude d'estimation dans la prime.

## Références

- Clopper, C. J., Pearson, E. S. (1934). The use of confidence or fiducial limits illustrated in the case of the binomial. *Biometrika*, 26(4), 404–413.
- Efron, B. (1979). Bootstrap methods: another look at the jackknife. *The Annals of Statistics*, 7(1), 1–26.
- Efron, B., Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall.
- García de Cortázar-Atauri, I., Brisson, N., Gaudillère, J. P. (2009). Performance of several models for predicting budburst date of grapevine (*Vitis vinifera* L.). *International Journal of Biometeorology*, 53, 317–326.
- Kaas, R., Goovaerts, M., Dhaene, J., Denuit, M. *Modern Actuarial Risk Theory*. Springer, chap. 5 « Premium principles ».
- Règlement (UE) 2021/2115, art. 76 : seuil de perte de 20 % et référence de rendement.
- Presse : Decanter, « Hail in Chablis vineyards adds to frost woes » (mai 2016) ; macommune.info, « Vin : après le gel, le vignoble de Chablis touché par la grêle » (14/05/2016) ; L'Info Durable, « Millesimus horribilis en Bourgogne : vendanges peau de chagrin » (24/09/2021) ; Agri Bourgogne (17/05/2024) ; Réussir (BIVB) ; DRAAF Bourgogne-Franche-Comté.
- Données : Météo-France (meteo.data.gouv.fr), données quotidiennes RR-T-Vent, département 89 ; DGDDI, déclarations de récolte.
