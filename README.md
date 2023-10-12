# Bert-Sentiment-Classification
Fine turning of Bert-base-uncased based on Amazon Customer Reviews

1.模型选择：为了完成电商评论中的情感分类任务，我们的一个问题是：我们应该用哪个模型呢？
由于情感分类输入NLU任务，而目前拥抱脸在transformer库中已经搭载了很多预训练好的BERT模型，因此，为了节约成本和降低训练难度，这里我们选用transformer库中的Bert-base-uncased模型进行微调和推理。

Bert-base-uncased 模型在transformer库中有许多不同的版本，如下图所示：

![image](https://github.com/HDX37/Bert-Sentiment-Classification/assets/128899278/02fec6ed-f2ab-404b-b367-371b1939ccd0)

从图片中我们可以看到，transformer库中自带了用于不同任务的Bert模型，由于我们要实现的情感分类属于句子分类任务中的一种，因此这里我们选择"BertForSequenceClassification"作为本次任务的推理模型。

2.预训练参数加载：Bert-base-uncased模型一共有1亿多个参数，因此，如果要从头训练该模型是十分困难的。好在拥抱脸团队已经为我们预训练了这个模型，不需要我们再从头对该模型进行训练。
为了加载预训练好的模型参数，我们可以在工程目录下创建一个bert-base-uncased的文件夹，其结构如下图所示：


![image](https://github.com/HDX37/Bert-Sentiment-Classification/assets/128899278/8dbfc4f6-8cb7-4f99-896d-e6a07712da57)

接着，使用

![image](https://github.com/HDX37/Bert-Sentiment-Classification/assets/128899278/c9552053-fdb0-491f-aef5-87968aec0a1d)
便可加载模型预训练参数。

3.准备数据集：本次预训练用的数据集是来自Amazon电商平台的用户评论，数据集文件我已经放到项目当中，大家可自行提取。不过大家也可根据自己的实际任务更改训练用的数据集，不过不同的数据集文件里面的格式可能有所区别，更改数据集后Dataset里的代码也有做相应的调整。具体调整的细节如果有不懂的可私信我~

4.开始训练：这里重点讲一下训练过程中可能会出现的几个问题：

①提示输入数据大于512.这个问题主要是输入Bert-base-uncased模型的单词个数超过512导致的，因为Bert-base-uncased模型最多只能接受512个词大小的句子输入，如果输入句子的单词数量超过512，就会报错。

解决方案：确保Dataset中的输出句子中的单词数始终在512内。

②模型无法收敛：这个问题主要是由于自己设计的前馈网络不合适造成的，由于在微调的时候，我们是靠加载预训练的Bert参数来进行初始化训练，所以要想充分利用预训练中模型的参数，应尽量保证微调的模型结构和预训练的模型结构相似，以便让模型更快地收敛。

解决方案：尽量确保微调时的Bert网络结构和预训练时的前馈网络结构相似。

③训练速度太慢：Bert模型大约有1亿个参数，因此，训练速度慢是正常的。如果想增加训练速度，可采用Lora等微调技术，可增加训练速度，具体可参考关于Lora微调的文章。（如果大家对这个的需求比较大的话，后续我再出一期主讲Lora微调的项目）

解决方案：采用Lora微调技术。

④超参数设置：这里主要是学习率，本项目中学习了设置为1e-5。在该学习率下，用3090（12GB）训练1个小时（1个epcho）即可实现98%的准确率。

解决方案：lr = 1e-5.
  
5.训练完毕:大家训练完毕后可自行输入对话进行测试，第一次实现还是蛮有成就感的~







