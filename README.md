# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System**! This web app recommends movies based on your favorite movie using content-based filtering. It’s built with **Python**, **Streamlit**, and **scikit-learn**.

---

<img width="1919" height="957" alt="image" src="https://github.com/user-attachments/assets/6791a914-986a-4c0a-a990-95cc4d6d1d07" />


## ✨ Features

- **Smart Movie Recommendations** – Get a list of similar movies based on your favorite.
- **Interactive UI** – Built with **Streamlit**, making it easy to use.
- **Autocomplete Suggestions** – Type any movie name and see dropdown suggestions in real-time.
- **Content-Based Filtering** – Uses genres, keywords, cast, director, and taglines.
- **Responsive Design** – Clean and modern interface with cool hover, shadow, and animation effects.

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Difflib](https://docs.python.org/3/library/difflib.html)
- [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

---

## ⚡ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/ZeDD0405/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
````

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   The app should open automatically at `http://localhost:8501`.

---

## 💡 How It Works

1. Combines movie features (`genres`, `keywords`, `cast`, `director`, `tagline`) into a single string.
2. Converts text data into **TF-IDF feature vectors**.
3. Computes **cosine similarity** between movies.
4. Suggests the top 30 similar movies for any movie you select.

---

## 🚀 Deployment

You can deploy this app easily on:

* [Streamlit Cloud](https://streamlit.io/cloud)
* [Heroku](https://www.heroku.com/)
* Any other cloud service supporting Python apps

---

## 🙌 Credits

Developed and deployed by **Sagar Kallimani**
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/sagarkallimani)

---





