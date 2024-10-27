from flask import Flask, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import json

application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works! V1.0"

@application.route("/pred")
def load_model():
        loaded_model = None
        with open('./basic_classifier.pkl', 'rb') as fid:
            loaded_model = pickle.load(fid)
        
        vectorizer = None
        with open('./count_vectorizer.pkl', 'rb') as vd:
            vectorizer = pickle.load(vd)

        sentence = request.args.get('sentence')
        print(f"sentence (from url query parameter) is '{sentence}'.")

        # use model to predict
        prediction = loaded_model.predict(vectorizer.transform([sentence]))[0]
        print("prediction is -", loaded_model.predict(vectorizer.transform(['This is true news'])) )
        # return "prediction is: " + prediction
        return str(int(prediction == "REAL"))

if __name__ == "__main__":
    application.run(port=5000, debug=True)
