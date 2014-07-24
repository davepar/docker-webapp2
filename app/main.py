import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        html = (
            '<html><head>'
            '<link rel="stylesheet" type="text/css" href="static/style.css">'
            '</head><body>'
            '<img src="static/hello.svg" width="100">'
            '<p class="hello">world!</p>'
            '</body></html>'
        )
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

def main():
    import os
    from werkzeug.serving import run_simple
    from werkzeug.wsgi import SharedDataMiddleware
    # Add handler for static files
    app_with_static = SharedDataMiddleware(app, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
    })
    # Bind to all addresses (i.e. 0.0.0.0), otherwise the world outside this
    # Docker container won't be able to see the server
    run_simple('0.0.0.0', 8080, app_with_static, use_reloader=True)

if __name__ == '__main__':
    main()
