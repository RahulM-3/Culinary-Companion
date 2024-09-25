import util
import recipe
import cv2

print()
print("Application output:")

cam = cv2.VideoCapture(0)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('main/temp_files/output.mp4', fourcc, 20.0, (frame_width, frame_height))

captured_ing = {}

while True:
    ret, frame = cam.read()
    out.write(frame)
    
    text = util.get_text(frame)
    start = False
    if(text):
        print("Captured input:\n", text)
        start = input("Type 'start' to get recipe recommendation: ")

    if(start == "start"):
        recipe = recipe.get_recipe_recommendation(util.get_text(frame))
        output_text = f'Today let us cook {recipe["Title"]}, you need {recipe["Ingredients"]}, here is the steps to cook it, {recipe["Direction"]}'

        print(output_text)
        util.generate_speech(output_text)


    if cv2.waitKey(1) == ord('q'):
        break


cam.release()
out.release()
cv2.destroyAllWindows()
