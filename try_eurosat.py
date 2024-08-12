
import geotorchai
import geotorchai.datasets
import geotorchai.datasets.raster
full_data = geotorchai.datasets.raser.EuroSAT(root="data/eurosat", download=True, include_additional_features=True)
geotorchai.datasets.raster.EuroSAT(root="data/eurosat", download=True, include_additional_features=True)



#########################################################################################################################################################
from torch.utils.data import DataLoader

from torchgeo.datamodules.utils import random_split
from torchgeo.datasets import EuroSAT
type(EuroSAT)


EuroSAT

# Initialize the dataset
dataset = EuroSAT(root="/home/contrerasnetk/Documents/Repositories/DatasetsMLSTAC", download=False, checksum=False)
type(dataset)

dataset[0]

# Initialize the dataloader with the custom collate function
dataloader = DataLoader(
    dataset,
    batch_size=128,
    shuffle=True,
    num_workers=4,
    collate_fn=random_split,
)

for i, batch in enumerate(dataloader):
    if i == 0:  
        print("Contenido del primer lote:")
        print(f"Imágenes (shape): {batch['image'].shape}")
        print(f"Cajas delimitadoras: {batch['boxes']}")
        print(f"Etiquetas: {batch['labels']}")
        if "masks" in batch:
            print(f"Máscaras: {batch['masks']}")
    break

# Training loop
for batch in dataloader:
    print(batch)
    images = batch["image"]  # list of images
    boxes = batch["boxes"]  # list of boxes
    labels = batch["labels"]  # list of labels
    masks = batch["masks"]  # list of masks

    # train a model, or make predictions using a pre-trained model