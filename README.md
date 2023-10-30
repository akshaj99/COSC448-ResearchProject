Mentorship Success-ResearchProject

This analysis is a continuation of and based on the Honours thesis project by Jasmine Mishra https://github.com/coffeehousejazz/honours_thesis.git

Analyzing mentor-mentee relationships based on quantitative data from open source projects on GitHub and Google Summer of Code over the years 2021 and 2022 to determine what contributes to a successful mentorship. 


Specifically with regard to the following research questions:

RQ1: Does communication matter? Does the number and type of comments that a mentor and mentee have on each other affect the success of a relationship?

- The sentiment analysis of comment text (using: https://huggingface.co/j-hartmann/emotion-english-distilroberta-base (base emotions - anger/disgust/fear/joy/neutral/sadness/surprise) )
  
- Number of questions in the comment text (using: https://huggingface.co/shahrukhx01/question-vs-statement-classifier (question/statement) )

- The general tone of comment text (using: https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment (positive/neutral/negative) )



RQ5: Does guiding documentation matter? Do pull request labels guide mentees? Are pull request labels helpful in success?

- Pull request title text analysis (using: https://huggingface.co/madhurjindal/autonlp-Gibberish-Detector-492513457 (clean/mild-gibberish/word-salad/noise) )
  
- Pull request body text analysis (using: https://huggingface.co/neuralsentry/starencoder-git-commit-bugfix-classification (bugfix/non-bugfix) and https://huggingface.co/madhurjindal/autonlp-Gibberish-Detector-492513457 (clean/mild-gibberish/word-salad/noise) )




