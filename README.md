spots-explorer
==============

Simple webapp to help visualize spots.io pictures.

cherrypy.cfg
------------

```
[/]
tools.staticdir.root = '/Users/mspier/Workspace/python/cherry/spots'
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

The results file can be created by fetching data direcly from spots.io API. The following code snippet can be used:
[https://gist.github.com/spiermar/5217827](https://gist.github.com/spiermar/5217827)