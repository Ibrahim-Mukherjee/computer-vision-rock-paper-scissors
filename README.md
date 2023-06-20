# Computer Vision RPS

# Rock Paper Scissors Machine Learning Model with Vision Detection

This project aims to create a machine learning model for playing the game "Rock Paper Scissors" using vision detection. The model will be trained to classify four classes: Rock, Paper, Scissors, and Nothing (when no hand gesture is detected). The goal is to accurately identify the hand gesture made by a player and determine the corresponding move in the game.

## Technologies Used

The following technologies are used in this project:

- Python: The programming language used for implementing the machine learning model and related scripts.
- TensorFlow Keras Layer: A popular open-source machine learning framework used for building and training the model.
- OpenCV: A computer vision library used for processing and analyzing the input images or video frames.
- NumPy: A fundamental library for scientific computing in Python, used for handling numerical operations and data manipulation.
- FastAPI: A modern web framework for building APIs, which will be used to serve the machine learning model.
- Pydantic: A library for data validation and parsing, used for asserting the data types of incoming requests.
- Uvicorn: A lightning-fast ASGI server implementation, used to run the API server locally.

## Milestone 1

In the first milestone, the initial setup of the project is completed, and the basic structure for the machine learning model is implemented. The FastAPI framework is chosen for creating the API, along with pydantic for data type assertions. The server is run locally using Uvicorn.

```python
# Insert your code snippets for milestone 1 here
```

Screenshot:

![Milestone 1 Screenshot](milestone1_screenshot.png)

## Milestone 2

In this milestone, the connection between the previous milestone and the current one is established. The technologies used include Kafka, a distributed streaming platform, and Docker for containerization.

Example command run in the terminal:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

The above command is used to check if the Kafka topic has been successfully created. Once confirmed, the API script is edited to send data to the created Kafka topic. The Docker container used has an attached volume, allowing for file editing persistence on the container.

```python
# Insert your code snippets for milestone 2 here
```

Screenshot:

![Milestone 2 Screenshot](milestone2_screenshot.png)

## Milestone n

Continue the process for each milestone, explaining the tasks, concepts, and technologies used in each. Provide code snippets and screenshots to demonstrate the progress made throughout the project.

## Conclusions

In conclusion, this project has successfully built a machine learning model for playing Rock Paper Scissors using vision detection. It leverages computer vision techniques and deep learning algorithms to accurately classify hand gestures. Through the milestones, we have demonstrated the understanding and utilization of various technologies such as TensorFlow, OpenCV, FastAPI, Kafka, and Docker.

To further improve the project, additional training data could be collected to enhance the model's accuracy. The inclusion of more sophisticated computer vision algorithms or exploring alternative machine learning architectures could also be considered. Furthermore, integrating the model into a user-friendly application or game interface would provide a more interactive experience for users.

Reading through the documentation, it should provide a clear and cohesive understanding of the project, including the tasks accomplished, technologies used, and the rationale behind them. The inclusion of code snippets and screenshots offers tangible evidence of the progress made and the functioning of the system.
