# Compression and Reconstruction of Color Image Using PCA

## The input image:

<div align="center">
  <img src="./demo/src.jpg" width="50%"/>
</div>

## 100 Principal Components:

<div align="center">
  <img src="./demo/20.jpg" width="50%"/>
</div>

## 300 Principal Components:

<div align="center">
  <img src="./demo/50.jpg" width="50%"/>
</div>

## 600 Principal Components:

<div align="center">
  <img src="./demo/100.jpg" width="50%"/>
</div>


# Conclusion:

By utilizing the first 100 principal components (PCs), a relatively high-quality image was reconstructed. It is worth noting that in our eigendecomposition step, we had 600 PCs since our input image had 600 columns. Therefore, PCA analysis can significantly reduce the image's dimensions. Moreover, you can adjust the mean normalization step to your liking; for instance, you can use 0.5 * np.mean(2D_image, axis=1) to reduce noise to some extent. I recommend giving it a try.
