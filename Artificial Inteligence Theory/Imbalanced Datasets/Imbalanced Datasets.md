
# Introduction

Statistic algorithms (and also the human brain) have an easier time determining patterns and rules when the data they are exposed to is unbiased and of high quality. 

Let's say we were to build an algorithm which tells you whether in an image there's a dog or a cat. We may consider that **your data is balanced if you have the same number of samples for all classes**. That means we have the same number of images with dogs as images of cats. 

If we had an imbalanced dataset, let's say 10 images with dogs and 1000 images with cats, it would be easier for the algorithm to classify that whatever image we give it as cat, rather than it figuring out the differences.

>[!example]
>Consider, you and your friend are playing a game of coin tossing. After a few tosses, you are amazed to see that 7 out of 8 tosses, the coin lands on heads. 
> 
> Seeing this, what face of the coin would you bet on next time?

![](media/imbalanced_datasets/introduction.jpeg | 420)
> *When we have a bias or an incomplete picture of the problem, we can't achieve our true potential.* - **Philosopher Goat** (image generated with [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion))

# Balancing Methods

For most real world problems, it's challenging (costly and time-consuming) to gather an equal number of samples from all scenarios (think of problems like Detecting Frauds or Rare Diseases). 

> [!warning]
> If the dataset is changed (more data is collected, from the same or different data source) the balancing method should be reevaluated.

However, there are several methods that we can imply in order to make the best out of our data:
* **[[1. Oversampling]]** - ways of copying or generating more samples for minor classes
* **[[2. Undersampling]]** - ways of removing data from major classes
* **[[3. Combined Sampling]]** - ways of combining both over- and under-sampling
* **[[4. Inner Balancing Samplers]]** - training robust [[decission trees]] by using #bootstraping

As a general rule of thumb, we may want to experiment with one of each approach in order to determine what is best for our algorithm.
