FROM tiangolo/uwsgi-nginx:python3.8-alpine

# Set environment information
ENV LISTEN_PORT=5000
EXPOSE 5000
ENV UWSGI_INI uwsgi.ini

# Install python packages
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r ./requirements.txt

# Add web application to image
COPY . .
