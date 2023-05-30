from tensorflow.keras.models import load_modelfrom PIL import Image, ImageOps
import numpy as np

# 다운받은 Keras 모델 로드
model = load_model('keras_model.h5')

# 케라스 모델에서 입력으로 받을 수 있는 변수 형식
# shape 매개변수가 (1, 224, 224, 3)으로 입력되는 이유는
# 컬러 이미지를 로드하면 보통 (높이, 넓이, RGB채널 수)의 행렬을 가지게 되는데,
# Keras에서 사용하기 위해 배치 크기를 default로 넣어줘야하고,
# 최종 크기는 (배치 크기, 높이, 넓이, 채널수)가 됩니다.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# 예측에 사용할 이미지 경로
image = Image.open('18111689_1260.jpg')
# 실제 로드할 이미지 크기는 좀더 크지만 모델의 입력으로 넣어주기 위해 리크기합니다.
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

# 이미지 데이터를 numpy array 형식으로 변경
image_array = np.asarray(image)
# 모델에 맞는 정규화 실행
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# array에 이미지 로드
data[0] = normalized_image_array

# 예측(inference) 실행
prediction = model.predict(data)
print(prediction)