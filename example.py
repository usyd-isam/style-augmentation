from styleaug import StyleAugmentor

import torch
from torchvision.transforms import ToTensor, ToPILImage
from PIL import Image
import matplotlib.pyplot as plt


# PyTorch Tensor <-> PIL Image transforms:
toTensor = ToTensor()
toPIL = ToPILImage()

# load image:
im = Image.open('mug.png')
im_torch = toTensor(im).unsqueeze(0) # 1 x 3 x 256 x 256

# create style augmentor:
augmentor = StyleAugmentor()

im_torch = im_torch.to(augmentor.device)

# randomize style:
im_restyled = augmentor(im_torch)

# display:
plt.imshow(toPIL(im_restyled.squeeze().cpu()))
plt.show()