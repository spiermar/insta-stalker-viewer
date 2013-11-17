insta-stalker-viewer
==============

Simple webapp to help visualize insta-stalker results.

cherrypy.cfg
------------

```
[/]
tools.staticdir.root = '/insta-stalker-viewer'
tools.staticdir.on = True
tools.staticdir.dir = ''

[/css]
tools.staticdir.on = True
tools.staticdir.dir = 'static/css'

[/js]
tools.staticdir.on = True
tools.staticdir.dir = 'static/css'

[/img]
tools.staticdir.on = True
tools.staticdir.dir = 'static/css'
```

results.xml
-----------
The script tries to load a file called 'results.xml' from root. The file should follow this format:

```xml
<?xml version="1.0" ?>
<results>
	<item date="Fri, 22 Mar 2013 19:48:53 +0000" image="http://distilleryimage10.s3.amazonaws.com/86cab116932911e2986822000aa8062e_6.jpg" link="http://www.spots.io/image/417431496866114098_245549329" user="_miss_kri"/>
</results>
```
