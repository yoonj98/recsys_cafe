from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from .model import model
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import pandas as pd
import io
import json
import os

def index(request):

    return render(request, 'main/main.html', {})

@csrf_exempt
def result(request):
    if request.method == "POST":
        # model 임포트했으니까 이런 식으로 사용하면 될 듯?
        target = request.FILES['img'].read() # 업로드된 이미지 - read()의 결과로 바이트 인코딩된 이미지 전송
        img = io.BytesIO(target) # 바이트 인코딩된 이미지 입력
        location = "main/model/"
        df = pd.read_csv(location + 'final_df_link_j.csv')
        close_list = model.image_plus(df, location+'img_final/',img) # 바이트 인코딩된 이미지를 Image.read()가 읽으면 이미지 처럼 사용할 수 있음.



        resultArr = []
        for index in close_list:
            # img_name = df.loc[index]['imgname_123']

            # 이미지 약간 꼼수써서 해결 했습니당 (마무리작업중..)
            resultDict = dict(df.loc[index][['review_cafename', 'link', 'imgname_123']])
            resultArr.append(resultDict) # 임시로 카페 이름과 링크만 가져옴. 추가 가능

        print(resultArr) 

        # 웹으로 전송할 수 있게 JSON 파일로 변환함
        return JsonResponse({"value": resultArr})

@csrf_exempt
def status(request):
    # api서버 상태 체크용
    testArr = [{'review_cafename': '쥬씨 서울시립대점', 'link': 'https://www.diningcode.com/profile.php?rid=V7Rhg37s4yx3'}, {'review_cafename': '17도씨', 'link':
'https://www.diningcode.com/profile.php?rid=ULkIg7tIGmky'}, {'review_cafename': 'Six Degrees Coffee', 'link': 'https://www.diningcode.com/profile.php?rid=QMtadMGwoN9X'}, {'review_cafename': '파오파오차', 'link': 'https://www.diningcode.com/profile.php?rid=ZQ4WJPvmNoZV'}, {'review_cafename': '파브커피', 'link': 'https://www.diningcode.com/profile.php?rid=CTB77NNnELIv'}]
    return JsonResponse({"value": testArr})


def getImg(request):
    
    img = open("main/model/img_final/" + request.GET["imgId"], 'rb')
    response = FileResponse(img)
    
    return response