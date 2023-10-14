![image](https://github.com/HDX37/Bert-Sentiment-Classification/assets/128899278/e3b64b19-6e27-4ece-9806-c695e10623c3)# AI may watch movie like humam
Fine turning of LLM and EasyOCR work with each other to ahieve this (Updating……)

To enable AI to understand movies, we conducted tests using BERT and EasyOCR. The objective of this test was to enable AI to differentiate between drama movies and tragedy movies.

# The Implementation results
Based on our test results, the objective of using BERT and EasyOCR for movie classification is to enable AI to differentiate between drama movies and tragedy movies. Through training and testing, our model has achieved good performance in this task. It can accurately classify movies based on factors such as plot, dialogue, and emotions, providing corresponding predictions. This allows AI to better understand and analyze movie content, providing users with more precise recommendations and suggestions. We will continue to optimize and improve this model to enhance its performance and accuracy.

**TV sitcom “Ipartment”**

![image](https://github.com/HDX37/Bert-Sentiment-Classification/assets/128899278/425433a2-1688-4e36-88ad-1a692914a3eb)


```python
#out: this is dama video
```



**Movie “Interstellar”**

![image](https://github.com/HDX37/Bert-Sentiment-Classification/assets/128899278/a61b646b-a4c1-4b7a-a4a8-fb963570677c)

```python
#out: this is tragic video
```

# Usage
To make it more convenient for everyone to use this project, we have simplified the input design. You just need to execute the  ```usage.py```  file to perform sentiment analysis on your own videos.

Like this:

```python
#usage.py
root = './Datas/video2.mp4'
language = 'En'
Via(root,language)
```

# Acknowledgements 
Special thanks to the following individuals for their support and contributions to this project:

- [HuggingFace](https://huggingface.co/)
- [JaidedAI](link2)

We would like to thank everyone who provided feedback and support for this project.










