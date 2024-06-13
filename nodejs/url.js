const http = require('http')
const url = require("url")
const server = http.createServer()
server.on('request', (req, res) => {
    var urlobj = url.parse(req.url,true)
    var pathName = url.parse(req.url).pathName
    console.log(urlobj.query.name)
    res.writeHead(renderStatus(pathName), { "Content-type": "text/html;charset=utf-8" })
    res.write(renderHTML(pathName))
    res.end()
})
server.listen(3000, () => {
    console.log("[*]server start")
})
function renderStatus(url) {
    var arr = ['/home', '/list', 'login']
    return arr.includes(url) ? 200 : 400
}
function renderHTML(url) {
    switch (url) {
        case '/home':
            return `
                <html>
                    <b>这是Home页面</b>
                </html>
            `
        case '/list':
            return `
                <html>
                    <b>这是List页面</b>
                </html>
            `
        case '/login':
            return `
                <html>
                    <b>这是登陆页面</b>
                </html>
            `
        default:
            return `
                <html>
                    <b>404页面不存在</b>
                </html>
            `
    }
}