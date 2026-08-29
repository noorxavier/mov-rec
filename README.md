# 🎬 Movie Recommender System

A **Content-Based Movie Recommendation System** built with Python and Streamlit that recommends movies similar to a user's selected movie using precomputed similarity scores. Movie posters are dynamically fetched from the **TMDB API**.

---

## 📌 Overview

The Movie Recommender System provides movie recommendations based on the similarity between movies.

Users can select a movie from the available collection and receive the **top 5 similar movies**, along with their posters.

The recommendation engine uses a precomputed similarity matrix, while the application is built with Streamlit to provide an interactive web interface.

---

## ✨ Features

* 🎥 Select a movie from the available movie collection
* 🤖 Content-based movie recommendations
* ⭐ Returns the **top 5 similar movies**
* 🖼️ Dynamically fetches movie posters using the TMDB API
* ⚡ Uses a precomputed similarity matrix for fast recommendations
* 🌐 Interactive Streamlit web interface
* 🚀 Deployment-ready configuration

---

## 🧠 How It Works

The recommendation pipeline works as follows:

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Feature Extraction
      ↓
Content-Based Similarity
      ↓
Similarity Matrix
      ↓
User Selects a Movie
      ↓
Find Similar Movies
      ↓
Top 5 Recommendations
      ↓
Fetch Movie Posters from TMDB
```

### Recommendation Process

1. The user selects a movie from the Streamlit dropdown.
2. The application identifies the selected movie in the dataset.
3. The corresponding row from the precomputed similarity matrix is retrieved.
4. Movies are ranked according to their similarity scores.
5. The top 5 similar movies are selected.
6. Movie posters are fetched using the movie's TMDB ID.
7. The recommendations are displayed in the Streamlit interface.

---

## 🛠️ Tech Stack

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| **Python**     | Core programming language |
| **Pandas**     | Data manipulation         |
| **NumPy**      | Numerical operations      |
| **Streamlit**  | Web application and UI    |
| **Requests**   | API requests              |
| **Pickle**     | Model/data serialization  |
| **TMDB API**   | Movie poster information  |
| **Git/GitHub** | Version control           |

---

## 📂 Project Structure

```text
mov-rec/
│
├── app.py              # Streamlit application
├── movies.pkl          # Movie dataset
├── similarity.pkl      # Precomputed similarity matrix
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment configuration
├── setup.sh            # Setup script
└── README.md           # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/noorxavier/mov-rec.git
cd mov-rec
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🖥️ Application

The application provides a simple interface where users can:

1. Select a movie.
2. Click the **Recommend** button.
3. View five recommended movies with their posters.

---

## 🔌 TMDB API

The application uses the **TMDB API** to retrieve movie poster information using each movie's TMDB ID.

The poster URL is generated dynamically from the movie information returned by the API.

> **Note:** If you fork or recreate this project, use your own TMDB API credentials and store them securely using environment variables rather than hardcoding them.

---

## 📊 Recommendation Logic

The recommendation function retrieves the similarity scores associated with the selected movie and ranks the movies according to those scores.

The highest-scoring movies, excluding the selected movie itself, are returned as recommendations.

```python
movies_list = sorted(
    list(enumerate(distance)),
    reverse=True,
    key=lambda x: x[1]
)[1:6]
```

This produces the **top 5 recommendations** based on similarity.

---

## 🔮 Future Improvements

* Add movie search functionality
* Display movie ratings and genres
* Add movie descriptions and release dates
* Improve recommendation quality using additional metadata
* Add user-based personalization
* Implement a more secure API-key management system
* Add recommendation explanations
* Improve UI/UX with movie cards and responsive layouts

---

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

* Content-based recommendation systems
* Similarity-based ranking
* Data preprocessing
* Python data handling
* Streamlit application development
* REST API integration
* Model/data serialization using Pickle
* Deployment configuration
* Building an end-to-end machine learning application

---

## 👨‍💻 Author

**Noor Xavier**

GitHub:
https://github.com/noorxavier

---

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub.
