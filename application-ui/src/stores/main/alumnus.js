import {defineStore} from "pinia";

export const useAllShowAlumnusStore = defineStore('allShowAlumnusStore', {
    state() {
        return {
            alumnuss: [],
        }
    },
    actions: {
        setAlumnus(data) {
            this.alumnuss = data;
        }
    }
})
