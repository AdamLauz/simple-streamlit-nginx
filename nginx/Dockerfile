# Pull nginx image from Docker Hub
FROM nginx

# Remove the default nginx config file and replace it with the new one
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

# Copy the certificate and prv key
COPY certs/ngnix_streamlit.crt /etc/nginx/ssl/ngnix_streamlit.crt
COPY certs/ssl_certificate_key /etc/nginx/ssl/ngnix_streamlit.key