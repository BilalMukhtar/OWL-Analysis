# OWL Analysis/Playoff Profit

## Overview
Using stats from The Overwatch League Stats Lab, I attempted to create a generalized statistic that can be used to show how well a player performed in a given map on a specific hero.

## Process
* The data was cleaned and combined into a simplified format that was easier to do predictions with
* Using random forest, I attempted to figure out how well a model could predict the likelihood of a win with all statistics given
* The statistic was created using a variety of techniques to fine tune the ability to predict a map win
* Finally, the statistic was ready to be used for a variety of different graphics to see the true impact of players on their team's success

## Files
### Notebooks
* [`OWL_part1.ipynb`](https://github.com/BilalMukhtar/OWL-Analysis/blob/main/OWL_part1.ipynb) ([nbviewer version](https://nbviewer.org/github/BilalMukhtar/OWL-Analysis/blob/main/OWL_part1.ipynb)): Cleaning of data and utilizing all stats to predict team success
* [`OWL_part2.ipynb`](https://github.com/BilalMukhtar/OWL-Analysis/blob/main/OWL_part2.ipynb) ([nbviewer version](https://nbviewer.org/github/BilalMukhtar/OWL-Analysis/blob/main/OWL_part2.ipynb)): Creating statistic and fine tuning with testing for best results
* [`OWL_part3.ipynb`](https://github.com/BilalMukhtar/OWL-Analysis/blob/main/OWL_part3.ipynb) ([nbviewer version](https://nbviewer.org/github/BilalMukhtar/OWL-Analysis/blob/main/OWL_part3.ipynb)): Utilizing statistic for vizualization

### Folders
* old csv files: raw data sourced from The Overwatch League Stats Lab
* new csv files: csvs used for storing data between notebooks


## Part 1: Cleaning and initial statistic
Below are images for the correlation matrix and feature importance graphs that could not render in nbviewer
<br></br>
[![f](https://github.com/BilalMukhtar/OWL-Analysis/blob/main/graphics/corr_matrix.svg)]

## Data Source
* [The Overwatch League Stats Lab](https://overwatchleague.com/en-us/statslab)
