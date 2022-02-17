from outils import Theme, Api

class Meteo(Theme.Theme):
    def __init__(self):
        super().__init__("meteo")

        super().ajouterReconnaisseur("meteo")
        super().ajouterConnecteur("a")

        self.api = MeteoApi()

    def action(self, ville):
        self.api.envoyerRequest(ville)

class MeteoApi(Api.Api):
    def __init__(self):
        super().__init__()

        self._API_KEY = "513cf5bef2bd3c00f2b188521ba509d9"
        self.URL = "https://api.openweathermap.org/data/2.5/weather?"

        self.derniereVille = {}

    def parametre(self, nom_ville):
        return f"q={nom_ville}&appid={self._API_KEY}"

    def envoyerRequest(self, nom_ville):
        reponse = super().getRequest(nom_ville)
        if super().checkRequestStatus(reponse):
            self.derniereVille = self._castToJson(reponse)
            self.afficherInfoMeteo()
        else:
            print("Error in the request.",reponse.status_code, reponse.json()["message"])

    def afficherInfoMeteo(self):
        if self.derniereVille.get("temp") is not None:
            print(f"{self.derniereVille['city']:-^50}\n\tTemperature: {self.derniereVille['temp']}°\n\tHumidity: {self.derniereVille['humidity']}%\n\tPressure: {self.derniereVille['pressure']}Pa\n\tWeather Report: {self.derniereVille['weather_report']}\n{'':-^50}")
        else:
            print(f"{'':-^50}\n\tNo city entered\n{'':-^50}")

    def _castToJson(self, reponse):
        data = reponse.json()
        main = data['main']
        return {"city":data["name"],
                "temp":round(main['temp']-273.15,2),
                "humidity":main['humidity'],
                "pressure":main['pressure'],
                "weather_report":data['weather'][0]['description']}