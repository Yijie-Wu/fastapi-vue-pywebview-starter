import axios from "axios";
import {getToken} from "@/utils/token.js";
import {showMessage} from "@/utils/message.js";
import router from "@/router/index.js"


const service = axios.create({
    baseURL:"http://127.0.0.1:8000/",
    timeout: 30000
})


service.interceptors.request.use(config => {
    config.headers['Authorization'] = 'Bearer ' + getToken();
    return config
});

service.interceptors.response.use(res => {
    return res
}, err => {
    if (err.response.status === 401) {
        router.push('/auth/login');
    } else {
        showMessage('error', err.response.data.detail)
        return Promise.reject(err)
    }

});

export default service;
