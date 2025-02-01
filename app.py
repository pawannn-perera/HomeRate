# import streamlit as st
# import pandas as pd
# import joblib

# # Load the model
# try:
#     model = joblib.load('best_model.pkl')
# except FileNotFoundError:
#     st.error("The model file 'best_model.pkl' is missing.")
#     st.stop()
# except Exception as e:
#     st.error(f"Error loading the model: {e}")
#     st.stop()

# # Load known districts from the dataset
# file_path = 'Monthly_house_rental_prices_in_Sri_Lanka.csv'
# try:
#     df = pd.read_csv(file_path)
#     known_districts = df['District'].unique().tolist()
# except FileNotFoundError:
#     st.error(f"The dataset file '{file_path}' is missing.")
#     st.stop()
# except Exception as e:
#     st.error(f"Error loading the dataset: {e}")
#     st.stop()

# # App title
# st.markdown(
#     """
#     <div style='text-align: center;'>
#     <h1>House Rental Price Prediction <br> in Sri Lanka</h1>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Sidebar
# st.sidebar.title("Menu")
# app_mode = st.sidebar.selectbox("Choose the app mode", ["Home", "About"])

# if app_mode == "About":
#     st.subheader("About this App")
#     st.write("""
#     This application predicts the monthly rental prices of houses in various districts in Sri Lanka.
#     It uses a machine learning model trained on historical rental data to estimate prices based on
#     factors like the number of baths, number of beds, land size, house size, and district.
#     """)
# else:
#     # Main page
#     st.subheader("Enter House Details for Price Prediction")

#     # Inputs for the user
#     district = st.selectbox("Select a District", ["Choose here"] + sorted(known_districts))
#     beds = st.number_input("Number of Beds", min_value=1, max_value=10, value=None)
#     baths = st.number_input("Number of Baths", min_value=1, max_value=10, value=None)
#     house_size = st.number_input("House Size (Square Feet)", min_value=100.0, value=None)
#     land_size = st.number_input("Land Size (Perches)", min_value=1.0, value=None)

#     if st.button("Predict"):
#         if district == "Choose here":
#             st.warning("Please select a valid district before proceeding.")
#         elif None in [beds, baths, house_size, land_size]:
#             st.warning("Please fill out all fields before making a prediction.")
#         else:
#             try:
#                 # Normalize the district name
#                 normalized_district = district.title()

#                 # Create a DataFrame for the new input
#                 new_data = pd.DataFrame([[baths, beds, land_size, house_size, normalized_district]],
#                                         columns=['Baths', 'Beds', 'Land size', 'House size', 'District'])

#                 # Make the prediction
#                 predicted_price = model.predict(new_data)

#                 # Display the result
#                 st.success(f"The predicted monthly rental price is Rs: {predicted_price[0]:,.2f}")
#             except Exception as e:
#                 st.error(f"Prediction error: {e}")

# # Footer
# st.sidebar.markdown("""
# *Developed by:*
# - Gihan Pramod
# - Janaka Nupehewage
# - Kavishka Jayasinghe
# - Pawan Perera
# - Pasindu Malshan
# """)

# # Sidebar image
# st.sidebar.image("logo.jpg", use_container_width=True)

import streamlit as st
import pandas as pd
import joblib
from PIL import Image  # For handling images

# Load the model
try:
    model = joblib.load('best_model.pkl')
except FileNotFoundError:
    st.error("The model file 'best_model.pkl' is missing.")
    st.stop()
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

# Load known districts from the dataset
file_path = 'Monthly_house_rental_prices_in_Sri_Lanka.csv'
try:
    df = pd.read_csv(file_path)
    known_districts = df['District'].unique().tolist()
except FileNotFoundError:
    st.error(f"The dataset file '{file_path}' is missing.")
    st.stop()
except Exception as e:
    st.error(f"Error loading the dataset: {e}")
    st.stop()

# App title
st.markdown(
    """
    <div style='text-align: center;'>
    <h1>🏠 House Rental Price Prediction <br> in Sri Lanka 🇱🇰</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Menu")
app_mode = st.sidebar.selectbox("Choose the app mode", ["Home", "About"])

# Sidebar image
st.sidebar.image("logo.jpg", use_column_width=True)

# About Page
if app_mode == "About":
    st.subheader("About this App")
    st.write("""
    This application predicts the monthly rental prices of houses in various districts in Sri Lanka.
    It uses a machine learning model trained on historical rental data to estimate prices based on
    factors like the number of baths, number of beds, land size, house size, and district.
    """)
    st.markdown("### Dataset")
    st.write("The dataset used for this app contains historical rental prices across Sri Lanka.")
    st.write("You can download the dataset below:")
    st.download_button(
        label="Download Dataset",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='Monthly_house_rental_prices_in_Sri_Lanka.csv',
        mime='text/csv'
    )
else:
    # Main page
    st.subheader("Enter House Details for Price Prediction")

    # Welcome message
    st.markdown("""
    Welcome to the House Rental Price Prediction app! 🎉  
    Please fill out the details below to get a price prediction.
    """)

    # Organize inputs into columns
    col1, col2 = st.columns(2)

    with col1:
        district = st.selectbox("Select a District", ["Choose here"] + sorted(known_districts))
        beds = st.number_input("Number of Beds 🛏️", min_value=1, max_value=10, value=None)
        baths = st.number_input("Number of Baths 🚿", min_value=1, max_value=10, value=None)

    with col2:
        house_size = st.number_input("House Size (Square Feet) 📏", min_value=100.0, value=None)
        land_size = st.number_input("Land Size (Perches) 🌳", min_value=1.0, value=None)

    if st.button("Predict Price 🚀"):
        if district == "Choose here":
            st.warning("⚠️ Please select a valid district before proceeding.")
        elif None in [beds, baths, house_size, land_size]:
            st.warning("⚠️ Please fill out all fields before making a prediction.")
        else:
            try:
                # Normalize the district name
                normalized_district = district.title()

                # Create a DataFrame for the new input
                new_data = pd.DataFrame([[baths, beds, land_size, house_size, normalized_district]],
                                        columns=['Baths', 'Beds', 'Land size', 'House size', 'District'])

                # Show a spinner while making the prediction
                with st.spinner("Predicting..."):
                    predicted_price = model.predict(new_data)

                # Display the result with a success message
                st.success(f"✅ The predicted monthly rental price is **Rs: {predicted_price[0]:,.2f}**")
            except Exception as e:
                st.error(f"❌ Prediction error: {e}")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### Developed by:")
st.sidebar.markdown("""
- Gihan Pramods
- Janaka Nupehewage
- Kavishka Jayasinghe
- Pawan Perera
- Pasindu Malshan
""")
st.sidebar.markdown("---")
st.sidebar.markdown("### Contact Us")
st.sidebar.markdown("📧 Email: example@example.com")
st.sidebar.markdown("🌐 Website: [example.com](https://example.com)")
st.sidebar.markdown("📱 Social Media: [Twitter](https://twitter.com) | [LinkedIn](https://linkedin.com)")