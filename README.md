### pydatascraper

pydatascraper is a Python application equipped with web scraping functionalities, enabling the extraction of Google and Yelp reviews. It features an intuitive graphical user interface (GUI) for effortless user interaction.

### Features

- **Web Scraping:** Extract information from web pages based on user-provided URLs.
- **Google Reviews:** Fetch reviews for a given business or location using Google Maps API.
- **Yelp Reviews:** Retrieve reviews for a business using the Yelp API.
- **OpenStreetMap Data:** Extract latitude, longitude, and additional information from OpenStreetMap.

#### Requirements

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`
  - `nltk` (for text processing)
  - `tkinter` (GUI toolkit)

#### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/arjunlimat/pydatascraper.git
   
   ```

2. Install the package directly:

```

pip install pydatascraper

```
3. import the webscraper model:

```
from pydatascraper.pyscraper import main
```
4. Run the application:
```
main()
```

The GUI will appear, allowing you to choose different services and perform web scraping tasks.

#### Services
Web Scraping

Enter a URL and click "Search" to explore available data types.

Choose the desired data type, enter a file name, and click "Download" to save the data.

#### Google Reviews
Select "Google reviews" from the services dropdown.

Enter the business or location name and address.
Provide a file name and click "Download" to fetch and save Google reviews.

#### Yelp Reviews
Select "Yelp reviews" from the services dropdown.
Enter the business name and address.
Provide a file name and click "Download" to fetch and save Yelp reviews.

#### OpenStreetMap
Select "Open Street Map" from the services dropdown.
Enter the map URL, provide a file name, and click "Download" to extract map data.

#### Contributing
Contributions are welcome! If you encounter issues or have ideas for improvement, please open an issue or submit a pull request.

#### License:
This project is licensed under the MIT License - see the LICENSE file for details.
