===================
awesome_recommender : http://ericawesome.pythonanywhere.com/
===================

**Demo of a movie recommendation system using the collaborative filtering (in particular calculating cosine similarity).**


.. image:: https://travis-ci.org/ericawesome/awesome_recommender.svg?branch=master
        :target: https://travis-ci.org/ericawesome/recommender_app


* Free software: MIT license
* Documentation: https://recommender-app.readthedocs.io.


Features
--------


* The **machine learning model** was deployed with **flask**.
* The **cosine similarity** is used to identify the most similar user with the most similar taste.
* Therefore, the movie recommender uses ratings from **610 users** of a total of nearly **20,000 movies**.
* In order to have access to the data at any time, I provided a **SQLite database** in the repository. 
* With the input from the user the movie recommender 
1) first detects the user with the most similar taste by calculating the similarity between each user and 
2) returns 5 movies that the most similar user rated with 5 stars.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
