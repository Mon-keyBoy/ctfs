FROM ubuntu:22.04@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e
RUN apt-get update -y
RUN apt-get install socat -y
RUN adduser prob
WORKDIR /home/prob

USER prob
COPY ./prob ./prob
COPY ./flag.txt ./flag.txt
COPY ./start.sh ./start.sh

USER root
RUN chown -R root:root /home/prob
RUN chmod 755 /home/prob
RUN chmod 644 ./flag.txt
RUN chmod 744 ./start.sh
RUN chmod 755 ./prob

CMD ./start.sh
EXPOSE 15252
EXPOSE 15353
