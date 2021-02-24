'use strict'

require('./check-versions')()

process.env.NODE_ENV = 'production'

import { ora } from 'ora'
import { rm } from 'rimraf'
import { join } from 'path'
import { red, cyan, yellow } from 'chalk'
import { webpack } from 'webpack'
import { build } from '../config'
import { webpackConfig } from './webpack.prod.conf'

const spinner = ora('building for production...')
spinner.start()
rm(join(build.assetsRoot, build.assetsSubDirectory), err => {
    if (err) throw err
    webpack(webpackConfig, function (err, stats) {
        spinner.stop()
        if (err) throw err
        process.stdout.write(stats.toString({
            colors: true,
            modules: false,
            children: false,
            chunks: false,
            chunkModules: false
        }) + '\n\n')

        if (stats.hasErrors()) {
            console.log(red('  Build failed with errors.\n'))
            process.exit(1)
        }

        console.log(cyan('  Build complete.\n'))
        console.log(yellow(
            '  Tip: built files are meant to be served over an HTTP server.\n' +
            '  Opening index.html over file:// won\'t work.\n'
        ))
    })
})
