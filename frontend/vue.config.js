var path = require('path')

module.exports = {
  publicPath: './',
  assetsDir: 'static',
  devServer: {
    // proxy: 'http://localhost:5000'
  },
  transpileDependencies: [
    "vuetify"
  ],
  configureWebpack: {
    resolve: {
      extensions: ['.js', '.vue', '.json'],
      alias: {
        vue$: 'vue/dist/vue.esm.js',
        '@': path.resolve('./src')
      },
    },
  }
}