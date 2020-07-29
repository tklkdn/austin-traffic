## Austin Traffic App

External libraries (Python):
- flask
- googlemaps
- sqlite3

Instructions:
1. Add your API key in the `getTraffic.py` file.
2. Install any of the external libraries you do not have.
3. Run the `main.py` file and keep it running while using the app.
4. Open Chrome (or possibly Safari) - this may not work with other browsers.
5. Enter "http://localhost:5000" in the address bar.

About the app:
- By default, the app will show current traffic.
- Higher scores means more severe traffic.
- The score for each region/route is relative to itself.
- Regions are color-coded in different shades of red based on traffic severity.
- You can enter a date and time to check predicted future traffic.
- Warning: It will NOT work for past dates and times.
- The buttons under "Your Commute" are not functional at this point.