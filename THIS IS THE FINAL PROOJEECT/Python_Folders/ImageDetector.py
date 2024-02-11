from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

PlasticBottle = "you could try reusing the water bottles by filling the inside with water, emptying it, and cleaning the top so that there aren't any germs, and fill it with water. If you don't want to save it, then throw it in the red container. If you don't have containers, type '!HowCanIHelp NoBins'."
Cans = "if you've got a typical soda can, then why don't you try reusing them, of course only if you're going to use it right away, because your soda might go bland! So if you're not going to do that, try using them as storage, for small items like coins, buttons or paperclips! Or you could rinse them out and use them to organize your workspace by storing pens, markers, even smaller tools! That way, you're giving your cans a new purpose. If you're not up to doing that, you could throw them away in the bright blue bin, if you don't have recycling bins, type 'HowCanIHelp NoBins'."

NewsPapers = "you've got some newspapers, how about try to make some Paper Mache! You just need strips of newspapers and glue. First, you have to make a mold of what you want to do, and then make it thicker by using paper mache, by first making the glue (flour and water) and preparing the paper (Cutting the newspapers in small strips), then, put the glue in a small bowl, and to actually start using it, get your mold, put a strip of paper and put it in the glue, DON'T LET IT DRY, distribute the paper around the model evenly, and once you're done using all the paper, let it dry. Tadaa! You've got a paper mache mold. Fun Fact: the creator of this bot used paper mache to make a sheath for his wooden sword."


def detect_image(model_path, labels_path, image_path):
    # Make the message
    message = ""

    # Load the model
    model = load_model("../keras_model.h5", compile=False)

    # Load the labels
    class_names = open("../labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Return the result as a string
    print (f"{class_name[2:]}")
    print(str(int(confidence_score*100))+ "%")
    return f"{class_name[2:]}"