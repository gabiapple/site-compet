import web
        
urls = (
    '/*', 'index'
)
app = web.application(urls, globals())

class index:        
    def GET(self):
    	f = open('static/index.html','r+')
    	page = f.read()
    	f.close()
    	return page

if __name__ == "__main__":
    app.run()