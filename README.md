# Purpose
The purpose of thise project is to identify flavor preferences of e-cigarettes online in order to identify any trends which might be concerning, in particular “brown” or “butter” flavors. This was a data scraping, NLP, and sentiment analysis project. It involved scraping reddit and a popular E-Cig repository. Using the collected data I built a list of commonly used flavors and how often they occurred in recipes, furthermore I used a bag of words approach and a Naive Bayes classifier for sentiment classification and tallied how often flavors were referred to in a positive vs. negative sentiment.


# Findings 
The interesting part is the reddit.txt file, it is an analysis of 497,274 (out of 15,495,518) comments on ecig subreddits. 
The format is flavor: [positive uses, negative uses], I used the e-liquid-recipes flavor list as a reference for flavors. 
Interesting points: butter is used a lot and highly controversial, Vanilla custard is used a lot, vanilla is used a lot, menthol is used a lot positively. 

I still haven’t filtered out junk data like usage of the word juice which is also a flavor or other artifacts like br. These artifacts are generated from cleaning the text which uses a lot of non latin characters. 
