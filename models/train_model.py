from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Počáteční tréninková data
training_data = [
    ("otevři prohlížeč", "open_browser"),
    ("nová karta", "open_browser"),
    ("otevři novou kartu", "open_browser"),
    ("zvětši okno", "maximize_window"),
    ("větší okno", "maximize_window"),
    ("zvětšit okno", "maximize_window"),
    ("zmenši okno", "minimize_window"),
    ("minimalizovat okno", "minimize_window"),
    ("menši okno", "minimize_window"),
    ("zmenšit okno", "minimize_window"),
    ("zavři okno", "close_window"),
    ("vytvoř nový projekt databáze", "create_new_project"),
    ("vytvoř nový projekt web", "create_new_project"),
    ("nastavení", "settings"),
    ("otevřít nastavení", "settings"),
    ("Jdi do nastavení", "settings"),
    ("potřebují do nastavení", "settings")
]


# Příprava tréninkových dat
X_train, y_train = zip(*training_data)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Trénování modelu
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Uložení modelu
with open('models/model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)
