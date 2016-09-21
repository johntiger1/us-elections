# us-elections
![alt-tag](https://github.com/thezane/us-elections/blob/master/forecasts/49days.png)

This is an ensemble model for predicting U.S. presidential elections.  The ensemble consists of three statistical models that performed very well historically: 538, Princeton Election Consortium (PEC) and Votamatic.  Each of those models correctly predicted the winner of at least 49 out of 50 states in 2012.  We briefly review each model and discuss how they are combined into a single prediction. 

###538###

###PEC###

Designed by neuroscientist and psephologist Sam Wang, the PEC model is the oldest of the three and is purely poll-based.  To capture a snapshot of state vote shares, it uses state polls.  Similarly for a snapshot of national vote shares.  To capture state win probabilities, PEC applies the t-distribution on a median of state polls with an estimated standard error of the median.

Unlike other models, PEC only forecasts the chance of party winning a state if the election is held today.  The exception is the chance of winning the presidency, which it does by calculating a snapshot for the expected electoral votes and adding an error term that decreases as Election Day nears.

###Votamatic###

###How They Are Combined###
