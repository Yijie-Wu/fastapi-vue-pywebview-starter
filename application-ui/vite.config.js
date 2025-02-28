import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import { viteCommonjs } from '@originjs/vite-plugin-commonjs'
import {resolve} from 'path'

export default defineConfig({
    plugins: [
        vue(),
        viteCommonjs()
    ],
    resolve: {
        alias: {
            "@": resolve(__dirname, "./src")
        }
    },
    server: {
        host: '127.0.0.1',
        port: 8000,
    }
})
