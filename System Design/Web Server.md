# Web Server
----

Jetty is a web server (HTTP), similar to the likes of Tomcat and such, but lighter than most servlet containers. This is closer to the traditional Java way of doing server applications (servlets, WAR files). Like Netty it is sufficiently lightweight to be embedded into Java applications.

Netty is a NIO (non-blocking IO) client server framework which enables quick and easy development of network applications such as protocol servers and clients. It greatly simplifies and streamlines network programming such as TCP and UDP socket server. So Netty is focusing on helping to write NIO/non-blocking, asynchronous network programs.

Geronimo, Glassfish and JBoss support the whole J2EE stack (more or less), and they use/include Tomcat or Jetty for web-containers. The most important part of a fullblown J2EE server besides the web-container used to be the [EJB](http://en.wikipedia.org/wiki/Enterprise_JavaBeans)\-container allowing for deployment of EJBs, having them run in a transactional context etc. 

Nginx is a HTTP server and a reverse proxy. You can for example load balance multiple deployed Jetty instances behind a nginx server.

----

- Date: 2019-03-04
- Tags: #Interview/System-Design 



