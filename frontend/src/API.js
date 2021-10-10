export default class APIs {
  static async getListOfCountries() {
    return await fetch("https://restcountries.eu/rest/v2/all")
      .then((r) => r.json())
      .catch(() => []);
  }
}
