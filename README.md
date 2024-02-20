# Gem Prediction

Learning how to use FastApi with Jira2 templates, AlpineJS, HTMX and poetry.
In this project I'll be comparing multiple regression models to predict the prices of a Zirconia gem based on its attributes.

Data obtained from [Kaggle](https://www.kaggle.com/datasets/colearninglounge/gemstone-price-prediction/data).

## Insights & Observations

Now that the main functionality is finished, I wanted to talk about opinions that I have, things that I learned, problems that I faced and how I solved them.

> Insights & Observations of the ML models, training and data cleaning are at the _Conclusions_ & _Insights_ sections of the `notebooks/gem_ML.ipynb` file.

- I really like fastApi, I've had experience with Go, Phoenix(Elixir), Laravel (PHP) & Django (Python) and I like how lightweight & simple it feels. It's really similar to Go which I really like. It's fast to work with and its fast to test stuff. However, I do prefer using Go, it feels simpler and, imo, more intuitive.

- I had one problem with the POST request in the form, the information wasn't being received by the `prediction` method. There were no errors when the information was sent with a GET request so I thought the problem was with HTMX or AlpineJS but after reading the [fastApi documentation](https://fastapi.tiangolo.com/tutorial/request-forms/) I found that I need to import `Form` from `fastapi`. After that it was smooth sailing.

- I really like HTMX and AlpineJS, specially together. I'm not a big Front-end fan (although I do work with Front-end **_A LOT_**) but HTMX and Alpine has make the Front-end experience really enjoyable. It feels nice and intuitive, I also feel that it's fast to work with. I really like working with html and having all in one file makes development faster and the best part is that it is still really easy to read.

- I'm thinking of using Tailwind for styling, but we'll see.

## Future Work

There are still more stuff I want to do with this project.

- Styling, I haven't touched CSS at all and it looks horrible. I'm thinking of using Tailwind atm.

- More data cleaning.

- Planning on implementing more regression methods.
