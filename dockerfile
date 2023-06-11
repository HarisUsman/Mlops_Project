FROM jupyter/base-notebook:latest

COPY "Model Training.ipynb" "C:/Users/Haris Usman/"

WORKDIR "C:/Users/Haris Usman/"

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
