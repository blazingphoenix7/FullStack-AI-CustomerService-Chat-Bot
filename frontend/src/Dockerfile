# File: frontend/Dockerfile (Frontend - React)

# Use an official Node runtime as a parent image
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React app
RUN npm run build

# Install serve to serve the React app
RUN npm install -g serve

# Expose port 3000 for the React app
EXPOSE 3000

# Start the React app
CMD ["serve", "-s", "build"]