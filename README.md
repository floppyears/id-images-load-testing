# ID Images Load Testing

The purpose of this repository is to load balance the ID images API using Locust. To run Locust, all you need installed is Docker.

First, create a config.py file from config_example.py. "osu_id_no_image" should be an OSU ID that exists but doesn't have an ID Card image associated with it in Banner. "osu_id_with_image" should be an OSU ID that has an ID Card image associated with it in Banner.

Next, use these commands to build and run the container. Replace target_host with the host you are testing the api against. For testing, api_path in config.py will be appended on to the desired host.

    docker build -t idimages-load-testing .
    docker run -p 8089:8089 \
        -e TARGET_URL=target_host \
        -v "$PWD"/config.py:/config.py:ro \
        idimages-load-testing

Go to localhost:8089 in a web browser to start load testing using the Locust UI. More information on Locust can be found on their [website](http://locust.io)