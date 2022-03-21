# Simple command reminder application
```
krmd is a simple command reminder application where you can add the commands,configs, parameters you use,and list,
update, delete whenever you want.
It basically consists of 4 commands.
Usages can be found in the Usage section.
```

## Installation

```
$ pip install krmd

```

[![Downloads](https://static.pepy.tech/personalized-badge/krmd?period=month&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/krmd)


## Usage

```
There is 4 command to use. 

1- add:    It is used when the command is wanted to be added.
   -> krmd add "<command>" 

2- list:   It is used when it is desired to display the added commands.
   -> krmd list

3- update: It is used if any of the added commands are wanted to be updated.
   -> krmd update <command_id> "<command>"
      -> krmd update 5 "<command>"

4- delete: It is used to delete any of the added commands.
   -> krmd delete <command_id>
      -> krmd delete 5
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run krmd cli application

$ krmd --help


### run pytest / coverage

$ make test
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `Your local command reminder`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it krmd --help
```
