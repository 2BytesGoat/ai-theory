![](media/ml_lingo/introduction.png | 420)
a goat with a beret looking confused during French class (image generated with [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion))

## What is a machine learning model

A machine learning model is a mathematical representation of one or more relationships between data. It is called a model, because it models those relationships as closely as possible, based on the training data and one or more error functions.

It is a model of the relationship between data.

>[!example] 
> **Problem statement**
> Consider you want to rent an apartment and want to find a place which is the best bang for your buck. So you start collecting data, and see that there is a linear correlation between the surface of the appartment and it's price (surface goes up, price goes up).
> 
> **The plan**
> Find a formula which tells you what the price of an appartment should be, given its surface, such that you can filter out the apartments that are inexplicably expensive.
> 
> **The implementation**
> After some investigation, you found out that there are several ways to tackle it:
> * deduce with pen and paper in hand what is the formula based on your examples
> * start learning about decission trees and linear regession
> * employ a machine learning engineer so you can focus on other work
> * stop caring about what apartment is optimal, and choose the one you like

What makes machine learning great, is that rather than deremining the mathematical formula by hand, we feed data to machine learning algorithms that are built to converge towards the right form. 

## What does training a model mean

Training a machine learning model means that we use a algorithm in order to determine what a mathematical formula for solving a given problem. 

Another way to put it is, you know you can train a machine learning model when:
* we have some data
* we know the data is correlated
* the relationship could be described matematically
* we don't know the formula

## What does inference mean

Inference (from the verb **to infer**) means that based on what the model learned, what would it conclude the output should be for a given input.

During this step we already have a matematical formula for the model and we only need to do an inference step (similar to a POST request) to the model with the input data and get a result back. The resources needed during training are serveral times larger than the ones during inference, mostly due to the fact that we don't compute any erors or do updates to the model.

In order to improve a model which is already deployed, most times production data is collected, a new model is trained (either from scratch or fine-tunned) and the production model is replaced with a newer version.

## Optimizations

![img|420x300](https://ars.els-cdn.com/content/image/1-s2.0-S0009261415000366-gr1.jpg)


#localMinimum - 
#globalMinimum - 
#overfit - overfitting can occur when an algorithm learns the training data by heart rather than generalizing. 
#underfit - similar to a person who cannot decide 
#noFreeLunch - 
#bootstraping 