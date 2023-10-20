const equipes = ["England", "France", "Italy", "New Zealand", "Australia", "Ireland", "Scotland", "South Africa", "Argentina", "Wales"];

// Fonction pour remplir les menus déroulants avec les équipes
function remplirMenusDeroulants() {
    const equipe1Dropdown = document.getElementById("equipe1");
    const equipe2Dropdown = document.getElementById("equipe2");

    equipes.forEach((equipe) => {
        const option1 = document.createElement("option");
        option1.value = equipe;
        option1.text = equipe;
        equipe1Dropdown.appendChild(option1);

        const option2 = document.createElement("option");
        option2.value = equipe;
        option2.text = equipe;
        equipe2Dropdown.appendChild(option2);
    });
}
document.addEventListener("DOMContentLoaded", function () {
    // ...

    const predictButton = document.getElementById("predictButton");

    predictButton.addEventListener("click", function () {
        const equipe1Dropdown = document.getElementById("equipe1");
        const equipe2Dropdown = document.getElementById("equipe2");

        const equipe1 = equipe1Dropdown.value;
        const equipe2 = equipe2Dropdown.value;

        if (equipe1 === equipe2) {
            // Gérez ici l'erreur d'équipes identiques
            console.error('Les équipes domicile et exterieur ne peuvent pas être identiques.');
            return;
        }

        fetch(`http://127.0.0.1:5000/predict?domicile=${equipe1}&exterieur=${equipe2}`, {
            method: 'GET',
        })
            .then(response => response.json())
            .then(data => {
                const predictionResult = document.getElementById("predictionResult");
                const predictresult = document.getElementById("predictresult");
                predictionResult.textContent = `Taux de réussite pour l'équipe à domicile (${equipe1}): ${data.taux_reussite_domicile.toFixed(2)*100}%`;
                predictresult.textContent = `Taux de réussite pour l'équipe à l'extérieur (${equipe2}): ${data.taux_reussite_exterieur.toFixed(2)*100}%`;
                // Affichez également le taux de réussite pour l'équipe à l'exterieur de la même manière
            })
            .catch(error => {
                console.error('Erreur de prédiction :', error);
            });
    });
});


// function predictWinner() {
//     const equipe1Dropdown = document.getElementById("equipe1");
//     const equipe2Dropdown = document.getElementById("equipe2");
//     const predictionResult = document.getElementById("predictionResult");

//     const equipe1 = equipe1Dropdown.value;
//     const equipe2 = equipe2Dropdown.value;

//     const temperature = parseFloat(document.getElementById("temperature").value);
//     const precipitation = parseFloat(document.getElementById("precipitations").value);
//     const windSpeed = parseFloat(document.getElementById("vitesseVent").value);

//     fetch('/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//             domicile: domicile,
//             exterieur: extérieur,
//             conditions_meteo: {
//                 avg_temp_c: temperature,
//                 precipitation_mm: precipitation,
//                 avg_wind_speed_kmh: windSpeed
//             }
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Traiter les données de prédiction et afficher les résultats sur la page
//         predictionResult.textContent = `Taux de réussite pour ${equipe1}: ${data.taux_reussite_domicile.toFixed(2)}%`;
//     });
// }

// // Écouteur d'événement pour le bouton de prédiction
// const predictButton = document.getElementById("predictButton");
// predictButton.addEventListener("click", predictWinner);

// Appel de la fonction pour remplir les menus déroulants
remplirMenusDeroulants();
