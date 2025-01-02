# Stage 1: Builder
FROM node:18-alpine AS builder
WORKDIR /app

# Copy package files first
COPY package*.json ./

# Install dependencies including dev dependencies
RUN npm install

# Copy the rest of the source code
COPY . .

# Build the app
RUN npm run build

# Stage 2: Production
FROM nginx:alpine
WORKDIR /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Remove default nginx static files
RUN rm -rf ./*

# Copy static files from builder
COPY --from=builder /app/build .

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]