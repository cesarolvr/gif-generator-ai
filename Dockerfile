FROM python:3.10-slim

WORKDIR /app

# Set environment variables for PyTorch
ENV TORCH_CUDA_ARCH_LIST=""
ENV TORCH_NVCC_FLAGS=""
ENV PYTORCH_CUDA_ALLOC_CONF=""

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Remove the ENTRYPOINT to make the container more flexible
CMD ["tail", "-f", "/dev/null"] 