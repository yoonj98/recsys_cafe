# recsys_cafe
tobigs conference 14 15

show_and_tell_model.py : show and tell 모델이 정의된 코드입니다 <br><br>
show_and_tell_proprecess.py : 데이터 전처리 및 kor2vec embedding을 만들고 저장하고 show and tell 모델에 적용시키기 위한 dataloader를 만드는 코드입니다. <br><br>
show_and_tell_train.py : show_and_tell 모델을 학습시키기 위한 코드입니다. <br><br>
show_and_Tell_embedding.py : 학습된 show_and_tell 모델에서 review와 image가 들어가있는 embedding을 추출하는 코드입니다.
<br><br>

tag_dataloader.py : tag 모델에 적용시키기 위한 데이터 전처리 및 dataloader를 만드는 코드입니다.
<br><br>
tag_mobilenet.py : tag인 mobilenet 모델이 정의된 코드입니다.
<br><br>
tag_train.py: tag 모델을 학습시키기 위한 코드입니다.
<br><br>
tag_embedding.py : 학습된 tag 모델에서 tag와 image가 들어가 있는 embedding을 추출하는 코드입니다.
<br><br>
similarity_result.py : show and tell model의 embedding을과 tag model의 embedding을 결합하고, 투입된 image와 결합한 embedding 파일의 유사도를 구하여 가장 가까운 5개의 카페를 추천해주는 코드입니다.