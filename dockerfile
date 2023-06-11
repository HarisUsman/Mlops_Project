# Use a base image with Python 3.8 and Jupyter installed
FROM jupyter/base-notebook:python-3.8

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the working directory
COPY . .

# Install any necessary packages
RUN pip install numpy pandas scikit-learn matplotlib

# Expose the Jupyter Notebook port
EXPOSE 8888

# Run the Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
