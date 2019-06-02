# 국민건강정보 결정학습 및 시각화

학과 | 학번 | 성명
---- | ---- | ---- 
정보컴퓨터공학 |201624642 |김남규


## 동기 및 목적

 Information entropy는 GPU 없이 현재 가지고 있는 장비로 할 수 있는 학습 방법이며 결과도 학습하는 방법을 설명할 수 없는 CNN, RNN을 제외하고는 결과가 가장 잘 나오는 방법 중 하나다.  공개되어있는 국민건강검진 데이터를 활용하여 나이, 성별, 콜레스테롤 지수 등을 주고 이 사람이 음주를 하는지와 같은 정보를 판별한다.

## 개요
![](https://github.com/soicem/python2019/blob/master/res/%EA%B0%9C%EC%9A%94%EB%8F%84.PNG)

 국민 건강데이터를 전처리한 후 해당 feature들 중 유의미한 feature를 선정하여 학습한다.  학습시킨 데이터의 feature를 slicing하거나 max depth를 늘리거나 줄여본다.  본 프로젝트에서는 트리 시각화를 위하여 max depth를 늘리고 줄이는 것을 주로 진행하였다.  해당 결과가 만족스럽다면 Report를 생성한다.

## 내용
```
건강정보 음주
```
![](https://github.com/soicem/python2019/blob/master/res/%EA%B1%B4%EA%B0%95%EC%A0%95%EB%B3%B4.png)
![](https://github.com/soicem/python2019/blob/master/res/%EC%9D%8C%EC%A3%BC%EC%97%AC%EB%B6%80.png)

```
decision tree depth==1
```
![](https://github.com/soicem/python2019/blob/master/res/max_depth1.png)
```
decision tree depth==2
```
![](https://github.com/soicem/python2019/blob/master/res/max_depth2.png)
```
decision tree depth==3 with prediction report

*gamma GTP
 ALP와 함께 쓸개 모세관 손상을 반영하는 효소로 주로 간세포의 쓸개모세관쪽 세포막에 존재한다. GGT는 간세포 손상때보다는 간의 폐쇄성질환과 공간점유병변 때 더 높게 상승하며 GGT는 간질환 없이도, 알코올 중독자, 비만한 사람의 일부, 아세트아미노펜, 페니토인, 카르바마제핀 같은 약물의 과다복용 때 상승할 수 있다.

```
![](https://github.com/soicem/python2019/blob/master/res/max_depth3.png)
![](https://github.com/soicem/python2019/blob/master/res/report%20depth3.PNG)
```
decision tree depth==13 with prediction report
```
![](https://github.com/soicem/python2019/blob/master/res/max_depth12.png)
![](https://github.com/soicem/python2019/blob/master/res/report%20depth13.PNG)

## 사용한 공공데이터 
[데이터보기](https://github.com/soicem/python2019/blob/master/NHIS_OPEN_GJ_2017.CSV)

## 소스
* [링크로 소스 내용 보기](https://github.com/soicem/python2019/blob/master/informationEntropy.py) 

## 파이썬 모듈 리스트

번호 | 이름
---- | ---- 
---- | 모듈
1 | sklearn decisionTree
2 | graphviz
3 | pandas
4 | numpy
---- | ----
---- | 환경
1 | Python 3.5
2 | anaconda
3 | windows 10
