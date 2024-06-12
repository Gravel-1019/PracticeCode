const http = require('http')
const server = http.createServer()
server.on('request', (req, res) => {
    if (req.url === '/login') {
        res.writeHead(200, { "Content-Type": "text/html;charset=utf-8" })
        res.write(`
        <html>
            <center><b>这里是登录页面</b></center>
        </html>
        `)
        res.end()
    } else if (req.url.trim() === '/') {
        res.writeHead(200, { "Content-Type": "text/html;charset=utf-8" })
        res.write(`
        <html>
            <center><b>默认页面</b></center>
        </html>
        `)
        res.end()
    } else {
        res.writeHead(404, { "Content-Type": "text/html;charset=utf-8" })
        res.write(`
        <html>
            <center><b>Error</b></center>
        </html>
        `)
        res.end()
    }
})
server.listen(3000, () => {
    console.log("[*]server start")
})