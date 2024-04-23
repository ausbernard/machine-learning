# Teachable Machine <(^_^)>

## Prompt
Over the next two steps, you're going to create your very own rock, paper, scissors game. You will use image classification to teach your computer to recognise gestures you hold up to your webcam. You'll then turn this into a game where you compete against a program that randomly makes its choice.

## Project
This project uses a multi-class image classifier to make a rock, paper, scissors game. It utilizes [Teachable Machine](https://teachablemachine.withgoogle.com/train) which appears to use Tensorflow. 

### Steps:
1. I designated three distinct classes for training: Rock, Paper, and Scissors.
2. Utilizing the webcam feature, I captured over 400 images for each class.
3. Following the image acquisition phase, I proceeded to train the model to accurately identify each class. The culmination of this effort resulted in the creation of the ["final project"](https://teachablemachine.withgoogle.com/models/_ojZ5tIpn/).

## Thoughts
It was a fun project and made me excited doing this. More excited then learning cybersecurity principles. It was fun to see the accuracy it was able to identify. I could see the limitations which were training it to see the actual game of having your hand go "rock, paper, scissors, shoot!" but it was overall pretty accurate. I didn't do much training and the images were captured at night with my monitor being my light. Excited to learn more.

## Discussion
*Is your model worse at identifying one of your classes in particular? If so, why do you think that is?* It excels at identifying the 'rock' class but encounters difficulty with 'paper,' possibly due to its flat nature. The model struggles when it can't distinguish between horizontal scissors and paper because it can't see the other fingers. To address this, I plan to train the model with more images, particularly focusing on differentiating between paper and scissors. By doing so, I anticipate an improvement in its performance. Additionally, I'm interested in testing how the model performs with various factors such as hand size, color, shape, and distance.

*What could you do to improve the accuracy of the algorithm?* In summary, my plan involves training the model with additional images featuring diverse hand sizes, shapes, colors, and gestures. Since individuals may execute rock-paper-scissors differently, this variation will help enhance the model's accuracy. Furthermore, I aim to vary the distance between the hand and the camera to further refine the model's performance.

Overall, this was fun and would like to do more of it. ʕ·͡ᴥ·ʔ