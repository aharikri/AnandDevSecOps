FROM python
MAINTAINER anand.harikrishnan@gmail.com
RUN pip install flask
RUN mkdir /myapp /
COPY ana.py /myapp
WORKDIR /myapp 
EXPOSE 5000 
CMD ["python", "ana.py"]
