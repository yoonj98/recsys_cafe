<br><br>
![image](https://user-images.githubusercontent.com/67720742/125874259-83d76782-bf2b-4a27-a035-688303aa645f.png)

# 카페인(Cafe-in)
### 너는 내 취향저격, 이미지 기반 카페 추천시스템
2021.07.17 **[제 12회 투빅스 컨퍼런스]** 발표작
- **카페 이미지**를 넣으면, 유사한 느낌의 **카페를 추천**해주는 서비스입니다.
- 이미지뿐만 아니라 기존 카페 이용고객들의 **리뷰**와 **태그 데이터**를 활용합니다.
- 다이닝코드 데이터 기반으로 진행하였으며, 상업적으로 이용할 의도가 전혀 없음을 밝힙니다. (넣을지말지)

<br>

## Structure

```python
카페인
├── README.md
├── data_preprocessing
│   ├───crawling.py
│   └───preprocess.py
│   
├── final_model
│   ├── show_and_tell
│     ├───show_and_tell_proprecess.py
│     ├───show_and_tell_embedding.py
│     ├───show_and_tell_model.py
│     ├───show_and_tell_train.py
│     └───similarity_result.py
│   ├── tag   
│     ├───tag_dataloader.py
│     ├───tag_embedding.py
│     ├───tag_mobilenet.py
│     └───tag_train.py

```
**show_and_tell_model.py** : show and tell 모델이 정의된 코드입니다 <br><br>
**show_and_tell_proprecess.py** : 데이터 전처리 및 kor2vec embedding을 만들고 저장하고 show and tell 모델에 적용시키기 위한 dataloader를 만드는 코드입니다. <br><br>
**show_and_tell_train.py** : show_and_tell 모델을 학습시키기 위한 코드입니다. <br><br>
**show_and_Tell_embedding.py** : 학습된 show_and_tell 모델에서 review와 image가 들어가있는 embedding을 추출하는 코드입니다.
**tag_dataloader.py** : tag 모델에 적용시키기 위한 데이터 전처리 및 dataloader를 만드는 코드입니다.
<br><br>
**tag_mobilenet.py** : tag인 mobilenet 모델이 정의된 코드입니다.
<br><br>
**tag_train.py**: tag 모델을 학습시키기 위한 코드입니다.
<br><br>
**tag_embedding.py** : 학습된 tag 모델에서 tag와 image가 들어가 있는 embedding을 추출하는 코드입니다.
<br><br>
**similarity_result.py** : show and tell model의 embedding을과 tag model의 embedding을 결합하고, 투입된 image와 결합한 embedding 파일의 유사도를 구하여 가장 가까운 5개의 카페를 추천해주는 코드입니다.
<br>

## Results 
![image](https://user-images.githubusercontent.com/67720742/125874187-69255e01-be11-4ea6-81a8-e184086ac51d.png)

<br>

## Presentation
저희 프로젝트에 대해 자세하게 알고 싶으시다면, 프로젝트 설명자료를 참고해주세요. 
** 여기에 PDF 파일 임베딩해서 넣고싶다 **
** 여기에 유튜브 링크도 첨부 **


## Contributors
빅데이터 동아리 **[ToBig's](http://www.datamarket.kr/xe/)** 멤버들이 함께한 프로젝트입니다.
<table>
  <tr>
    #준영
    <td align="center"><a href="https://github.com/pjy970108"><img src="https://user-images.githubusercontent.com/41895063/104710310-45d68e80-5763-11eb-8bca-3d11bab3f636.png" width="150" height="150"><br /><sub><b>박준영</b></sub></td>
      #지우
    <td align="center"><a href="https://github.com/simba-pumba"><img src="https://user-images.githubusercontent.com/41895063/104711155-576c6600-5764-11eb-8a1e-a7a011cfe17d.png" width="150" height="150"><br /><sub><b>강지우</b></sub></td>
      #유진
    <td align="center"><a href="https://github.com/yourmean"><img src="https://user-images.githubusercontent.com/41895063/104711276-7cf96f80-5764-11eb-8473-99c5c0dc8a8a.png" width="150" height="150"><br /><sub><b>한유진</b></sub></td>
      #민준
    <td align="center"><a href="https://github.com/lilly9117"><img src="https://user-images.githubusercontent.com/41895063/104711018-29872180-5764-11eb-9858-53c5f4cc26e4.png" width="150" height="150"><br /><sub><b>안민준</b></sub></td>
  </tr>
</table>

<table>
  <tr>
    #이윤정
    <td align="center"><a href="https://github.com/mink7878"><img src="https://user-images.githubusercontent.com/55529646/104719170-6a386800-576f-11eb-8b55-36b524c4d166.jpg" width="150" height="150"><br /><sub><b>이윤정</b></sub></td>
      #김현지
    <td align="center"><a href="https://github.com/shkim960520"><img src="https://user-images.githubusercontent.com/55529646/104719176-6d335880-576f-11eb-849f-4d6756824d68.jpg" width="150" height="150"><br /><sub><b>김현지</b></sub></td>
      #강재영
    <td align="center"><a href="https://github.com/Jeong-JaeYoon"><img src="https://user-images.githubusercontent.com/55529646/104719173-6b699500-576f-11eb-9a42-a8569be057bc.jpg" width="150" height="150"><br /><sub><b>강재영</b></sub></td>
      #이원도
    <td align="center"><a href="https://github.com/Yu-Jin22"><img src="https://user-images.githubusercontent.com/41895063/104711416-afa36800-5764-11eb-85c1-1a9ad50033b7.png" width="150" height="150"><br /><sub><b>이원도</b></sub></td>
