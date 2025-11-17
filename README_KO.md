# CVnet 홈 어시스턴트 통합
[English](README.md) | [한국어](README_KO.md)

CVnet 홈 어시스턴트 통합은 CVnet SmartHome 애플리케이션을 통해 동작합니다.

**참고**: 현재 더포디엄830 (서울) 아파트만 지원합니다. 아파트별로 API가 다르기 때문에 다른 아파트 지원을 희망하는 경우, 개발 목적으로 사용될 본인 계정을 제공해주시거나 직접 이 프로젝트에 기여해주세요.

## 설명
[CVnet SmartHome 애플리케이션](https://play.google.com/store/apps/details?id=com.cvnet.smarthome.cvnet&hl=ko)의 기기를 홈 어시스턴트에 연결할 수 있습니다.

### 통합
먼저 CVnet SmartHome 애플리케이션에서 계정을 등록해야 합니다. 그런 다음 통합 항목을 설정하는 동안 양식에 CVnet 계정 정보를 입력해야 합니다.

![image](https://github.com/user-attachments/assets/36a23794-0720-42e7-b459-73a16a4f8dee)


## 설치
### HACS
아래 링크를 통해 쉽게 설치할 수 있습니다.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=nnnlog&repository=homeassistant-cvnet-smarthome&category=integration)

또는 HACS 스토어에서 `cvnet` 키워드로 통합을 찾을 수 있습니다.

![image](https://github.com/user-attachments/assets/909a7614-b988-4e6c-8e9c-0ec073136871)


### 수동 설치
`custom_components/cvnet/`의 내용을 Home Assistant의 `custom_components/cvnet/` 디렉토리에 복사합니다.

## 지원되는 기기
- 난방
- 조명
- 환기
- 대기 전력 (전원 콘센트)
- 원격 검침 (에너지, 물, 가스)

## 스크린샷
![image](https://github.com/user-attachments/assets/c5091e20-90e0-4985-8724-bae40dff4342)
![image](https://github.com/user-attachments/assets/d8e73655-85e3-4aee-8079-462d7fdc7f42)
![image](https://github.com/user-attachments/assets/34c4bfbc-e148-47b5-bf08-b0f865460012)

## TODO
* 방범 모드 : 재실, 외출, 수면 (Select)
* 일괄소등 : 이 기능은 개별 제어를 지원하지 않는 조명(예. 화장실)을 포함한 모든 조명을 제어할 수 있습니다. (이진 스위치)
* 가스 : 안전을 위해 끄는 것만 지원됨 (이진 스위치 [끄는 것만 지원])
* 방문자 사진 (이미지)
* 엘리베이터 (버튼)
