import cherrypy
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

STEP = 32

def parse_xml(xml_file):
	l = list()
	tree = ET.parse(xml_file)
	root = tree.getroot()
	for item in root:
		i = dict()
		i['user'] = item.get('user')
		i['image'] = item.get('image')
		i['link'] = item.get('link')
		i['date'] = item.get('date')
		l.append(i)
	return l

class Root:
	@cherrypy.expose
	def index(self, page=1):
		tmpl = env.get_template('index.html')
		results = parse_xml('results.xml')
		results = results[(STEP * int(page)) - STEP:(STEP * int(page))]
		return tmpl.render(results = results, page = int(page))

cherrypy.quickstart(Root(), '/', config='cherrypy.cfg')