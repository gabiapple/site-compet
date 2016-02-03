import web
        
urls = (
    '/', 'index',
    '/favicon.ico', 'icon',
    '/([a-zA-Z-]*)', 'pages'
)

app = web.application(urls, globals())

class index:
	def GET(self):
		p = pages()
		return p.GET('../index')

class pages:
	def GET(self, url):
		try:
			f = open('static/pages/' + url + '.html', 'r')
			post = f.read()
			f.close()

			render = web.template.frender('static/template.html')
			return render(post)
		except:
			raise web.seeother('/')

class icon:
    def GET(self):
    	raise web.seeother("/static/favicon.ico")

if __name__ == "__main__":
    app.run()