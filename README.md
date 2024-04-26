# Learn-Bert-Again
I want to use this place to restore my own code and write down my process of my learn.

# My result 2024.04.26
I modify the code from https://github.com/cxy229/BDCI2019-SENTIMENT-CLASSIFICATION. The final code is called roberta.py and put in the folder.

I get my train data and test data from https://www.datafountain.cn/competitions/350. It is lucky that I can find this website which held a competition about analyzing the emotion in the Internet News using LLM. 

And my macro-F1 score of eval data is 0.7821222515304876.  The train steps is 10000. The batch size is 8. It also means that I train the model for 27 epochs. If you want to see the detail, just open the eval_result.txt.

I also find another test data from other websites. But it is embarrassed that I forget where I get them. If I find the source, I will update readme.md as soon as possible. 

My weighted-F1 score of test data is 0.778953700008025. The reason why I use weighted-F1 score is that the test data is unbalanced. The number of label 0 is 322. And the number of label 1 is 6097. The number of label 2 is 4676. You can see the detail of test data in .\data\all_test2.csv. And you should encode it using "utf8".

If you want to know more details, you can open data folder and code folder. It is obvious that all_train2.csv is my train data.

And in fact, I run the py using Slurm. Thanks to the ZJU, providing the necessary source of training model for students.

In the future, I will process the data more carefully. And change model to see if it can make our result better.

In the end, I think it is a meaningful opportunity to learn how to train model and use it in the research.



