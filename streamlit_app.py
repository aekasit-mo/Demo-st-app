import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.subheader('Input')
url_input = st.text_input('GitHub URL', '')

if url_input:
    st.subheader('Output')
    st.info(f'The GitHub URL of your data is: {url_input}')
    df = pd.read_csv(url_input)
    st.write(df)

    column_name = df.columns
    df2 = df.groupby(column_name[-1]).mean()
    st.write(df2)
    st.bar_chart(df2)

else:
    st.header('Enter your input')
    st.error('Awaiting your input!')

# species = df.columns[column_name[-1]]
# st.write(species)

genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")