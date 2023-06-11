FROM jupyter/base-notebook:latest

COPY Model\ Training.ipynb /home/jovyan/work/

WORKDIR /home/jovyan/work

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
