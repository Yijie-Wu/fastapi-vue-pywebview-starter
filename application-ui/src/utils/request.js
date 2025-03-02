import axios from "axios";

const service = axios.create({
    baseURL:"http://127.0.0.1:8080/",
    timeout: 30000
})

export default service;
