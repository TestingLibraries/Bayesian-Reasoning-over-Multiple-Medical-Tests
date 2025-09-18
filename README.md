# Bayesian-Reasoning-over-Multiple-Medical-Tests

---

## What does this tool do?

This tool allows you to calculate the probability of disease given how a patient has tested over as many tests as you would like.

This tool serves to answer the following question,
what is the probability, that my patient has the disease, given that they test either positive or negative?
This is in contrast to sensitivity and specificity, where the probabilities are in reverse.
Sensitivity and Specificity tell you what is the probability a patient will test positive or negative given or not given that they have the disease,
However this might not be so useful, because we dont know whether or not the patient has the disease, until we test them.

## How do i use this tool?
Simply key in the sensitivity, specificity and prevalence of the tests you are ordering, in the order of which they are being ordered.
If you lack the prevalence, you can instead key in a prior belief, from 0-100

## Do i need any dependencies?
No, this is stock python.
