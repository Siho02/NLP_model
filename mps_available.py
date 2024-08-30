import torch

if torch.backends.mps.is_available():
    #device = torch.device("mps")
    print('MPS available')
else:
    #device = torch.device("cpu")
    print('MPS not available')

#x = torch.randn(3, 3).to(device)

# 텐서를 MPS 장치로 이동
#x = torch.randn(3, 3).to(device)

# 모델을 MPS 장치로 이동
#model = MyModel().to(device)

# 모델과 데이터를 사용한 연산 수행
#output = model(x)
