FROM ubuntu:24.04-alpine
RUN apt-get update && apt-get install -y curl
CMD ["bash"]
