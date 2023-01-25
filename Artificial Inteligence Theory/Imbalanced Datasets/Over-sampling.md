> Tags: #Overfit 

# Downsides
When duplicating samples from the minority classes, the ML algorithm will tend to "learn" them by heart in order to achieve a low error rate, thus leading to overfit.

# Methods

![img|420x420](https://imbalanced-learn.org/stable/_images/sphx_glr_plot_comparison_over_sampling_004.png)
> Image taken from: [imbalanced-learn.org](https://imbalanced-learn.org/stable/auto_examples/over-sampling/plot_comparison_over_sampling.html#sphx-glr-auto-examples-over-sampling-plot-comparison-over-sampling-py)

## 1. Naive random over-sampling 
Randomly sample with replacement (duplicate) elements from the minor class (the classes with lesser samples) until all classes have the same number of elements.

## 2. SMOTE - Synthetic Minority Oversampling Technique
SMOTE creates a "synthetic" sample based two randomly selected samples of the minority class.
![image|420x210](media/imbalanced_datasets/smote.webp)
> Image taken from: [rikunert.com](https://rikunert.com/smote_explained)

## 3. ADASYN - Adaptive Synthetic
ADASYN creates a "synthetic" sample based on two randomly selected samples of the minority class while **retaining the sample distribution**.

## 4. SMOTENC
SMOTENC is a variant of SMOTE which supports categorical features for samples.

# References
1. **Synthetic Minority Oversampling Technique (SMOTE)**  - [paper](https://arxiv.org/abs/1106.1813) - [sklearn](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)
2. **Adaptive Synthetic (ADASYN)** - [paper](https://sci2s.ugr.es/keel/pdf/algorithm/congreso/2008-He-ieee.pdf) - [sklearn](https://imbalanced-learn.org/dev/references/generated/imblearn.over_sampling.ADASYN.html)
3. **SMOTE vs ADASYN** - [paper](https://www.diva-portal.org/smash/get/diva2:1519153/FULLTEXT01.pdf)

