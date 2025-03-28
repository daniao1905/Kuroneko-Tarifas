from flask import Flask, render_template, request
from scraper import obtener_tarifa_zona

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        peso = request.form["peso"]
        origen = request.form["origen"]
        destino = request.form["destino"]
        
        tarifa = obtener_tarifa_zona(peso, origen, destino)
        return render_template("resultado.html", tarifa=tarifa)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
