# 1 - Introduction au TD Learning : une méthode d'estimation pas à pas

- Dans cette nouvelle section, nous allons explorer une autre approche puissante appelée **TD Learning (Temporal Difference Learning)**. 
- Contrairement aux méthodes Monte Carlo qui attendent la fin d’un épisode complet, les méthodes TD permettent de mettre à jour les estimations **en temps réel**, au fur et à mesure que l’agent avance dans l’environnement.

# 2 - Pourquoi le TD Learning ?

Les méthodes Monte Carlo ont leurs avantages, mais elles présentent aussi certaines **limitations** :
1. **Elles doivent attendre la fin de l’épisode** pour pouvoir estimer la valeur d’un état, ce qui peut être long ou impossible si l’épisode ne se termine jamais.
2. **Elles ne sont pas idéales pour les environnements continus ou très longs**, où l’attente d’une fin complique la mise à jour.

Les méthodes TD (comme **TD(0)**, **TD(n)** ou encore **SARSA**) apportent des solutions efficaces :
-  Elles **n'ont pas besoin d'attendre la fin de l'épisode** : on peut commencer à apprendre dès la première étape.
-  Elles permettent un **apprentissage en ligne**, parfait pour les environnements en continu ou à durée indéterminée.
-  Elles combinent les avantages des méthodes de Monte Carlo et de la programmation dynamique.

# 3 -  Qu'allons-nous faire ?

Nous allons commencer par la méthode **TD(0)**, la version la plus simple du TD Learning :
- Elle met à jour la valeur d’un état **immédiatement après avoir observé la récompense suivante et l’état suivant**.
  
Ensuite, nous étendrons la méthode avec :
1. **TD(n)**, qui permet de prendre en compte plusieurs étapes futures.
2. **SARSA** : une méthode de contrôle basée sur le TD, qui apprend à la fois les valeurs et la politique.
3. **Q-learning** : une autre méthode basée sur le TD, qui apprend la valeur optimale indépendamment de la politique suivie.

Nous appliquerons ces concepts dans un environnement concret (par exemple **FrozenLake**), où un agent apprend progressivement à choisir les meilleures actions, sans attendre la fin du jeu.

<br/>

# 3 - Résumé avec une explication plus simple

**TD Learning**, ou apprentissage par différence temporelle, est une méthode qui permet à un agent d’apprendre **au fil de ses expériences, sans attendre la fin du jeu**. 
- Imagine que tu joues à un jeu vidéo et qu’à chaque action, tu obtiens un petit indice sur si tu vas gagner ou pas — tu n’attends pas d’avoir fini le jeu pour tirer des leçons : tu apprends tout de suite, action par action. C’est ça, le cœur du TD Learning.
- Si Monte Carlo consiste à observer tout un film avant de donner son avis, TD Learning te permet de **donner une critique dès la première scène**, et de la corriger au fur et à mesure que tu avances. Cela rend l’apprentissage plus rapide, surtout quand le film est long ou infini.

<br/>

# 3 - TD Learning, c’est la science du "j’apprends au fur et à mesure" (l’art d’apprendre **au fil de l’expérience**)



Avec le **TD Learning**, on n’attend pas la fin d’un épisode pour apprendre : **on ajuste ses estimations à chaque étape, en temps réel**. C’est l’équivalent, dans la vie quotidienne, de goûter un plat pendant que tu le cuisines, plutôt que d’attendre de l’avoir servi pour juger s’il est bon.

- **TD Learning** : À chaque étape de la recette, tu goûtes, tu ajustes le sel, tu modifies la cuisson. Tu apprends **pendant l’action**.
- **Monte Carlo** : Tu prépares le plat entier sans y toucher, tu attends le verdict final à la première bouchée… et si ce n’est pas bon, tu recommences depuis le début.

Autrement dit, **Monte Carlo apprend en observant des trajectoires complètes**, alors que **TD Learning apprend pas à pas, dès qu’une information est disponible**. Cela en fait une méthode bien plus adaptée aux environnements continus ou longs, où attendre la fin est trop coûteux — voire impossible.




# 4 - Exemples simpels de la vraie vie pour illustrer TD Learning (Temporal Difference Learning)

-  **Tu veux apprendre à bien saler tes pâtes** : tu goûtes une fourchette après 3 minutes, tu ajoutes un peu de sel, tu regoûtes à 5 minutes, tu ajustes... et à la fin, c’est (presque) parfait. C’est du TD Learning : **on ajuste à chaque étape**.

-  **Tu veux devenir bon en karaoké** : à chaque fausse note, tu regardes la tête de ton public et tu baisses un peu le volume. Tu ajustes ton ton couplet après couplet… pas besoin d’attendre la fin de la chanson pour corriger le tir !

-  **Tu veux prendre une douche pas trop froide ni trop chaude** : tu ouvres l’eau, tu testes la température avec la main, tu ajustes, tu retestes, tu réajustes… Tu ne restes pas gelé 10 minutes à attendre de voir si ça s’arrange tout seul.

-  **Tu veux apprendre à bien servir au ping-pong** : tu testes un service, l’autre rate complètement. Tu tentes avec un peu plus d’effet, ça passe mieux. Tu ajustes à chaque échange — pas besoin de perdre 21-0 pour comprendre.

-  **Tu veux laver la vaisselle sans inonder la cuisine** : tu ouvres un peu l’eau, tu vois que ça éclabousse, tu fermes un peu, tu ajustes la pression. Tu n’attends pas la fin de la pile de vaisselle pour comprendre que ça déborde.



Bref, **TD Learning, c’est apprendre à chaque pas**, pas à la fin du chemin. Tu avances, tu observes, tu corriges.

<br/>



# 4 - Nos anciens connaissaient déjà le principe du TD Learning

Bien avant les algorithmes, nos grands-parents savaient que **la meilleure façon d’apprendre, c’est d’observer, de corriger, et de s’adapter**. Dans les pays arabes, on dit souvent : **« ʿīnek mīzānek »** – « Tes yeux sont ta balance ». Cela signifie qu’au lieu de suivre une règle figée, on ajuste **en fonction de ce qu’on voit, de ce qu’on ressent, et de ce qui se passe ici et maintenant**.

Ce proverbe illustre parfaitement l’idée du **TD Learning** : on apprend à chaque étape, à partir de l’expérience immédiate, sans attendre la fin du processus pour tirer des leçons. C’est l’opposé d’un apprentissage théorique : **on ajuste en temps réel, parce qu’on fait confiance à ce que la réalité nous montre**.



Dans ce sens, **TD Learning** est une formalisation algorithmique de ce principe ancestral :  
> **"Regarde, ajuste, puis apprends. Pas l’inverse."**

D'autres cultures partagent cette philosophie :
- **Proverbe africain** : *« Ce n’est pas au bout du chemin qu’on redresse ses sandales. »*
- **Proverbe anglais** : *« Don’t fix it all at once — fix it as you go. »*

Toutes ces sagesses expriment la même idée :  
👉 **Le vrai apprentissage ne se fait pas à la fin — il se fait à chaque instant, en corrigeant avec les yeux ouverts.**


De la cuisine au jardinage, du bricolage à l’enseignement, nos aînés pratiquaient déjà, sans le nommer, un apprentissage par différences temporelles — celui de **l’intuition corrigée par l’expérience**.

