from flask import Flask, request, jsonify
import algo  # Importez votre module algo.py
from flask_cors import CORS

# ...

app = Flask(__name__)
CORS(app)


# Route GET pour prédire les résultats
@app.route('/predict', methods=['GET'])
def predict():
    print('test')
    domicile = request.args.get('domicile')
    exterieur = request.args.get('exterieur')
    print(domicile)
    if domicile == exterieur:
        return jsonify({
            'error': 'Les équipes domicile et exterieur ne peuvent pas être identiques.'
        })
        
    
    taux_reussite_domicile, taux_reussite_exterieur = algo.prédire_vainqueur(domicile, exterieur)
    print(domicile)
    return jsonify({
        'taux_reussite_domicile': taux_reussite_domicile,
        'taux_reussite_exterieur': taux_reussite_exterieur
    })
















if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         # Obtenez les données du formulaire ou de la requête AJAX, faites votre prédiction
#         domicile = request.form['domicile']
#         exterieur = request.form['exterieur']
#         taux_reussite_domicile, taux_reussite_exterieur = algo.prédire_vainqueur(domicile, exterieur)
#         return render_template('details_match.html', domicile=domicile, exterieur=exterieur, taux_reussite_domicile=taux_reussite_domicile, taux_reussite_exterieur=taux_reussite_exterieur)
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
