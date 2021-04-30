FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 -y
RUN apt-get install python3.8 python3.8-dev python3-pip -y
RUN python3.8 -m pip install pyaudio==0.2.11
CMD python3.8 -c "import pyaudio"

WORKDIR /usr/src/app
COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install PyAudio

#RUN pip3 install PyAudio-0.2.11-cp39-cp39-win_amd64
CMD ["test.py"]
ENTRYPOINT ["python3"]

