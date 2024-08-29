# DepremAPI
# Earthquake Data Analysis and Visualization Project
 
## Project Overview
This project is designed to fetch live earthquake data from an observatory API, process it, and import it into a database for analysis. It also provides visualization of the earthquake data using Python libraries. The system continuously fetches data at regular intervals to ensure the display of up-to-date information.
 
### Tasks:
- Fetching and processing live data from the earthquake observatory API.
- Importing processed data into the database.
- Visualizing the data using Python libraries.
- Ensuring regular intervals for data fetching to display the latest information.
 
## Data Transformation and Modeling
The script transforms raw data fetched from the API into a suitable format for storage in the database.
 
## Visualization
The earthquake data is visualized using Python libraries such as Matplotlib, Plotly, or Seaborn. The script generates visualizations like bar charts, line plots, or any other appropriate graph types to represent the earthquake data.
 
## Continuous Streaming
The script runs in a loop, fetching new data from the API at regular intervals (e.g., every 10 minutes). The visualization updates accordingly to reflect the latest earthquake information.
 
## Technologies Used
- Python
- SQL
- HTML/CSS
- JavaScript
- Flask for Python
- Microsoft Azure
- GitHub
 
## Requirements
To run this project, you'll need the following:
- Python libraries needed for the project.
- API key for the earthquake observatory API.
- Connection to the Azure database.
 
## Getting Started
To clone and run this application, follow these steps:
 
1. Clone the project files to your local machine:
   ```
   git clone https://github.com/ItelligenceTurkeyAnalytics/earthquakeapi
   ```
 
2. Install required packages:
   ```
   pip install libraries
   ```
 
3. Set up Azure database connection:
   - Obtain necessary connection credentials for your Azure database.
   - Configure the database connection settings in your project.
 
4. Run the application:
   ```
   python app.py
   ```
 
5. Access the web interface:
   - Once the application is running, access the web interface by opening a browser and navigating to [http://localhost:5000](http://localhost:5000).
 
## Project Structure
- **app.py**: Contains the main Flask application setup and routing logic.
- **templates folder**: Includes HTML files for the web interface pages.
- **database_config.py** (or similar): Configuration file for setting up the connection to the Azure database.
- **README.md**: The documentation file providing project information and instructions.
 
## Contribution
Contributions are welcome! Feel free to submit pull requests for any improvements or additional features.
