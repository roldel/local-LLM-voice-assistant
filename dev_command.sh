# Via container set up 
 
sudo docker build -t getting-started ./assistant
sudo docker run -it --rm -p 8000:8000 getting-started

## OR

# Via volume binding (requires manual install of packages and requirements)

sudo docker run -it --rm -p 8000:8000 -v $(pwd)/assistant:/app python:slim bash