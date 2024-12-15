# La Lluita Continua - Bits x La Marató (Winner Project)

Respiratory illness outbreaks in schools can escalate quickly, affecting students and the community. Our app tracks symptoms, offering actionable insights to improve prevention and response.

## Inspiration

Our project is inspired by the challenges faced during the COVID-19 pandemic, particularly in schools. The rapid spread of respiratory illnesses highlighted the need for effective tracking, early detection, and prompt response. With this in mind, we created an app that empowers health professionals to monitor symptoms in real time, enabling quicker interventions and reducing the risk of outbreaks. 

## What it does

Our platform is designed to transform how schools and communities monitor and respond to health trends. It offers the following features:

- **Symptom Tracking Interface:** A user-friendly interface enabling students to log their symptoms easily, fostering real-time data collection.

- **Regional Insights:** Provides an overview of health trends across different sanitary regions of Catalonia, aiding targeted interventions and policymaking.

- **Environmental and Climate Data Integration:** Incorporates external data sources to explore correlations between environmental factors and epidemic patterns.

- **Spread of Epidemic Visualization Tool:** Displays the geographical spread of outbreaks.

## How it works

The following are some of the main screens of the application:

<img width="1065" alt="Inici" src="https://github.com/user-attachments/assets/a58c9f45-7f6a-45c6-a819-078fa0bb46d6" />

Students can Register and Login...

<img width="1065" alt="Register Alumne" src="https://github.com/user-attachments/assets/6e34b5fb-1640-4ed3-a540-3a77657daacd" />

<img width="1049" alt="Login Alumne" src="https://github.com/user-attachments/assets/ca6752a6-e23f-42f0-a53b-45ce2c221550" />

...to complete a short quiz everyday to collect syntoms data:

<img width="1022" alt="Enquesta Alumne" src="https://github.com/user-attachments/assets/382beaa6-ba62-4bcd-9858-0a0d7208ead9" />

We store all the responses among other data in a self hosted MongoDB database:

<img width="1288" alt="Mongo DB" src="https://github.com/user-attachments/assets/2ddb3a29-49bb-476a-8eb5-6d6b9f70f15a" />

Doctors can also Register and Login to view various Graphs and Insights obtained in real time from the data collected through the application as well as other souces:

<img width="953" alt="Register Metge" src="https://github.com/user-attachments/assets/ee4782cc-7f8c-48ba-b873-14081dd21678" />

General Overview Line Chart of the evolution of all Registered Symptoms:

<img width="1402" alt="General" src="https://github.com/user-attachments/assets/59e3e97e-cc82-483c-92f4-a70a340ed452" />

Correlation between our collected data and public data of the main deseases:

<img width="1158" alt="Correlació" src="https://github.com/user-attachments/assets/27e11731-4311-4e01-99ee-bbd0a2c2023d" />

Monitoring of various relevant environment variables:

<img width="1407" alt="Entorn" src="https://github.com/user-attachments/assets/c0951d18-c396-4a9a-a5e9-3f0577699099" />

Desease occurrency over time by "Regions Sanitàries":

<img width="1383" alt="Regions Sanitàries" src="https://github.com/user-attachments/assets/9c62edaf-da14-4def-9f5c-c888da65af43" />

Desease spread map animation:

<img width="1403" alt="Mapa" src="https://github.com/user-attachments/assets/c2eac8fe-277f-44f2-a9bd-a5b81ec01d5f" />

## How we built it

We combined powerful backend and frontend technologies to create a robust, yet intuitive system:

- **Python Backend:** Our backend processes data to generate the required plots, connecting seamlessly with a MongoDB database for storage and retrieval.

- **MongoDB Database:** This database provides a scalable and flexible foundation for handling real-time data inputs from schools.

- **Streamlit Dashboard:** The frontend was built using Streamlit, offering an intuitive interface to view plots, trends, and key metrics. The dashboard makes health data accessible and actionable, without the need for technical expertise.

- **Docker Deployment:** We Leveraged Docker to Containerize and seamlessly deploy both our application and database to our own Cloud Server. Thanks to a custom automatic Deployment Pipeline powered by Webhooks triggered by GitHub on every commit in the main branch, we were able to significantly reduce our CI/CD times, enabling our team to iterate faster and with more agility while investing more resources on developing the core functionality of the application.

## What's next

The application is designed to be easily scalable. With more data of the schools, the plots would be more insightful. Additionally, the map can be extended to incorporate SEIR models to predict epidemic expansion.   
