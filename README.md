# COSC448-ResearchProject
Analyzing mentor-mentee relationships based on quantitative data from open source projects on GitHub to determine what contributes to a successful mentorship. 
This analysis is a continuation of and based on the Honours thesis project by Jasmine Mishra https://github.com/coffeehousejazz/honours_thesis.git


Specifically with regard to the following research questions:

RQ1: Does communication matter? Does the number and type of comments that a mentor and mentee have on each other affect the success of a relationship?

- The sentiment analysis of comment text
  Using:
  https://huggingface.co/j-hartmann/emotion-english-distilroberta-base (base emotions - anger/disgust/fear/joy/neutral/sadness/surprise) 
  
- Number of questions in the comment text
  Using:
  https://huggingface.co/shahrukhx01/question-vs-statement-classifier (question/statement)

- The general tone of comment text
  Using:
  https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment (positive/neutral/negative)



RQ5: Does guiding documentation matter? Do pull request labels guide mentees? Are pull request labels helpful in success?

- Pull request title text analysis
  Using:
  https://huggingface.co/madhurjindal/autonlp-Gibberish-Detector-492513457 (clean/mild-gibberish/word-salad/noise)
  
- Pull request body text analysis
  Using:
  https://huggingface.co/neuralsentry/starencoder-git-commit-bugfix-classification (bugfix/non-bugfix)
  https://huggingface.co/madhurjindal/autonlp-Gibberish-Detector-492513457 (clean/mild-gibberish/word-salad/noise)




