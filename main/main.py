import pickle
import tensorflow as tf
import numpy as np
import util

# load tokenizer word index
with open('main/model/Culinary-Companion-word_index.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load trained rnn model
recommendation_model = tf.keras.models.load_model('main/model/Culinary-Companion-V0.1.keras')

def get_recipe_recommendation(ingredients: str) -> dict[str, str]:
    max_seq_len = 232
    for _ in range(max_seq_len):
        token_list = tokenizer.texts_to_sequences([ingredients])[0]
        token_list = tf.keras.utils.pad_sequences([token_list], maxlen=max_seq_len-1, padding = "pre")
        predicted = recommendation_model.predict(token_list, verbose=0)
        predicted = np.argmax(predicted, axis=-1)
        
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                if(word == "~"):
                    break
                output_word = word
                break
        ingredients += " "+output_word

    #ingredients = ingredients.encode("windows-1252").decode("utf-8")
    outputlist = ingredients.split(" | ")
    recipe = {}
    recipe["NER"] = outputlist[0]
    recipe["Title"] = outputlist[1]
    recipe["Ingredients"] = outputlist[2]
    recipe["Direction"] = outputlist[3]
    return recipe

#print()
print("Application output:")
#for i in range(1, 5):
#    print(get_recipe_recommendation(ocr.get_text(f"testdata/{i}.png")))

recipe = get_recipe_recommendation(util.get_text("main/testdata/3.png"))
output_text = f'Today let us cook {recipe["Title"]}, you need {recipe["Ingredients"]}, here is the steps to cook it, {recipe["Direction"]}'

print(output_text)
util.generate_speech(output_text)