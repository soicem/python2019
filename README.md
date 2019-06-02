# 국민건강정보 결정학습 및 시각화

학과 | 학번 | 성명
---- | ---- | ---- 
정보컴퓨터공학 |201624642 |김남규


## 프로젝트 동기 및 목적

 Information entropy는 GPU 없이 현재 가지고 있는 장비로 할 수 있는 학습 방법이며 결과도 학습하는 방법을 설명할 수 없는 CNN, RNN을 제외하고는 결과가 가장 잘 나오는 방법 중 하나다.  공개되어있는 국민건강검진 데이터를 활용하여 나이, 성별, 콜레스테롤 지수 등을 주고 이 사람이 음주를 하는지와 같은 정보를 판별한다.

## 프로젝트 개요
![](https://github.com/soicem/python2019/blob/master/%EA%B0%9C%EC%9A%94%EB%8F%84.PNG)

 국민 건강데이터를 전처리한 후 해당 feature들 중 유의미한 feature를 선정하여 학습한다.  학습시킨 데이터의 feature를 slicing하거나 max depth를 늘리거나 줄여본다.  본 프로젝트에서는 트리 시각화를 위하여 max depth를 늘리고 줄이는 것을 주로 진행하였다.  해당 결과가 만족스럽다면 Report를 생성한다.

## 사용한 공공데이터 
[데이터보기](https://github.com/soicem/python2019/blob/master/NHIS_OPEN_GJ_2017.CSV)

## 소스
* [링크로 소스 내용 보기](https://github.com/soicem/python2019/blob/master/informationEntropy.py) 
