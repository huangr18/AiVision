# AiVision

install requirement:

opencv - pip install opencv-python

mediapipe - pip install mediapipe

To run the code cd to path/to/pose folder and type python test.py     

or      

python3 test.py

if want to run on the camera instead of demo vedio

-> comment out line 9 in test.py and uncomment line 7 in test.py

-> you can change which camera by changing the value in cv2.VideoCapture(0) (i.e. 1, 2, 3)

# DB connection
1. Make sure Docker has been installed successfully on your machine and check with `docker-compose -v` to make sure the installation is success.
2. Direct into `db` folder and run command `docker-compose -f ai-vision.yml up -d` to start the postgres DB on your local machine. Should be able to see successful response:
```
Digest: sha256:7c0ee16b6a3b4403957ece2c186ff05c57097a557403ae5216ef1286e47c249c
Status: Downloaded newer image for postgres:latest
Creating db_postgres_1 ... done
```
3. Run a `docker ps` command and you can see the new db has been created.
`0e35de9539da   postgres                      "docker-entrypoint.s…"   3 seconds ago   Up 2 seconds          5432/tcp, 0.0.0.0:9000->9000/tcp   db_postgres_1`
4. Download the DB tool `DBeaver`. Create a new DB connect. Update the port number `9001` and database as `test`. Also Use the username and password as `test` for local testing. Click the `test connection` button to check if connection is success.


# Backend service connect with DB
1. Install `pip install psycopg2`
2. Direct into `pose` folder and run `python test_db_connection.py `.
3. Should be able to see the terminal returning proper value. Also, go and check the data in the DBeaver. Should be able to see a new table got created with the value inside.