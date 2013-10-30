# AINO

Aino server is a local environment picture rerouting service. Aino server sits on a local network and can store and reroute images to multiple services such as Amazon Glacier or SFTP server. Server exposes an API that enables multiple computers and mobile devices to connect to it to upload images.

## Basic Use Case

"I want to upload my images to Aino which reroutes and backups my images to all services I want"

## Basic concepts

Aino environment is built on top of following concepts
- Incoming channels such as REST API, RSS feeds, E-mail
- Outgoing channels such as storing to external file server, image sharing service or an individual computer's hard drive
- Flags that are attached to incoming channel message and are used to reroute images to outgoing channels
- Default routes are preinstalled routes by server owner
- Service queue built using  Redis that dispatches emails to and from channels

One image always arrives from one incoming channels and is rerouted possibly through other incoming channels to its final destinations. Same image can end up in multiple destinations depending on flags and default routes.

## Installation and configuration

- Goal of the project is to provide as self-sufficient package as possible for major modern operating systems.
- Goal of the project is to offer easy configuration using command line tools and web user interface
- Tablets and other mobile computers can communicate with Aino server through RESTful API and a web interface
- Servers defines a plugin interface for adding functionality to service through drop-in plugins.

## WIP

- Project is pre-alpha as of 2013 10 30

## License

Software is license under Apache License as described in [License](LICENSE)

