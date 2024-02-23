# Gem Prediction

Learning how to use FastApi(with Jira2 templates), AlpineJS, HTMX, TailwindCSS and Poetry.
In this project I'll be comparing multiple regression models to predict the prices of a Zirconia gem based on its attributes.

Data obtained from [Kaggle](https://www.kaggle.com/datasets/colearninglounge/gemstone-price-prediction/data).

## Insights & Observations

Now that the main functionality is finished, I wanted to talk about opinions that I have, things that I learned, problems that I faced and how I solved them.

> Insights & Observations of the ML models, training and data cleaning are at the _Conclusions_ & _Insights_ sections of the `notebooks/gem_ML.ipynb` file.

- I really like fastApi, I've had experience with Go, Phoenix(Elixir), Laravel (PHP) & Django (Python) and I like how lightweight & simple it feels. It's really similar to Go which I really like. It's fast to work with and its fast to test stuff. However, I do prefer using Go, it feels simpler and, imo, more intuitive.

- I had one problem with the POST request in the form, the information wasn't being received by the `prediction` method. There were no errors when the information was sent with a GET request so I thought the problem was with HTMX or AlpineJS but after reading the [fastApi documentation](https://fastapi.tiangolo.com/tutorial/request-forms/) I found that I need to import `Form` from `fastapi`. After that it was smooth sailing.

- I really like HTMX and AlpineJS, specially together. I'm not a big Front-end fan (although I do work with Front-end **_A LOT_**) but HTMX and Alpine has make the Front-end experience really enjoyable. It feels nice and intuitive, I also feel that it's fast to work with. I really like working with html and having all in one file makes development faster and the best part is that it is still really easy to read.

- I used TailwindCSS for the styling, and it was a nice experience. It was surprisingly fast to use, specially considering the amount of classes used. I think the fact that it was written directly in the HTML helped. There have been times when I have used the `style` attribute in HTML because it was faster, however, writing all the normal CSS syntax is long and tedious compared to using Tailwind. 

- I tend to use SCSS a lot but Tailwind actually feels better, and I'll use it more for sure.

## Conclusion
- Of course this is not a full on project, it isn't a completely functional application and I have not used this stack in production, so I cannot say for certain that this stack is amazing. However, at least for prototyping, it feels really fast, and I do love how simple it feels to use these technologies. Using AlpineJS, HTMX & TailwindCSS with any
framework that uses templates, like Templ, Django, FastApi, etc., feels amazing, and I'll try to incorporate it in my work (if possible).