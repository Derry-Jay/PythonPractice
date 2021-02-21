'use strict'
import { cssLoaders } from './utils'
import { build, dev } from '../config'
const isProduction = process.env.NODE_ENV === 'production'

export const loaders = cssLoaders({
    sourceMap: isProduction
        ? build.productionSourceMap
        : dev.cssSourceMap,
    extract: isProduction
})
export const transformToRequire = {
    video: 'src',
    source: 'src',
    img: 'src',
    image: 'xlink:href'
}
