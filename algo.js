// fetch('rugby_filtered_dataset.csv')
//   .then((response) => response.text())
//   .then((csvData) => {
//     // Ici, vous pouvez traiter les données CSV
//     console.log(csvData); // Cela affichera le contenu du fichier CSV dans la console
//   })
//   .catch((error) => {
//     console.error('Erreur lors de la récupération du fichier CSV :', error);
//   });


// // Fonction pour calculer la pondération des matchs en fonction de la date
// function calculerPonderation(matchDate, currentYear) {
//     const yearsAgo = currentYear - matchDate.getFullYear();
//     // Vous pouvez ajuster les pondérations en fonction de vos préférences
//     if (yearsAgo <= 5) {
//         return 1.0; // Matchs des 5 dernières années
//     } else {
//         return 0.5; // Matchs plus anciens, avec un poids réduit
//     }
// }

// // Fonction pour prédire le vainqueur d'un match entre deux pays
// function predireVainqueur(pays1, pays2) {
//     const currentYear = new Date().getFullYear();

//     // Filtrer les matchs entre les deux pays
//     const matchesEntrePays = donneesRugby.filter(match => 
//         ((match.home_team === pays1 && match.away_team === pays2) || 
//          (match.home_team === pays2 && match.away_team === pays1))
//     );

//     // Si aucun match n'a été joué entre ces deux pays, renvoyer "Match nul" avec un taux de réussite de 50% pour chaque équipe
//     if (matchesEntrePays.length === 0) {
//         return ["Match nul", 50.0, 50.0];
//     }

//     // Copier la tranche pour éviter l'erreur d'assignation
//     const matchesEntrePaysCopie = [...matchesEntrePays];

//     // Calculer le nombre de victoires de chaque équipe avec pondération
//     matchesEntrePaysCopie.forEach(match => {
//         match.ponderation = calculerPonderation(new Date(match.date), currentYear);
//     });

//     const victoiresPays1 = matchesEntrePaysCopie
//         .filter(match => (match.home_team === pays1 || match.away_team === pays1) && match.home_score > match.away_score && match.ponderation > 0)
//         .length;

//     const victoiresPays2 = matchesEntrePaysCopie
//         .filter(match => (match.home_team === pays2 || match.away_team === pays2) && match.home_score > match.away_score && match.ponderation > 0)
//         .length;

//     // Calculer le taux de réussite de chaque équipe
//     const totalPonderation = matchesEntrePaysCopie.reduce((total, match) => total + match.ponderation, 0);
//     let tauxReussitePays1 = Math.min((victoiresPays1 / totalPonderation) * 100, 100.0);
//     let tauxReussitePays2 = Math.min((victoiresPays2 / totalPonderation) * 100, 100.0);

//     // Assurez-vous que la somme des deux taux ne dépasse pas 100%
//     if (tauxReussitePays1 + tauxReussitePays2 > 100.0) {
//         tauxReussitePays1 = (tauxReussitePays1 / (tauxReussitePays1 + tauxReussitePays2)) * 100;
//         tauxReussitePays2 = (tauxReussitePays2 / (tauxReussitePays1 + tauxReussitePays2)) * 100;
//     }

//     return [tauxReussitePays1, tauxReussitePays2];
// }

// // Exemple d'utilisation
// const pays1 = "South Africa";
// const pays2 = "Italy";

// const [tauxReussitePays1, tauxReussitePays2] = predireVainqueur(pays1, pays2);

// console.log(`Taux de réussite pour ${pays1}: ${tauxReussitePays1.toFixed(2)}%`);
// console.log(`Taux de réussite pour ${pays2}: ${tauxReussitePays2.toFixed(2)}%`);


