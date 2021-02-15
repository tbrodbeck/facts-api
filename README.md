# summarization-api

Model-directory of [Summarization Toolbox](https://github.com/tbrodbeck/summarization-toolbox) has to be copied to the containers working directory `/app`. Compare line `8` in `Dockerfile` using `./saved_model`: 
```docker
COPY saved_model saved_model
```

Then just build it:
```sh
docker build --tag summ-api .
```

And you can start it with:
```sh
docker run -dp 80:80 summ-api
```
