FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Remove the ENTRYPOINT to make the container more flexible
CMD ["tail", "-f", "/dev/null"] 