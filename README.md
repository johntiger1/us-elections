# us-elections
![alt-tag](https://github.com/thezane/us-elections/blob/master/forecasts/49days.png)

This is an ensemble model for predicting U.S. presidential elections.  The ensemble consists of three statistical models that performed very well historically: 538, Princeton Election Consortium (PEC) and Votamatic.  Each of those models correctly predicted the winner of at least 49 out of 50 states in 2012.  We briefly review each model and discuss how they are combined into a single prediction. 

###538###

###PEC###

Designed by neuroscientist and psephologist Sam Wang, PEC is the oldest of the three models and is purely poll-based.  Its procedure is as follows.  PEC starts by capturing a snapshot of each state's margin of victory with the median of state polls.  Similarly for a snapshot of national margin victory.  Likely voter polls are favoured over registered voter polls if a pollster releases both.  After estimating state margin of victories, it calculates state and presidential win probabilities on Election Day with a random walk starting from the forecast date.

###Votamatic###

Votamatic is the newest of the three models and is the work of political scientist Drew Linzer.  It is a Bayesian forecasting model with priors being a blend of economic factors, incumbent Presidential approval ratings and duration of incumbent party control of the White House.  The model is updated with state polls.  Confidence in state polls increases the closer the forecast date is to Election Day.  To calculate state vote shares and win probabilities on Election Day, a reverse random-walk is performed from Election Day to the forecast date.  The starting positions and daily rates of change of the reverse random-walk are estimated via the Markov chain Monte Carlo method.  Unlike the other models, Votematic does not forecast national vote shares. 

###How They Are Combined###
