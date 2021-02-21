'use strict'
import 'eventsource-polyfill'
import { subscribe } from 'webpack-hot-middleware/client?noInfo=true&reload=true'

subscribe(function (event) {
    if (event.action === 'reload') {
        window.location.reload()
    }
})
