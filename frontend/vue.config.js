module.exports = {
    assetsDir: 'static',
    devServer: {
        proxy: {
            '/api': {
              target: 'http://localhost:8000',
              ws: false,
                changeOrigin: true
            }
        }
    }
};
