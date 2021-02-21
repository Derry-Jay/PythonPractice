'use strict'
import { join } from 'path'
import { assetsPath } from './utils'
import { build, dev } from '../config'
import vueLoaderConfig from './vue-loader.conf'

function resolve(dir) {
    return join(__dirname, '..', dir)
}

export const entry = {
    app: './src/main.js'
}
export const output = {
    path: build.assetsRoot,
    filename: '[name].js',
    publicPath: process.env.NODE_ENV === 'production'
        ? build.assetsPublicPath
        : dev.assetsPublicPath
}
export const resolve = {
    extensions: ['.js', '.vue', '.json'],
    alias: {
        '@': resolve('src'),
    }
}
export const module = {
    rules: [
        {
            test: /\.(js|vue)$/,
            loader: 'eslint-loader',
            enforce: 'pre',
            include: [resolve('src'), resolve('test')],
            options: {
                formatter: require('eslint-friendly-formatter')
            }
        },
        {
            test: /\.vue$/,
            loader: 'vue-loader',
            options: vueLoaderConfig
        },
        {
            test: /\.js$/,
            loader: 'babel-loader',
            include: [resolve('src'), resolve('test')]
        },
        {
            test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
            loader: 'url-loader',
            options: {
                limit: 10000,
                name: assetsPath('img/[name].[hash:7].[ext]')
            }
        },
        {
            test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/,
            loader: 'url-loader',
            options: {
                limit: 10000,
                name: assetsPath('media/[name].[hash:7].[ext]')
            }
        },
        {
            test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
            loader: 'url-loader',
            options: {
                limit: 10000,
                name: assetsPath('fonts/[name].[hash:7].[ext]')
            }
        }
    ]
}
