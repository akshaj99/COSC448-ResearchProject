# COSC448-ResearchProject
Analyzing mentor-mentee relationships based on quantitative data from open source projects on Github to determine what contributes to better mentorship. 
This analysis is a continuation of and based on the Honours thesis project by Jasmine Mishra https://github.com/coffeehousejazz/honours_thesis.git


Specifically on the following research questions:

RQ1: Does communication matter? Does the number of comments that a mentor and mentee have on each other affect the success of a relationship?

No. Of conversation vs sentiment analysis(hugging face) - https://huggingface.co/SamLowe/roberta-base-go_emotions (in depth emotions) - https://huggingface.co/j-hartmann/emotion-english-distilroberta-base (base emotions) - https://huggingface.co/microsoft/deberta-large-mnli (entailment/neutral/contradiction) - https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment (positive/neutral/negative)
No. of questions in comment data - https://huggingface.co/shahrukhx01/question-vs-statement-classifier
General tone of sentences when communicating - https://huggingface.co/yiyanghkust/finbert-tone



RQ5: Does guiding documentation matter? Do pull request labels guide mentees? Are pull request labels that are made for the newcomer/mentee helpful in success?

Pull request title text analysis(hugging face) (explanatory vs reduntant)
Pull request body text analysis(hugging face) (explanatory vs reduntant) - https://huggingface.co/neuralsentry/starencoder-git-commit-bugfix-classification (bugfix/non-bugfix) - https://huggingface.co/madhurjindal/autonlp-Gibberish-Detector-492513457 (clean/mild-gibberish/word-salad/noise)




