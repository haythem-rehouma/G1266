# Exercice : Identifier le type d’environnement en Apprentissage par Renforcement (AR)

# 1 - *Note*:

Pour chaque exemple, le contexte est précisé explicitement afin que vous puissez facilement identifier :  
- **Qui est l’agent (celui qui interagit avec l’environnement)**  
- **Qu’est-ce que l’environnement (ce qui change ou non autour de l’agent)**  
- **Ce qui est connu/prévisible (déterministe) ou inconnu/imprévisible (stochastique)**  
- **Ce qui change indépendamment ou non des actions de l’agent (dynamique ou statique)**  



# 2 - **Consigne :**  
Pour chaque cas, déterminez précisément si l’environnement décrit est :  
- **Statique déterministe**
- **Statique stochastique**
- **Dynamique déterministe**
- **Dynamique stochastique**

Justifiez brièvement votre choix.


# 3 - **Exemples détaillés à compléter :**

**1. Renouvellement hypothécaire à taux fixe mais changeant chaque 5 ans :**  
- **Agent :** Propriétaire qui renouvelle son hypothèque.  
- **Environnement :** Marché hypothécaire avec taux révisé tous les 5 ans. Le taux futur est inconnu.  
⇒ Type : ………… (justification)

**2. Tweet imprévisible de Donald Trump affectant immédiatement le marché financier :**  
- **Agent :** Investisseur sur le marché boursier.  
- **Environnement :** Marché boursier influencé par les tweets aléatoires et inattendus d’une personnalité politique.  
⇒ Type : ………… (justification)

**3. Abonnement Netflix mensuel à tarif fixe garanti pendant 12 mois :**  
- **Agent :** Abonné Netflix.  
- **Environnement :** Tarif Netflix immuable durant l’année d’abonnement, aucun changement sans action de l’abonné.  
⇒ Type : ………… (justification)

**4. Coupure électrique programmée annoncée par Hydro-Québec :**  
- **Agent :** Résident qui reçoit l’électricité.  
- **Environnement :** Réseau électrique, interruption prévue et annoncée clairement à l’avance, hors contrôle du résident.  
⇒ Type : ………… (justification)

**5. Coupure électrique soudaine imprévue (tempête) :**  
- **Agent :** Résident qui reçoit l’électricité.  
- **Environnement :** Réseau électrique coupé soudainement à cause d'une météo imprévisible.  
⇒ Type : ………… (justification)

**6. Date fixe connue à l’avance de fermeture annuelle de votre compte bancaire :**  
- **Agent :** Titulaire du compte bancaire.  
- **Environnement :** Banque avec date fixe et prédéfinie pour fermer les comptes chaque année.  
⇒ Type : ………… (justification)

**7. Tweet imprévisible d’Elon Musk sur le Bitcoin :**  
- **Agent :** Investisseur en cryptomonnaie.  
- **Environnement :** Valeur du Bitcoin influencée soudainement et aléatoirement par tweets d’Elon Musk.  
⇒ Type : ………… (justification)

**8. Lancer un dé pour déterminer le dividende annuel d’une action virtuelle (aucun dividende si pas d’action de l’agent) :**  
- **Agent :** Investisseur décidant de recevoir un dividende.  
- **Environnement :** Dividende payé uniquement après une action de l’investisseur, montant aléatoire déterminé par le dé.  
⇒ Type : ………… (justification)

**9. Compte d’épargne à intérêt fixe garanti pendant 10 ans :**  
- **Agent :** Titulaire du compte d’épargne.  
- **Environnement :** Banque avec un taux fixe connu et garanti, sans changement spontané durant les 10 ans.  
⇒ Type : ………… (justification)

**10. Élections présidentielles américaines tous les 4 ans (date fixe connue, mais résultat imprévisible) :**  
- **Agent :** Investisseur en bourse anticipant l’impact électoral sur ses investissements.  
- **Environnement :** Date de l’élection connue et immuable, mais le gagnant (résultat) est totalement imprévisible.  
⇒ Type : ………… (justification)

**11. Faillite inattendue d’une grande entreprise cotée en bourse :**  
- **Agent :** Investisseur actionnaire.  
- **Environnement :** Marché boursier impacté par une faillite surprise, imprévisible pour l’agent.  
⇒ Type : ………… (justification)

**12. Jeu de roulette au casino (rien ne se passe sans votre mise) :**  
- **Agent :** Joueur plaçant sa mise.  
- **Environnement :** Résultat aléatoire après la mise seulement. Aucun changement spontané sans action de l’agent.  
⇒ Type : ………… (justification)

**13. Coucher du soleil chaque jour selon un calendrier astronomique précis :**  
- **Agent :** Photographe attendant de prendre une photo du coucher de soleil.  
- **Environnement :** Soleil se couche à une heure précise, indépendante des actions de l’agent, prévisible précisément.  
⇒ Type : ………… (justification)

**14. Changement imprévisible du prix de l’essence chaque semaine :**  
- **Agent :** Automobiliste devant faire le plein.  
- **Environnement :** Prix de l’essence modifié régulièrement sans préavis, totalement imprévisible.  
⇒ Type : ………… (justification)

**15. Prix fixe garanti annuel d’abonnement au gym :**  
- **Agent :** Abonné du gym.  
- **Environnement :** Tarif d’abonnement annuel fixe, sans variation durant l’année en cours.  
⇒ Type : ………… (justification)

**16. Hausse surprise du tarif mensuel de votre fournisseur internet :**  
- **Agent :** Abonné internet.  
- **Environnement :** Fournisseur augmentant soudainement le tarif sans avertir préalablement l’abonné.  
⇒ Type : ………… (justification)

**17. Lancer d’une pièce de monnaie (pile ou face) quand vous décidez de jouer :**  
- **Agent :** Joueur qui décide de lancer la pièce.  
- **Environnement :** Résultat du lancer aléatoire. Sans lancer, rien ne se passe.  
⇒ Type : ………… (justification)

**18. Versement mensuel d’un loyer fixe pendant toute la durée d’un bail :**  
- **Agent :** Locataire payant chaque mois.  
- **Environnement :** Montant du loyer fixe garanti par contrat, ne change pas spontanément.  
⇒ Type : ………… (justification)

**19. Pluie imprévue affectant votre barbecue extérieur planifié :**  
- **Agent :** Personne organisant le barbecue.  
- **Environnement :** Conditions météo aléatoires et imprévisibles perturbant le barbecue prévu.  
⇒ Type : ………… (justification)

**20. Trafic routier dense à heure fixe tous les jours ouvrables (prévisible selon l’horaire) :**  
- **Agent :** Conducteur quotidien.  
- **Environnement :** Embouteillage quotidien systématique à heure précise, parfaitement prévisible.  
⇒ Type : ………… (justification)

---

# 4 - Exemple de réponse complète (exemple de correction) :

> **Renouvellement hypothécaire tous les 5 ans à taux inconnu ⇒** **Dynamique stochastique**  
> **Justification :** Le taux évolue indépendamment des actions du propriétaire (dynamique), et le taux futur est imprévisible (stochastique).

