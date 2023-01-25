>Tags:  #LocalMinimum, #Metrics, #Overfit

Statistic algorithms (and also the human brain) flourish when the data they are exposed to is unbiased and of high quality. If the data is balanced, it is easier to estimate how far an algorithm is from the truth, and it makes it easier for the algorithm to generalize and identify correlations between input and target data.

**When we have a bias...**
> *Consider that, from the day you are born, the only dog you ever saw or read about was a Puddle. Then one day, a friend asks you to guess how his new dog (a German Sheppard) looks like, and you start describing him as a puddle.*

**... or an incomplete picture of the problem ...**
>*Different people can look at the same thing from different angles, and still not be able to get to the global minimum, the same as in [The blind men and the elephant](https://en.wikipedia.org/wiki/Blind_men_and_an_elephant#:~:text=The%20parable%20of%20the%20blind,the%20side%20or%20the%20tusk.).*

**... we can't achieve our potential.**

![img|420x420](media/imbalanced_datasets/introduction.jpeg)

Edgy examples aside, for most real world problems it is challenging (costly and time-consuming) to gather an equal number of samples for all scenarios (think detecting Frauds or Rare Diseases). 

However, in order to bypass this limitation, we can imply one of several balancing methods such as:
* **[[Over-sampling|Over-sampling]]** - copying or generating more samples for minor classes
	* *downsides: may cause overfitting*
* **[[Under-sampling|Under-sampling]]** - removing data from major classes
	* downsides: may push algorithm towards a local minimum
* **[[Combined-sampling|Combined-sampling]]** - trying to get the best of both worlds

# Remarks

## * Accuracy is not a representative metric
Accuracy is not a good metric for datasets with skewed classes. For example, when classifying whether someone is suffering from a rare diesese or not, only predicting `negative` will produce a over 90% accuracy.

## * Precission, recall and F1 are good metrics

