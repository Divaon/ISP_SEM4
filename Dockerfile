FROM python:3
ADD main.py /
ADD data1.txt /
ADD data2.txt /
RUN pip install numpy
CMD ["python", "./main.py"]
