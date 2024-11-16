# 🏠 House Rental Price Prediction in Sri Lanka

This application predicts monthly rental prices of houses in various districts across Sri Lanka. The predictions are based on a machine learning model trained on historical data, taking into account key features such as the number of bathrooms, bedrooms, house size, and land size.

## Files in the Repository

- **`app.py`**: This is the main file that contains the Streamlit app code.
- **`best_model.pkl`**: This is the trained machine learning model used for predicting rental prices.
- **`Monthly_house_rental_prices_in_Sri_Lanka.csv`**: The dataset used to train the model, containing historical house rental data for different districts.
- **`requirements.txt`**: A list of dependencies required to run the application.

## 🌟 Features

- **District**: Select from the available districts in Sri Lanka.
- **Number of Beds**: Input the number of bedrooms.
- **Number of Baths**: Input the number of bathrooms.
- **House Size**: Input the size of the house in square feet.
- **Land Size**: Input the land size in perches.

The machine learning model estimates the rental price using the above features, providing an accurate and data-driven prediction.

## 🚀 How It Works

### Data Loading and Model Preparation:
-The pre-trained model, stored as best_model.pkl, is loaded using joblib.

### User Input:
- Users enter details about the house they wish to evaluate, including:
- District: Dropdown selection from a list of available districts.
- Number of Beds: The number of bedrooms.
- Number of Baths: The number of bathrooms.
- House Size: Square footage of the house.
- Land Size: Land size in perches.

Prediction:
When the "Predict" button is clicked, the application:
Verifies if all inputs are provided correctly.
Creates a DataFrame with the inputs.
Uses the pre-trained model to predict the monthly rental price based on input details.

Output:
The predicted rental price is displayed on the screen with a success message.

## 🛠️ Technologies Used

The project leverages the following technologies:

Python: The core programming language used for development.
Streamlit: A web application framework to create a user-friendly interface.
pandas: For data manipulation and analysis.
joblib: To save and load machine learning models.
Scikit-Learn: The machine learning library used to train and serialize the rental price prediction model (not directly used in this script but in the model training process).

## 👥 Contributors

This project was developed with the support and collaboration of:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/janakanupehewage">
        <img src="https://github.com/janakanupehewage.png" width="100px;" alt="Janaka NUpehewage"/>
        <br />
        <sub><b>Janaka Nupehewage</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/gihanpramod">
        <img src="https://github.com/gihanpramod.png" width="100px;" alt="Gihan Pramod"/>
        <br />
        <sub><b>Gihan Pramod</b></sub>
  </tr>
</table>
A big thank you to everyone for their hard work and contributions!
