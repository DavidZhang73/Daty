module.exports = {
    assetsDir: 'static',
    devServer: {
        proxy: {
            '/api': {
              target: 'https://daty.davidz.cn',
              ws: false,
                changeOrigin: true
            }
        }
    }
};
