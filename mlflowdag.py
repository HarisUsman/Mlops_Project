from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import mlflow
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import flask
from datetime import datetime, timedelta



def train_model():
    # Load the data from the .npy file
    features = np.load('/home/saad/Documents/MLOPS_Proj/HOGFeatures.npy')
    print(features.shape)
    labels_np = np.load('/home/saad/Documents/MLOPS_Proj/labels.npy')
    print(labels_np.shape)
    X_train, X_test, y_train, y_test = train_test_split(features, labels_np, test_size=0.2, random_state=42)
    # Train an SVM model
    mlflow.set_experiment('Leaf Disease Detection')
# Start a new MLflow run
    with mlflow.start_run(run_name="SVM"):



    # Train the model
        clf = SVC(kernel='linear', probability=True, random_state=42)
        # Train the classifier on the training data and labels
        clf.fit(X_train, y_train)

        # Log the model parameters and metrics to MLflow
        mlflow.log_param('C', clf.get_params()['C'])
        score =clf.score(X_train, y_train)
        mlflow.log_metric('train_accuracy', score)


        # Evaluate the model
        y_pred = clf.predict(X_test)
        test_accuracy = accuracy_score(y_test, y_pred)

        # Log the test accuracy to MLflow
        mlflow.log_metric('test_accuracy', test_accuracy)

        # Save the model to disk and log it to MLflow
        mlflow.sklearn.log_model(clf, 'model')
    mlflow.end_run()
    return 



default_args = {
  'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(2023, 6, 11),
'email_on_failure': False,
'email_on_retry': False,
'retries': 1,

'retry_delay': timedelta(minutes=5),
}

dag = DAG('MLFLOW1',

default_args=default_args,
description='My first Airflow DAG',
schedule_interval=timedelta(days=1),
catchup=False)

hello_task = PythonOperator(task_id='hello_task',
python_callable=train_model,
dag=dag)

hello_task
