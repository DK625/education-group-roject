# Stage 1: Dependencies
FROM node:18-alpine AS deps
WORKDIR /app

# Install dependencies for node-gyp
RUN apk add --no-cache python3 make g++

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies with cache mounting
RUN --mount=type=cache,target=/root/.npm \
    npm ci

# Stage 2: Builder
FROM node:18-alpine AS builder
WORKDIR /app

# Copy dependencies from deps stage
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Set build arguments
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# Build with cache mounting
RUN --mount=type=cache,target=/root/.npm \
    npm run build

# Stage 3: Production
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

# Use non-root user for better security
USER nginx

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]