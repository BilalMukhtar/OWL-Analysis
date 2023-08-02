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
* OWL_part1: Cleaning of data and utilizing all stats to predict team success
* OWL_part2: Creating statistic and fine tuning with testing for best results
* OWL_part3: Utilizing statistic for vizualization

### Folders
* old csv files: raw data sourced from The Overwatch League Stats Lab
* new csv files: csvs used for storing data between notebooks

## Part 1: Cleaning and initial analysis
Based on the following diagram, the goal is to expand the project to also contain data from teams which may improve the current predictions along with allowing for future projects/analysis (Click on the image for an interactive view)
<br></br>
[![alttext](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/imgs/soccer_db_png.png)](https://drawsql.app/teams/bilals-team-1/diagrams/soccerdb/embed)


## Data Sources
* futbin.com (FIFA Data)
* understat.com (Player Data)
