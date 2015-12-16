import web
        
urls = (
    '/*', 'index',
    '/favicon.ico', 'icon'
)
app = web.application(urls, globals())

class index:        
    def GET(self):
    	f = open('static/index.html','r+')
    	page = f.read()
    	f.close()
    	return page

class icon:
    def GET(self): raise web.seeother("/static/favicon.ico")

if __name__ == "__main__":
    app.run()