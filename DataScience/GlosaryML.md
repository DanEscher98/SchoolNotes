---
author: Daniel Sanchez
title: Machine Learning Glossary
---

- **Cross validation**: Allows us to compare different machine
    learning methods and get a sense of how well they will work in
    practice. It's very common to divide the data into 10 blocks
    (Ten-Fold Cross Validation).
- **The Confusion Matrix**: The rows correspond to what the `ML`
    algorithm predicted and the columns to the know truth. The numbers
    along the main diagonal, tell us how many time the samples were
    correctly classified; the rest, are samples the algorithm messed
    up.
- **Sensitivity**: For a $2x2$ confusion matrix:
    $$\text{Sensitivity} = \frac{\text{True Positives}}
    {\text{True Positives} + \text{False Negatives}}$$
    For bigger matrix, the values in the *column*, that aren't at the
    main diagonal, are summed to obtain the False Negatives.
- **Specificity**: For a $2x2$ confusion matrix:
    $$\text{Specificity} = \frac{\text{True Negatives}}
    {\text{True Negatives} + \text{False Positives}}$$
    For bigger matrix, the values in the *row* are summed to obtain
    the False Positives.
- **Precision**: For a $2x2$ confusion matrix:
    $$\text{Precision} = \frac{\text{True Positives}}
    {\text{True Positives} + \text{False Positives}}$$
- **Bias**: The inability for a `ML` method to capture the true
    relationship of the data.
- **Variance**: The difference in fits between data sets.
- **overfit**: When a model fits very well the training set but not
    the testing set.
- **Regularization**:
- **Boosting**:
- **Bagging**:
- **ROC**: *Receiver Operator Characteristic* graphs provide a simple
    way to summarize all the information, insted of being overwhelmed
    with confusion matrices. The y-axis show the *True Positive Rate*
    (Sensitivity), and the x-axis the *False Positive Rate ($1 -
    \text{Specificity}$).
- **AUC**: 
- **Entropy**:
- **Linear Regression**:
- **Multiple Regression**:
