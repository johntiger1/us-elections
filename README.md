# us-elections
![alt-tag](https://github.com/thezane/us-elections/blob/master/forecasts/47days.png)

This is an ensemble model for predicting U.S. presidential elections.  The ensemble consists of three statistical models that performed very well historically: 538, Princeton Election Consortium (PEC) and Votamatic.  Each of those models correctly predicted the winner of at least 49 out of 50 states in 2012.  We briefly review each model and discuss how they are combined into a single prediction. 

###538###

The ![538 Polls-Plus model](http://projects.fivethirtyeight.com/2016-election-forecast/?ex_cid=rrpromo#plus) is designed by statistician and journalist Nate Silver.  It is unique in that it is only member of the ensemble to model third-party performance.  To forecast state vote shares, the model calculates a weighted polling average for each state, which it then combines with demographics and economic data.  Adjustments are made to individual polls based on house effects, methodology and track records of polling firms.  To forecast state and presidential win probabilities on Election Day, the model simulates election outcomes with seperate regional and national error terms.  The error terms decrease the closer the forecast date is to Election Day and the fewer the share of undecided and third-party votes.

###PEC###

Built by neuroscientist and psephologist Sam Wang, ![PEC](http://election.princeton.edu/) is the oldest of the three models and is the only model that is purely poll-based.  Its procedure is as follows.  PEC starts by capturing a snapshot of each state's margin of victory with the median of state polls.  Similarly for a snapshot of national margin victory.  Likely voter polls are favoured over registered voter polls if a pollster releases both.  After estimating state margin of victories, PEC calculates state and presidential win probabilities on Election Day with a random walk starting from the forecast date.

###Votamatic###

![Votamatic](http://votamatic.org/) is the newest of the three models and is the work of political scientist Drew Linzer.  It is a Bayesian forecasting model.  Its priors are a blend of economic factors, incumbent Presidential approval ratings and duration of incumbent White House control.  The model is updated with state polls, whose weight increases the closer the forecast date is to Election Day.  To calculate state vote shares and win probabilities on Election Day, a reverse random walk is performed from Election Day to the forecast date with starting positions and daily rates of change of the walk being estimated via the Markov chain Monte Carlo method.  Unlike other models, Votematic does not forecast national vote shares. 

###How They Are Combined###

The ensemble combines the predictions of the three models by averaging them without favouring any individual model.  There are two reason for this simple averaging.  Firstly, each model has a very different methodology.  Thus, their predictions are not too strongly correlated, which increases the predictive power of the ensemble.  Secondly, each model has a very good but short track record, which prevents us from determining which model performs better and when.  In particular, 538 is only active for two presidential elections, PEC for three and Votamatic for one.  However, as these models and others like them build a track a record, a more sophisticated averaging method may be possible.
