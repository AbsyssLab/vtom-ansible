# Integration Ansible avec Visual TOM
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE.md)&nbsp;
[![fr](https://img.shields.io/badge/lang-en-red.svg)](README.md)

Ce projet permet l'intégration d'Ansible avec l'ordonnanceur Visual TOM. Il permet d'exécuter des playbooks à travers un Traiement modèle.

# Disclaimer
Aucun support ni garanties ne seront fournis par Absyss SAS pour ce projet et fichiers associés. L'utilisation est à vos propres risques.

Absyss SAS ne peut être tenu responsable des dommages causés par l'utilisation d'un des fichiers mis à disposition dans ce dépôt Github.

Il est possible de faire appel à des jours de consulting pour l'implémentation.

# Prérequis

 * Visual TOM 7.1.2 or greater 
 * python3
 * ansible
 * ansible-runner

# Consignes

Il faut disposer du module complémentaire de Python **ansible-runner", pour cela il exécuter les commandes suivantes avec le fichier requirement.txt fourni.

  ```Commande PIP à exécuter avec le fichier requirement.txt fourni 
pip install -U update
pip install -U -r requirement.txt
  ```

Le modèle **ansible.xml** est à importer sous VTOM, il contient 5 paramètres à renseigner obligatoirement ou optionnels :
 * Le répertoire de travail contenant le/les playbooks (obligatoire)
 * Le nom du playbook à exécuter (.yml) (obligatoire)
 * le fichier inventaire (chemin complet) (optionnel)
 * les variables supplémentaires (optionnel)
 * les tags (optionnel)

Le script Python **ansible.py** est exécuté à partir de la queue batch tom_submit.ansible
Renseigner le chemin complet du script **ansible.py** dans la queue batch. Si positionné dans $TOM_SCRIPT aucun changement à effectuer.

  ```à modifier
 Ligne 31 : python3 ${TOM_SCRIPT}/ansible.py 
  ```
# Actions disponibles

Il est possible d'exécuter des playbooks Ansible en indiquant des arguments obligatoires et optionnels.

<img width="688" height="350" alt="image" src="https://github.com/user-attachments/assets/ce176eb5-136c-47fd-af4e-4124e6133f84" />

## Arguments obligatoire
L'action principale est d'exécuter un Playbook Ansible en renseignant les deux entrées **obligatoires** suivantes :
- Playbook Path : Le répertoire contenant le/les playbooks
- Playbook : le playbook à exécuter

## Arguments optionnels

### Inventaire spécifique
- option : -i (inventory)
- Utilise un inventaire Ansible personnalisé
- Permet de cibler des environnements différents (prod, preprod, etc.)

### Variables dynamiques
- option : -e (extra vars)
- Injecte des variables Ansible (extra_vars)
- Permet de modifier le comportement du playbook sans le changer

### Tâches spécifiques
- option : -t (tags)
- Exécute uniquement les tasks / roles taggés
- Utile pour des opérations ciblées (patch, restart, deploy…)

# Licence
Ce projet est sous licence Apache 2.0. Voir le fichier [LICENCE](license) pour plus de détails.


# Code de conduite
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg)](code-of-conduct.md)  
Absyss SAS a adopté le [Contributor Covenant](CODE_OF_CONDUCT.md) en tant que Code de Conduite et s'attend à ce que les participants au projet y adhère également. Merci de lire [document complet](CODE_OF_CONDUCT.md) pour comprendre les actions qui seront ou ne seront pas tolérées.
