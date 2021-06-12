# show and tell

## 파일설명

#### 전처리
- build_vocab.py : <start>, <end>, <pad>, <unk> .을 문장에 넣는 작업 및 toknize. pkl에 저장
- dataHandler.py : 이미지와 caption dataloader 만드는 파일
- preprocess.py : build_vocab과 비슷한 기능을 하는것 같은데 train 과정에서 bulid_vacab과 datahandler를 사용하기때문에 사용안하는것 같음

#### 모델
- model_cnn_rnn.py : 학습에 필요한 
- Model.py : model_cnn_rnn.py에 사용될 encoder(ResNet-152), Decoder RNN(LsTM) 모델 구조를 담은 파일

#### 학습 및 test
- train.py : flickr data set을 train, val, test 나누고 train
- test_model.py : model test

#### baseline 진행상황
현재 flicker 8k를 사용하여 진행 <br>
<br>
image file + caption.txt 로 구성되어 있으며 <br><br>
위 코드에 적용하기 위해 caption.txt는 json 파일로 변환하여 진행 <br><br>
caption.txt 의 형태 <br><br>
columns    image        caption <br>
           image_이름   문장 <br>
<br>
but cuda of memory 문제로 인해 학습 진행이 안됨....
<br>


## <해야할일>...
생각보다 해둔게 없어서 죄송하네요...

#### 1. 데이터 파일 받았을때:
- resnet-152를 이용한 기존 모델로 show and tell baseline 만들기
- encoder의 pretrained model을 사용하여 show and tell baseline 만들기?

#### 2. 데이터 파일을 받지 않았을때 :
- flickr 8 파일로 돌아가는 모델 만들기

#### 2. 생각해볼문제
- 결과 값을 어떻게 추천에 활용할 것인지? (text 유사도? encoder 부분만 사용한다거나?)
- 네이버의 kor2vec(https://github.com/naver/kor2vec)을 사용하면 어떨까? 


<데이터 출처 : https://www.kaggle.com/kunalgupta2616/flickr-8k-images-with-captions> <br>
<코드 출저: https://github.com/Pillercottrer/radcap_project>

