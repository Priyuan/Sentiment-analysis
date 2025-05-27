import streamlit as st
import pandas as pd

df = pd.read_csv('dataset.csv', encoding='latin1')
df = df.dropna(subset=['track_name', 'artists', 'track_genre', 'popularity', 'danceability', 'energy', 'tempo'])

def music_chatbot(user_input, df):
    user_input = user_input.lower()
    genres = df['track_genre'].unique()
    matched_genres = [str(g) for g in genres if g and str(g).lower() in user_input]
    artists = df['artists'].unique()
    matched_artists = [str(a) for a in artists if a and str(a).lower() in user_input]
    mood_map = {
        'energetic': ('energy', 0.7),
        'danceable': ('danceability', 0.7),
        'popular': ('popularity', 70),
        'slow': ('tempo', 80),
        'fast': ('tempo', 120),
    }
    filters = []
    for mood, (feature, threshold) in mood_map.items():
        if mood in user_input:
            if feature == 'tempo':
                if mood == 'slow':
                    filters.append(df['tempo'] < threshold)
                else:
                    filters.append(df['tempo'] > threshold)
            else:
                filters.append(df[feature] > threshold)
    filtered_df = df
    if matched_genres:
        filtered_df = filtered_df[filtered_df['track_genre'].str.lower().isin([g.lower() for g in matched_genres])]
    if matched_artists:
        filtered_df = filtered_df[filtered_df['artists'].str.lower().isin([a.lower() for a in matched_artists])]
    if filters:
        for f in filters:
            filtered_df = filtered_df[f]
    if filtered_df.empty:
        filtered_df = df.sort_values(by='popularity', ascending=False).head(5)
    else:
        filtered_df = filtered_df.sort_values(by='popularity', ascending=False).head(5)
    recs = []
    for _, row in filtered_df.iterrows():
        recs.append(f"🎵 {row['track_name']} by {row['artists']} — Genre: {row['track_genre']} (Popularity: {row['popularity']})")
    return recs

st.title("🎧 Music Recommendation Chatbot")
user_input = st.text_input("Type something like 'energetic songs' or 'slow pop music'")

if user_input:
    recommendations = music_chatbot(user_input, df)
    st.write("### Recommendations:")
    for r in recommendations:
        st.write(r)
