from flask import Flask, render_template, request
from models.ml_detector import MLDetector
from models.gemini_detector import GeminiDetector

app = Flask(__name__)

ml_detector = MLDetector()
gemini_detector = GeminiDetector()
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/authenticity")
def authenticity():
    return render_template("authenticity.html")


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         news_text = request.form['news_text']
#         if not news_text.strip():
#             return render_template('index.html', error="Please enter some news text.")

#         # Get results from both detectors
#         ml_fake, ml_reasoning = ml_detector.detect(news_text)
#         gemini_fake, gemini_reasoning = gemini_detector.detect(news_text)

#         # Overall decision: if either is fake, overall fake
#         overall_fake = ml_fake or gemini_fake
#         overall_result = "Fake News" if overall_fake else "Real News"

#         return render_template('result.html',
#                                news_text=news_text,
#                                overall_result=overall_result,
#                                ml_result="Fake News" if ml_fake else "Real News",
#                                ml_reasoning=ml_reasoning,
#                                gemini_result="Fake News" if gemini_fake else "Real News",
#                                gemini_reasoning=gemini_reasoning)

#     return render_template('index.html')
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        news_text = request.form['news_text']
        if not news_text.strip():
            return render_template('index.html', error="Please enter some news text.")

        # Get results from both detectors
        ml_fake, _ = ml_detector.detect(news_text)
        gemini_fake, gemini_reasoning = gemini_detector.detect(news_text)
        print("ML : ",ml_fake)
        print("Gemini : ",gemini_fake)
        # ✅ New logic: Gemini overrides ML
        if gemini_fake:
            final_result = "Fake News"
        else:
            final_result = "Real News"

        return render_template('result.html',
                               news_text=news_text,
                               final_result=final_result,
                               gemini_reasoning=gemini_reasoning)

    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)




