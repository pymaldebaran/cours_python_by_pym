# Le champ de Noël

## Un champ...

1.	Afficher (avec des print dans un terminal) un rectangle dont les bord sont
	des "#" avec de réparti aléatoirement dedans des arbres (que tu représentera
	par une lettre O).
2. 	À chaque fois qu'on lance le programme les arbres doivent être à un endroit
	différent.
3.	Et, dans un premier temps au moins, tu va fixer la taille de ton champ (le
	rectangle) en dur dans ton code. Ce n'est donc pas un paramètre. Idem pour
	le nombre d'arbre.

## ...mais un champ de Noël

### Instructions

Tu va encore dessiner un champ avec des arbres placés aux hasard dessus. Sauf que maintenant un arbre ça sera ça :


```
   ^
  ^ ^
 (o  )
(o  o )
   U
```

Parce que c'est plus dur comme ça hein 😉

### Objectifs

1. La position correspondra à celle du pied du sapin
2. Pour te faciliter quand même un peu la life : tu laissera 3 lignes vide au dessus du champ, 2 colonnes vides à droite et à gauche aussi.
Ça assurera que tes sapin de noël auront bien place d'être dessinés en entier.
3. Et, bien sûr, je veux que ceux dessiner "devant" (c'est à dire en bas du champ vu qu'on a de la "perspective") soit bien dessinés devant ceux qui sont "au fond" (donc en haut).

### Indices

Si tu veux je peux te mettre sur la bonne voie car le but ici n'est pas que tu t'arrache la tête sur les algorithmes qui marche ± bien. (pour moi l'important c'est que tu sache exprimer tout ce que tu pense en python… faire de toi une boss en algorithmie… appelons ça le plan B)

Alors le pb de tes programmes actuels c'est que tu te concentre sur l'idée d'afficher qqch à l'écran… Alors qu'en fait c'est secondaire.

Tu te raccroche à la fonction `print` car c'est ce que tu maîtrise bien.

Tu va faire autrement cette fois :
Plutôt que de choisir la position des arbre puis printer à l'écran le champ ligne par ligne le champ… tu va créé une **représentation en mémoire** de ton champ : une grosse liste (ligne) de liste (colonne) de caractères et tu va écrire dedans en accédant directement comme ça par exemple :

```
virtual_champ[y][x] = "o"
```

Ainsi tu pourra la modifier comme tu veux et dans l'ordre que tu veux. Et à la fin quand tu aura tout "dessiné" dedans tu l'afficheras ligne par ligne à l'écran. C'est ce qu'on appelle construire un "modèle".

## Si on veut aller plus loin

Liste de trucs cool si on voulait améliorer notre programme à fond :

- gérer vraiment la transperence
- prendre les paramètres (taille, nb d'arbre) en paramètre du programme
- dessiner en couleur
- etc

