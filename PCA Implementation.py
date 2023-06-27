from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
import numpy as np
from PIL import Image
import imageio


def comp_2d(image_2d, nmobre_comp):  # FONCTION POUR RECONSTRUIRE UNE MATRICE 2D EN UTILISANT L'ACP
    cov_matrice = image_2d - np.mean(image_2d)
    valeurs_propre, vectures_propre = np.linalg.eigh(
        np.cov(cov_matrice))  # Determiner les valeurs et verctures propres
    p = np.size(vectures_propre)
    idx = np.argsort(valeurs_propre)
    idx = idx[::-1]
    vectures_propre = vectures_propre[:, idx]
    valeurs_propre = valeurs_propre[idx]
    if nmobre_comp < p or nmobre_comp > 0:
        vectures_propre = vectures_propre[:, range(nmobre_comp)]
    score = np.dot(vectures_propre.T, cov_matrice)
    recon = np.dot(vectures_propre, score) + np.mean(image_2d).T
    recon_img_mat = np.uint8(np.absolute(recon))
    return recon_img_mat


def comp_3d(url_image_3d, nmobre_comp):
    image_3d = imageio.imread(url_image_3d)
    a_np = np.array(image_3d)
    a_r = a_np[:, :, 0]
    a_g = a_np[:, :, 1]
    a_b = a_np[:, :, 2]
    a_r_recon, a_g_recon, a_b_recon = comp_2d(a_r, nmobre_comp), comp_2d(a_g, nmobre_comp), comp_2d(
        a_b, nmobre_comp)  # RECONSTRUCTION DES COMPOSANTES R, G ET B SÉPARÉMENT
    # COMBINER LES COMPOSANTES R.V.B POUR PRODUIRE UNE IMAGE COULEUR
    recon_color_img = np.dstack((a_r_recon, a_g_recon, a_b_recon))
    recon_color_img = Image.fromarray(recon_color_img)    
    return recon_color_img


def open_image():
    global filepath
    filepath = filedialog.askopenfilename(title="Select Image", filetypes=(
        ("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*")))
    if filepath:
        resized_image = comp_3d(filepath, 20)
        photo = ImageTk.PhotoImage(resized_image)
        label.configure(image=photo)
        label.image = photo
        scale.config(to=resized_image.size[0])
        scale.set(20)
        scale.pack()


root = tk.Tk()
root.title("PCA Image Compression")
root.geometry("700x700")


scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.set(20)
button = tk.Button(root, text="Open Image", command=open_image)
button.pack(pady=10)


def slider_released(event):
    value = scale.get()
    if filepath:
        resized_image = comp_3d(filepath, int(value))
        photo = ImageTk.PhotoImage(resized_image)
        label.configure(image=photo)
        label.image = photo


scale.bind("<ButtonRelease-1>", slider_released)


label = tk.Label(root)
label.pack()

root.mainloop()
