document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const equipe1 = urlParams.get("equipe1");
    const equipe2 = urlParams.get("equipe2");
    const pourcentage1 = parseFloat(urlParams.get("pourcentage1"));
    const pourcentage2 = parseFloat(urlParams.get("pourcentage2"));

    const matchResult = document.getElementById("matchResult");
    const equipe1Name = document.getElementById("equipe1-name");
    const equipe2Name = document.getElementById("equipe2-name");
    const equipe1Bar = document.getElementById("equipe1-bar");
    const equipe2Bar = document.getElementById("equipe2-bar");
    const equipe1Percent = document.getElementById("equipe1-percent");
    const equipe2Percent = document.getElementById("equipe2-percent");

    // Afficher le résultat du match
    matchResult.textContent = pourcentage1 > pourcentage2 ? `${equipe1} gagne !` : `${equipe2} gagne !`;

    // Afficher les détails des équipes
    equipe1Name.textContent = equipe1;
    equipe2Name.textContent = equipe2;

    // Mise à jour des barres de progression
    equipe1Bar.style.width = pourcentage1 + "%";
    equipe2Bar.style.width = pourcentage2 + "%";

    // Afficher les pourcentages dans les barres de progression
    equipe1Bar.textContent = pourcentage1.toFixed(2) + "%";
    equipe2Bar.textContent = pourcentage2.toFixed(2) + "%";

    // Mise à jour des pourcentages affichés à côté des barres de progression
    equipe1Percent.textContent = pourcentage1.toFixed(2) + "%";
    equipe2Percent.textContent = pourcentage2.toFixed(2) + "%";

    // Ajouter un gestionnaire d'événement pour le bouton "Réessayer"
    const retryButton = document.getElementById("retryButton");
    retryButton.addEventListener("click", function () {
        // Revenir à la page précédente (index.html)
        window.history.back();
    });
});

