# Chicken-Disease-Classification

### Project Description:

The objective of this project is to distinguish between two distinct categories of chicken fecal samples: those displaying symptoms of disease (specifically Coccidiosis) and those reflecting normal, healthy characteristics. Leveraging advanced computer vision techniques, this initiative involves analyzing and interpreting images of fecal samples.

### Purpose and Achievement:

This project is more than just a classification task; it represents my journey into understanding end-to-end machine learning workflows. In pursuit of this goal, I meticulously designed and implemented the frontend, backend, and machine learning components. This holistic approach allowed me to grasp the complete lifecycle of a machine learning project, from data preprocessing to model deployment.

### **Technologies and Frameworks Utilized**

![Tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Fastapi](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![DVC](https://img.shields.io/badge/DVC-945DD6?style=for-the-badge&logo=dataversioncontrol&logoColor=white)

### **Challenges Faced**

During this project, one notable challenge was managing the complexity of the pipeline. Integrating frontend, backend, and machine learning components brought to light the intricacies and potential bottlenecks within the workflow. Coordinating these diverse elements was a learning curve, revealing opportunities for refinement and simplification.

### **Future Development and Features**

To streamline future projects, I aim to address these challenges by refining the pipeline architecture. This includes optimizing the flow between frontend, backend, and machine learning segments for enhanced efficiency and maintainability. Implementing a well-defined folder structure for both the ML and backend components will be a key focus. This structuring will aid in organizing codebases, maintaining modularity, and ensuring scalability.

# How to run?

### STEPS:

Clone the repository

```bash
git clone https://github.com/ja-yy/Chicken-Disease-Classification
```

### STEP 01- Create a pipenv environment after opening the repository

```bash
pipenv shell
```

### STEP 02- Install the requirements

```bash
pipenv install -r requirements.txt
```

```bash
# install frontend dependencies
cd FN

npm i
```

### STEP 03- Train Model

```bash
# Before starting backend server run below command
dvc init

dvc repro
```

### STEP 04- Run Backend server

```bash
# Finally run the following command
python app.py
```

### STEP 05- Run Fronend

```bash
cd FN

npm run dev
```

Now,

```bash
open up you local host and port
```

## Demo

![Chicken Disease Classification](assert\Chicken Disease Classification.mp4)

## Credits

This project draws inspiration and references from the informative guidance provided in the following video:

- Video Title: End To End Deep Learning Project Using MLOPS DVC Pipeline With Deployments Azure And AWS- Krish Naik

- Link: https://www.youtube.com/watch?v=p1bfK8ZJgkE&t=10774s
