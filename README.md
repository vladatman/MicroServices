# MicroServices

## Build Docker containers
```shell
> docker compose up
```

## Run application
```shell
> python main.py -m/--method [-t/--text "Message"]
```

## Examples
### Welcome page
```shell
> python main.py -h
```
##### Output
```
  Microservice help

  -h           print help message and exit
  -m/--method  [GET, POST] method for testing
  -t/--text    text of message to insert for POST method
```
### 1
```shell
> python main.py -m post -t "Hello"
```
##### Output
  ```
  Return:
  success
  ```
### 2
```shell
> python main.py -m post
```
##### Output
  ```
  Return:
  success
  ```
### 3
```shell
> python main.py -m get
```
##### Output
  ```
  Return:
  Hello, default message
  ```
