import {defineStore} from "pinia";
import {showMessage} from "@/utils/message.js";

export const useWebSocketStore = defineStore('websocketStore', {
    state() {
        return {
            data: [],
            status: '等待链接',
            message: '',
            socket: null,
        }
    },
    actions: {
        setData(data) {
            this.data.push(data)
        },
        connect(url) {
            this.socket = new WebSocket(url);
            this.socket.onopen = () => {
                if (this.socket.readyState === WebSocket.OPEN) {
                    this.status = '已经连接'
                }
            };
            this.socket.onclose = () => {
                if (this.socket.readyState === WebSocket.OPEN) {
                    this.status = '等待链接'
                    this.socket.close()
                }
            };
            this.socket.onerror = (e) => {
                this.socket.close();
                this.status = '等待链接'
                console.log(e)
                this.message = e
            };
            this.socket.onmessage = (e) => {
                console.log(e.data)
                console.log('=========================')

                this.setData(e.data)
            }
        },
        disconnect() {
            this.socket.close()
            this.status = '等待链接'
            this.socket = null
        },
        sendData(data) {
            this.socket.send(JSON.stringify(data))
        }
    }
})
