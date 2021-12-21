![(python_version)](https://img.shields.io/badge/Python-3.8-green) ![  ](https://img.shields.io/badge/pymongo-4.0.1-yellow)![snscrape](https://img.shields.io/badge/snscrape-0.4.0-red) ![pytorch](https://img.shields.io/badge/pytorch-1.10-blue) ![](https://img.shields.io/badge/pandas-3.1.0-orange)

# Tweets sentiment analysis for extracting opinion on LGBT

This project aims to investigate some statistics of tweets with the search word of "LGBT", and then perform sentiment analysis to differentiate between pride month sentiments compared to other times. 

To execute the program make sure to load LGBT_sentiments_from_tweets.ipynb, that is the script for the whole flow (Make sure to install the needed requirements for execution), which includes all of the outputs of the execution. 

The sentiment analysis is done using roberta (hugging faces).

Data is stored as no-sql mongoDB (docker) is manipulated both via the collection and pandas. 

Citing sentiment analyzer:
>@inproceedings{rosenthal2017semeval,
> title={SemEval-2017 task 4: Sentiment analysis in Twitter},
>author={Rosenthal, Sara and Farra, Noura and Nakov, Preslav},
>booktitle={Proceedings of the 11th international workshop on semantic evaluation (SemEval-2017)},
>pages={502--518},
>year={2017},
>}

Citing hate speech detection:
>@inproceedings{basile-etal-2019-semeval,
>title = \"SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter
>author = \"Basile, Valerio  and Bosco, Cristina  and Fersini, Elisabetta  and Nozza, Debora and Patti, Viviana and
>Rangel Pardo, Francisco Manuel  and Rosso, Paolo  and Sanguinetti, Manuela
>booktitle = \"Proceedings of the 13th International Workshop on Semantic Evaluation
>year = \"2019\",\n",
>address = \"Minneapolis, Minnesota, USA,
>publisher = \"Association for Computational Linguistics\,
>url = \"https://www.aclweb.org/anthology/S19-2007\,
>doi = \"10.18653/v1/S19-2007\,
>pages = \"54--63\
>}

