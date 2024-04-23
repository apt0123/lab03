import streamlit as st
import os

# SP Travel

def recipe(name, serving_size=1):
    st.title(name) #1st New Stremalit Methods
    st.write ("Plan your Spain visit")
    image_filename = os.path.join("imagesP2/"+name.lower() + ".jpg") #Will Include 3 Images

    st.image(image_filename, use_column_width=True)
    st.header("Train Rides")
    st.subheader("stimated cost p/ person [tourist]")

    if name == "Madrid":
        pasta_quantity = 12 * serving_size
        tomato_sauce_quantity = round(1.8 * pasta_quantity, 2)
        st.write("Main train station(s): Atocha | Chamartín")
        st.write(f"-Starting at {pasta_quantity} euros. in low season")
        st.write(f"-Starting at {tomato_sauce_quantity} euros. in high season")


    elif name == "Barcelona":
        p_quantity = 16 * serving_size
        t_quantity = round(2.1* p_quantity, 2) #Round the number and get the new value
        st.write("Main train station(s): Sants | Francia")
        st.write(f"-Starting at {p_quantity} euros. in low season")
        st.write(f"-Starting at {t_quantity} euros. in high season")


    elif name == "Toledo":
        l_quantity = 7 * serving_size
        to_quantity = round(1.3 * l_quantity, 2)
        st.write("Main train station(s): Toledo")
        st.write(f"- Starting at {l_quantity} euros. in low season")
        st.write(f"- Starting at {to_quantity} euros. in high season")


    st.header("Must see places!")

    if name == "Madrid":
        st.write("1. Museo del Prado")
        st.write("2. Estanque del Retiro")
        st.write("3. Catedral Santa María de la Almudena")
        st.write("4. Palacio Real de Madrid")
        st.write("5. Hotel Riu - rooftop at nighttime")

    elif name == "Barcelona":
        st.write("1. Catedral de la Sagrada Familia")
        st.write("2. Parc Guell")
        st.write("3. Las Ramblas del Poble Nou")
        st.write("4. Barrio Gótico")
        st.write("5. Gran Vía")

    elif name == "Toledo":
        st.write("1. Catedral de Toledo")
        st.write("2. Alcázar de Toledo")
        st.write("3. Iglesia de Santo Tomé")
        st.write("4. Fly Toledo - zip line over the river")
        st.write("5. Eat mazapán from Snato Tomé")

# the sidebar
st.sidebar.title("Spain travels")
recipe_choice = st.sidebar.radio("Select a Destination", ["Madrid", "Barcelona", "Toledo"])#2nd New Streamlit Method

# how many people
serving_size = st.sidebar.number_input("How many people are traveling?", min_value=1, value=1)#3rd New Streamlit Method

# display!
if recipe_choice == "Madrid":
    recipe("Madrid", serving_size)
elif recipe_choice == "Barcelona":
    recipe("Barcelona", serving_size)
elif recipe_choice == "Toledo":
    recipe("Toledo", serving_size)
