# us-elections
![alt-tag](https://github.com/thezane/us-elections/blob/master/forecasts/49days.png)

This is an ensemble model for predicting U.S. presidential elections.  The ensemble consists of three statistical models that performed very well historically: 538, Princeton Election Consortium (PEC) and Votamatic.  Each of those models correctly predicted the winner of at least 49 out of 50 states in 2012.  We briefly review each model and discuss how they are combined into a single prediction. 

###538###

###PEC###

Designed by neuroscientist and psephologist Sam Wang, the PEC model is the oldest of the three and is purely poll-based.  It starts by capturing a snapshot of state vote shares with the median of state polls.  Similarly for a snapshot of national vote shares.  Likely voter polls are favoured over registered voter polls if a pollster releases both.  After calculating state vote shares, it estimates state win probabilities and the chance of winning the presidency on Election Day with a random walk.

###Votamatic###

###How They Are Combined###
