# video_recorder
My  video recorder using OpenCV

cv.VideoCapture를 이용하여 노트북의 카메라 영상을 얻어 왔습니다.
cv.VideoWriter를 이용하여 동영상 파일을 만들어 줍니다.('webcam.avi')
preview와 record 모드를 구현하였으며, space 바를 누를때마다 모드가 전환됩니다.
(각각의 창을 띄우도록 구현했습니다.)
record모드일때는 화면에 빨간색 원을 띄우며, 영상이 저장되기 시작합니다.
esc키를 누르면 프로그램이 종료됩니다.

추가기능:
+와 -버튼을 눌렀을때 밝기가 조정되도록 했으며, 이를 화면 상단에 출력합니다
