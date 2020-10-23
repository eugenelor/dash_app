# dash_app
A learning experiment with Dash by plotly. This project contains multiple dash .py scripts, from simple graphs to a real time sensor data dashboard, which is deployed in [Heroku](https://demoapp-gene.herokuapp.com/) 

# How to use project
This code was orginally ran on a `Ubuntu 18.04` machine, in a `Python 3` virtual environment `venv`. This github project does not contain the enviroment setup, so please follow instructions for your machine to create a `venv` virtual environment based on your Operating System. 

```
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
```

All packages used in this project are in `requirements.txt`. An automated install can be done by running the code below in `Ubuntu`:

```
pip install -r requirements.txt
```

# Materials and Resources

## Dash Overview
1. [Dash Site](https://plotly.com/dash/)
2. [Dash Gallery](https://dash-gallery.plotly.host/Portal/)

## Venv setup
1. [Windows](https://www.youtube.com/watch?v=APOPm01BVrk)
2. [Ubuntu/Mac](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)

## Dash Resources
1. [Introduction to Dash](https://www.youtube.com/watch?v=hSPmj7mK6ng&t=1347s)
2. [Great Channel on all things Dash](https://www.youtube.com/channel/UCqBFsuAz41sqWcFjZkqmJqQ/playlists)
3. [Dash Introduction](https://dash.plotly.com/introduction)
4. [Dash Components](https://dash.plotly.com/dash-core-components)

## Deployment to Heroku
1. [Step by Step tutorial](https://www.youtube.com/watch?v=b-M2KQ6_bM4)

# Script descriptions
This project contains a few .py scripts that all run a seperate Dash dashboard. Descrbied below:
1. `dash_sentdex_1.py` is made to illustrate the power of Dash to support Inputs
2. `dash_sentdex_3.py` is a dashboard that plots Stock market tickers from 2017 to present day based on user. It updates in real time.
3. `dash_sentdex_5.py` is made to realise real time capabilities of Dash, the script generates random values in lieu for illustration purposes.
4. `dash_logger.py` is the app that is illustrates the responsiveness of Dash, enabling the design of interactive dashboards that respond to user input in real time.
